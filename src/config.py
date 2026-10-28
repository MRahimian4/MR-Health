# -*- coding: utf-8 -*-
"""
Configuration and constants for MR.Health medical reporting platform.
Sample data is anonymized and generalized for demonstration purposes.
"""
from pathlib import Path
import os
import shutil

# Base project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_DIR = PROJECT_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
CSS_DIR = ASSETS_DIR / "css"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Sample Patient Demographics (Anonymized / Fictional)
PATIENT_INFO = {
    "name_fa": "آقای آریا رادمنش (پرونده نمونه)",
    "name_en": "Mr. Arya Radmanesh (Sample)",
    "age": 35,
    "gender": "Male / مذکر",
    "national_id": "0078912345",
    "reception_date_p1": "۱۴۰۳/۱۱/۱۸",
    "reception_date_p2": "۱۴۰۴/۰۸/۲۲",
    "reception_date_p3": "۱۴۰۵/۰۷/۲۸",
    "lab_name": "آزمایشگاه تخصصی پاتوبیولوژی و ژنتیک پارس (نمونه)",
    "doctor": "دکتر کامران شمس (متخصص غدد و متابولیسم)",
    "weight_kg": 77.5,
    "height_cm": 180,
    "bmi": 23.92,
    "bmr_kcal": 1765,
    "clinical_status": "پایش دوره‌ای سالیانه سلامت | ورزش فیتنس و رژیم تغذیه ورزشی",
}

# Executive KPI Metrics (Fictionalized & Anonymized)
EXECUTIVE_METRICS = [
    {
        "title_fa": "شاخص توده بدنی (BMI)",
        "value": "23.92",
        "unit": "kg/m²",
        "status": "محدوده نرمال و متناسب",
        "status_class": "badge-optimal",
        "desc": "وزن ۷۷.۵ کیلوگرم / قد ۱۸۰ سانتی‌متر"
    },
    {
        "title_fa": "نرخ فیلتراسیون کلیوی (eGFR)",
        "value": "> 90",
        "unit": "mL/min/1.73m²",
        "status": "تصفیه گلومرولی بهینه (Stage 1)",
        "status_class": "badge-optimal",
        "desc": "کراتینین ۰.۹۵ سرم و هیدراتاسیون کافی"
    },
    {
        "title_fa": "شاخص فیبروز کبدی (FIB-4)",
        "value": "0.88",
        "unit": "Score",
        "status": "فاقد فیبروز و بافت کبدی سالم",
        "status_class": "badge-optimal",
        "desc": "ALT: 26 U/L | AST: 28 U/L"
    },
    {
        "title_fa": "ویتامین دی سرم (25-OH D3)",
        "value": "54.2",
        "unit": "ng/mL",
        "status": "اشباع مطلوب و بدون کمبود",
        "status_class": "badge-optimal",
        "desc": "رشد تدریجی از ۳۸ به ۵۴.۲"
    },
    {
        "title_fa": "نسبت آتروژنیک (TG / HDL)",
        "value": "1.12",
        "unit": "Ratio",
        "status": "ریسک قلبی-عروقی بسیار پایین",
        "status_class": "badge-optimal",
        "desc": "TG: 56 mg/dL | HDL: 50 mg/dL"
    },
    {
        "title_fa": "سطح پایه متابولیسم (BMR)",
        "value": "1,765",
        "unit": "kcal/day",
        "status": "سوخت‌وساز استاندارد پایه",
        "status_class": "badge-optimal",
        "desc": "کالری پایه برای فعالیت عضلانی"
    }
]

def find_browser_executable():
    """
    Auto-detects Microsoft Edge or Google Chrome binary on Windows.
    """
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    
    for name in ["msedge.exe", "chrome.exe", "msedge", "google-chrome"]:
        found = shutil.which(name)
        if found:
            return found
            
    return candidates[0]
