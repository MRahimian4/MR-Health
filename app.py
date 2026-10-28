# -*- coding: utf-8 -*-
"""
MR.Health - FastAPI Backend Server
Provides multimodal intake (Scans + 1-min Voice Notes + Text), Gemini AI analysis, and instant PDF/HTML generation.
"""
import os
import sys
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

load_dotenv()

from src.config import OUTPUT_DIR
from src.gemini_analyzer import analyze_checkup, get_reference_dataset
from src.report_generator import generate_full_report_package

app = FastAPI(
    title="MR.Health AI — Clinical Laboratory Analytics Platform",
    description="Multimodal medical checkup analysis powered by Google Gemini 3.8 Flash",
    version="2.0.0"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files mount
static_dir = PROJECT_ROOT / "static"
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = static_dir / "index.html"
    if not index_file.exists():
        return HTMLResponse("<h1>MR.Health is loading...</h1>")
    with open(index_file, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/api/status")
async def get_status():
    has_env_key = bool(os.getenv("GEMINI_API_KEY"))
    return {
        "status": "online",
        "service": "MR.Health AI",
        "has_server_gemini_key": has_env_key,
        "supported_models": ["gemini-3.8-flash", "gemini-4-argon"],
        "max_voice_seconds": 60
    }

@app.get("/api/demo")
async def run_demo():
    """
    Returns instant pre-analyzed checkup for Mehran Rahimian (3-period longitudinal dataset).
    """
    dataset = get_reference_dataset()
    package = generate_full_report_package(dataset, output_prefix="Demo")
    return {
        "success": True,
        "is_demo": True,
        "message": "اطلاعات آزمایش ۳ دوره با موفقیت بارگذاری شد.",
        "data": dataset,
        "pdf_url": "/api/download-pdf/Demo",
        "pdf_base64": package["pdf_base64"],
        "interactive_html": package["interactive_html"]
    }

@app.post("/api/analyze")
async def analyze_lab_checkup(
    files: List[UploadFile] = File(...),
    audio: Optional[UploadFile] = File(None),
    notes: Optional[str] = Form(""),
    api_key: Optional[str] = Form(None)
):
    """
    Multimodal checkup intake: processes lab scans + 1-min voice note + clinical notes via Gemini API.
    """
    try:
        # 1. Read uploaded lab scan files
        processed_files = []
        for f in files:
            content = await f.read()
            mime = f.content_type or "image/jpeg"
            processed_files.append({
                "filename": f.filename,
                "mime_type": mime,
                "data": content
            })

        # 2. Read audio voice note if uploaded
        audio_bytes = None
        audio_mime = "audio/webm"
        if audio:
            audio_bytes = await audio.read()
            audio_mime = audio.content_type or "audio/webm"

        # 3. Call Gemini Multimodal Analyzer
        analysis_result = analyze_checkup(
            files=processed_files,
            audio_bytes=audio_bytes,
            audio_mime=audio_mime,
            notes=notes or "",
            api_key=api_key
        )

        # 4. Generate report package (PDF + Interactive HTML)
        req_id = uuid.uuid4().hex[:8]
        package = generate_full_report_package(analysis_result, output_prefix=req_id)

        return {
            "success": True,
            "is_demo": False,
            "message": "تحلیل هوشمند چندحالته با موفقیت به پایان رسید.",
            "data": analysis_result,
            "pdf_url": f"/api/download-pdf/{req_id}",
            "pdf_base64": package["pdf_base64"],
            "interactive_html": package["interactive_html"]
        }

    except Exception as e:
        print(f"Error during analysis: {e}")
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": str(e)}
        )

@app.get("/api/download-pdf/{prefix}")
async def download_pdf(prefix: str):
    pdf_path = OUTPUT_DIR / f"Comprehensive_Health_Report_{prefix}.pdf"
    if not pdf_path.exists():
        pdf_path = OUTPUT_DIR / "Comprehensive_Health_Report_Mehran_Rahimian.pdf"
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF report not found")
        
    return FileResponse(
        path=str(pdf_path),
        media_type="application/pdf",
        filename="Comprehensive_Health_Report_Mehran_Rahimian.pdf"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
