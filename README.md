# 🩺 MR.Health — Clinical Analytics & Laboratory Reporting Platform

> **A modern, offline-first clinical reporting and longitudinal biomarker analytics platform designed for high-precision health monitoring.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Format: PDF & Interactive HTML](https://img.shields.io/badge/Deliverables-PDF%20%7C%20Interactive%20HTML-0d9488.svg)](#)

---

## 📋 Overview

**MR.Health** is a specialized laboratory intelligence suite built to track, analyze, and visualize longitudinal health markers. Designed specifically for post-bariatric surgery (SASI Bypass) recovery and athletic bodybuilding adaptation, the system processes multi-period panel data to deliver:

1. **Official 5-Page Medical Report (PDF)**:
   - Pixel-perfect A4 printable layout compiled via headless Chromium/Edge.
   - 7 comprehensive biomarker panels with full-width, zero-wrap data tables.
   - Dedicated visual trend analytics page with vector SVG charts and body composition progression timeline.
   - Rigorous clinical insights and actionable 4-phase monitoring roadmap.

2. **Interactive Single-File Web Application (HTML)**:
   - 100% offline-ready with embedded Base64 fonts (Vazirmatn & Inter) and zero CORS dependencies.
   - Interactive Heads-Up Display (HUD) modal for all 35 parameters with detailed physiological interpretation.
   - Dynamic in-category SVG trend charts and a dedicated **📈 Trends Analytics Dashboard** tab.
   - One-click direct PDF export engine backed by an inlined Base64 binary payload for guaranteed identical 5-page PDF downloads.

---

## 🏛️ Project Architecture

```
MR Health/
├── src/
│   ├── __init__.py           # Package marker & metadata
│   ├── config.py             # Paths, patient demographics, and browser discovery
│   ├── data.py               # Master lab dataset (35 parameters + urinalysis)
│   ├── trend_data.py         # 16 longitudinal biomarkers across 3 historical periods
│   ├── visualizer.py         # Standalone SVG sparkline & trend card generator
│   ├── pdf_builder.py        # Headless browser PDF compilation engine
│   └── web_builder.py        # Interactive single-file web app compiler
├── assets/
│   ├── css/
│   │   └── embedded_fonts.css  # Base64 WOFF2 fonts for offline zero-CORS rendering
│   └── fonts/
│       ├── font_0.woff2 to font_6.woff2
│       └── fonts.css
├── output/
│   ├── Comprehensive_Health_Report_Mehran_Rahimian.pdf   # Official 5-page PDF
│   ├── MR_Health_Interactive.html                        # Interactive Web App
│   └── Comprehensive_Health_Report_5Pages.html           # Print template HTML
├── main.py                   # Master CLI execution pipeline
├── requirements.txt          # Python dependencies (PyMuPDF)
├── .gitignore                # Git ignore configuration
└── README.md                 # Project documentation
```

---

## 🔬 Clinical Scope & Monitored Panels

The system tracks 35 biochemical and hematological parameters across 7 specialized clinical categories:

| # | Panel Category | Key Monitored Parameters |
|---|---|---|
| **1** | **Metabolism & Glycemic Control** | Fasting Blood Sugar (FBS), 2-Hour Postprandial Glucose, HbA1c, BMR |
| **2** | **Lipid & Cardiovascular Profile** | Total Cholesterol, Triglycerides (TG), HDL-C, LDL-C, TG/HDL Ratio |
| **3** | **Renal Function & Electrolytes** | Serum Creatinine, Blood Urea, Uric Acid, eGFR (CKD-EPI) |
| **4** | **Hepatic & Biliary Function** | ALT (SGPT), AST (SGOT), Alkaline Phosphatase (ALP), Total Bilirubin, FIB-4 |
| **5** | **Hormonal, Vitamins & Micronutrients**| 25-OH Vitamin D3, TSH, Serum Ferritin, Calcium, Phosphorus, Zinc |
| **6** | **Hematology & Hemostasis** | Complete Blood Count (CBC: WBC, RBC, Hb, Hct, MCV, Plt), PT, INR |
| **7** | **Urinalysis (Complete Dipstick & Micro)** | Physical, Chemical (Protein, Glucose, Blood), Microscopic (Cells, Crystals) |

---

## 🚀 Quickstart & Usage

### 1. Installation

Clone the repository and install the minimal requirements:

```bash
git clone https://github.com/MRahimian4/MR-Health.git
cd "MR-Health"

# Install dependencies
pip install -r requirements.txt
```

### 2. Generate Deliverables via CLI

Run the master pipeline to compile both the official PDF and the interactive web application:

```bash
# Build both PDF and Interactive Web App
python main.py

# Build only the official 5-page PDF report
python main.py --pdf

# Build only the interactive Web Application
python main.py --web

# Build and automatically open the Web App in your default browser
python main.py --open
```

---

## 📊 Longitudinal Trend Tracking

The platform tracks 3 distinct historical milestones:
- **Period 1**: اسفند ۱۴۰۳ (March 2025) — Baseline recovery
- **Period 2**: آذر ۱۴۰۴ (November 2025) — Mid-term adaptation
- **Period 3**: مهر ۱۴۰۵ (October 2026) — Hypertrophy & athletic maintenance

Vector sparklines render with:
- Shaded green bands representing age- and gender-adjusted normal reference ranges.
- Precise data point nodes with numerical values.
- Delta indicator badges showing directional progression (`+`, `-`, or `Stable`).

---

## 📄 License

This project is released under the **MIT License**.
Authored by **Mehran Rahimian**.
