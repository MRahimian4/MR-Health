# -*- coding: utf-8 -*-
"""
Interactive Web Application Builder for MR.Health.
Generates a zero-CORS, 100% offline-ready single-file HTML app with embedded Base64 PDF export.
"""
import os
import base64
import json
from pathlib import Path

from .config import OUTPUT_DIR, CSS_DIR, PROJECT_ROOT
from .data import all_parameters
from .trend_data import trend_items
from .visualizer import generate_svg_trend_card, generate_trend_card_html

def build_web_app(output_html_path=None, pdf_path=None):
    """
    Builds the interactive single-file web application with inlined Base64 PDF.
    """
    if output_html_path is None:
        output_html_path = OUTPUT_DIR / "MR_Health_Interactive.html"
    else:
        output_html_path = Path(output_html_path)

    if pdf_path is None:
        pdf_path = OUTPUT_DIR / "Comprehensive_Health_Report_Mehran_Rahimian.pdf"
    else:
        pdf_path = Path(pdf_path)

    # 1. Read PDF binary for Base64 injection
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            b64_pdf = base64.b64encode(f.read()).decode("utf-8")
        print(f"Embedded official PDF ({pdf_path.stat().st_size:,} bytes) into Web App.")
    else:
        b64_pdf = ""
        print("Warning: Official PDF not found. Web App generated without embedded PDF export binary.")

    # 2. Read embedded fonts CSS
    fonts_css_file = CSS_DIR / "embedded_fonts.css"
    if fonts_css_file.exists():
        with open(fonts_css_file, "r", encoding="utf-8") as f:
            embedded_fonts_css = f.read()
    else:
        embedded_fonts_css = ""

    # 3. Enhance trend items with pre-rendered SVGs
    trend_items_enhanced = []
    for t in trend_items:
        t_copy = dict(t)
        t_copy["svg"] = generate_svg_trend_card(t, width=320, height=140)
        trend_items_enhanced.append(t_copy)

    # We read the template from output/MR_Health_Interactive.html if it exists, or update the Base64 inside
    source_html = OUTPUT_DIR / "MR_Health_Interactive.html"
    if source_html.exists():
        with open(source_html, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace base64 if needed
        import re
        content = re.sub(r'const pdfBase64 = ".*?";', f'const pdfBase64 = "{b64_pdf}";', content, flags=re.DOTALL)
        
        with open(output_html_path, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        # If not present, copy from scratch
        shutil.copy(r"C:\Users\Mehran\.gemini\antigravity\scratch\MR_Health_Interactive.html", str(output_html_path))

    print(f"Interactive Web App successfully written to: {output_html_path} ({output_html_path.stat().st_size:,} bytes)")
    return output_html_path
