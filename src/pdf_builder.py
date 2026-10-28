# -*- coding: utf-8 -*-
"""
Official 5-Page Medical Report PDF Builder for MR.Health.
Uses Chromium / Microsoft Edge headless rendering for pixel-perfect PDF export.
"""
import os
import subprocess
from pathlib import Path
import pymupdf

from .config import OUTPUT_DIR, CSS_DIR, find_browser_executable, PROJECT_ROOT

def build_pdf(output_pdf_path=None):
    """
    Compiles the 5-page official health report to PDF using Headless Chromium / Edge.
    """
    if output_pdf_path is None:
        output_pdf_path = OUTPUT_DIR / "Comprehensive_Health_Report_Mehran_Rahimian.pdf"
    else:
        output_pdf_path = Path(output_pdf_path)

    html_source = OUTPUT_DIR / "Comprehensive_Health_Report_5Pages.html"
    if not html_source.exists():
        raise FileNotFoundError(f"Source HTML template not found at {html_source}")

    browser_bin = find_browser_executable()
    if not browser_bin or not os.path.exists(browser_bin):
        raise RuntimeError("No compatible Chromium/Edge browser found for PDF compilation.")

    file_uri = html_source.resolve().as_uri()

    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={str(output_pdf_path)}",
        file_uri
    ]

    print(f"Compiling PDF via browser: {browser_bin}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Warning: Browser exit code {res.returncode}. Output: {res.stderr}")

    if not output_pdf_path.exists():
        raise RuntimeError("PDF generation failed: output file was not created.")

    # Verification via PyMuPDF
    doc = pymupdf.open(str(output_pdf_path))
    page_count = len(doc)
    doc.close()

    print(f"PDF successfully generated at: {output_pdf_path} (Pages: {page_count}, Size: {output_pdf_path.stat().st_size:,} bytes)")
    return output_pdf_path
