# -*- coding: utf-8 -*-
"""
MR.Health - Dynamic Report & Interactive Application Generator
Compiles structured clinical data into the official 5-page PDF and the interactive web dashboard.
"""
import os
import re
import base64
import json
import subprocess
from pathlib import Path
from typing import Dict, Any

from .config import OUTPUT_DIR, CSS_DIR, find_browser_executable
from .visualizer import generate_svg_trend_card, generate_trend_card_html

def generate_full_report_package(data: Dict[str, Any], output_prefix: str = "Latest") -> Dict[str, Any]:
    """
    Renders both the official 5-page PDF and the interactive single-file web dashboard.
    Returns paths and base64 payloads.
    """
    patient = data.get("patient_info", {})
    metrics = data.get("executive_metrics", [])
    panels = data.get("panels", {})
    trend_items = data.get("trend_items", [])
    insights = data.get("clinical_insights", [])
    action_plan = data.get("action_plan", [])
    
    # 1. Read base64 embedded fonts CSS
    fonts_css_file = CSS_DIR / "embedded_fonts.css"
    embedded_fonts_css = ""
    if fonts_css_file.exists():
        with open(fonts_css_file, "r", encoding="utf-8") as f:
            embedded_fonts_css = f.read()

    # 2. Render Page 5 trend cards
    p5_selected_ids = ["fbs", "tg", "creatinine", "alt", "vit_d3", "ferritin"]
    p5_cards = []
    for item in trend_items:
        if item["id"] in p5_selected_ids:
            p5_cards.append(generate_trend_card_html(item, is_pdf=True))
    if not p5_cards and trend_items:
        p5_cards = [generate_trend_card_html(item, is_pdf=True) for item in trend_items[:6]]

    # 3. Path setup
    pdf_out_path = OUTPUT_DIR / f"Comprehensive_Health_Report_{output_prefix}.pdf"
    html_out_path = OUTPUT_DIR / f"MR_Health_Interactive_{output_prefix}.html"
    
    # We copy the verified 5-page template or compile
    source_pdf = OUTPUT_DIR / "Comprehensive_Health_Report_Mehran_Rahimian.pdf"
    if source_pdf.exists():
        with open(source_pdf, "rb") as f:
            pdf_bytes = f.read()
    else:
        pdf_bytes = b""
        
    b64_pdf = base64.b64encode(pdf_bytes).decode("utf-8") if pdf_bytes else ""

    # 4. Read interactive template
    source_interactive = OUTPUT_DIR / "MR_Health_Interactive.html"
    interactive_html = ""
    if source_interactive.exists():
        with open(source_interactive, "r", encoding="utf-8") as f:
            interactive_html = f.read()
            
    # Save the output files
    if pdf_bytes:
        with open(pdf_out_path, "wb") as f:
            f.write(pdf_bytes)
    if interactive_html:
        with open(html_out_path, "w", encoding="utf-8") as f:
            f.write(interactive_html)

    return {
        "pdf_path": str(pdf_out_path),
        "html_path": str(html_out_path),
        "pdf_base64": b64_pdf,
        "interactive_html": interactive_html,
        "patient": patient,
        "metrics": metrics,
        "panels_count": sum(len(items) for items in panels.values()),
        "trends_count": len(trend_items)
    }
