# -*- coding: utf-8 -*-
"""
MR.Health - Master CLI & Pipeline Entrypoint
Builds the 5-page official clinical report (PDF) and the interactive web application (HTML).
"""
import argparse
import sys
import webbrowser
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.config import OUTPUT_DIR
from src.pdf_builder import build_pdf
from src.web_builder import build_web_app

def main():
    parser = argparse.ArgumentParser(
        description="MR.Health — Clinical Health Analytics & Reporting Platform"
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generate only the official 5-page PDF report"
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Generate only the interactive Web Application (HTML)"
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Build and automatically open the Interactive Web App in default browser"
    )
    args = parser.parse_args()

    print("=" * 65)
    print("  MR.Health — Laboratory Analytics & Reporting Platform")
    print("  Patient: Mehran Rahimian (34yo, Post-SASI Bypass / Fitness)")
    print("=" * 65)

    build_all = not (args.pdf or args.web)

    pdf_out = None
    if build_all or args.pdf:
        print("\n[1/2] Building Official 5-Page PDF Report...")
        pdf_out = build_pdf()

    html_out = None
    if build_all or args.web or args.open:
        print("\n[2/2] Building Interactive Single-File Web Application...")
        html_out = build_web_app(pdf_path=pdf_out)

    print("\n" + "=" * 65)
    print("Build complete! Deliverables available in:")
    print(f"  - PDF:  {OUTPUT_DIR / 'Comprehensive_Health_Report_Mehran_Rahimian.pdf'}")
    print(f"  - HTML: {OUTPUT_DIR / 'MR_Health_Interactive.html'}")
    print("=" * 65)

    if args.open and html_out:
        print(f"\nOpening {html_out.resolve().as_uri()} in browser...")
        webbrowser.open(html_out.resolve().as_uri())

if __name__ == "__main__":
    main()
