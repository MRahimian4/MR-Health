# -*- coding: utf-8 -*-
"""
Configuration and constants for MR.Health medical reporting platform.
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

# Patient Demographics & Profile
PATIENT_INFO = {
    "name_fa": "آقای مهران رحیمیان",
    "name_en": "MR. Mehran Rahimian",
    "age": 34,
    "gender": "Male / مذکر",
    "national_id": "0082348561",
    "reception_date_p1": "۱۴۰۳/۱۲/۲۲",
    "reception_date_p2": "۱۴۰۴/۰۹/۱۵",
    "reception_date_p3": "۱۴۰۵/۰۷/۲۴",
    "lab_name": "آزمایشگاه تخصصی پاتوبیولوژی و ژنتیک امید",
    "doctor": "آقای دکتر بهروزیان",
    "weight_kg": 78.0,
    "height_cm": 178,
    "bmi": 24.62,
    "bmr_kcal": 1740,
    "clinical_status": "پست‌عمل ساسی بای‌پَس (SASI Bypass ~3y) | بدنسازی سنگین ۳ جلسه در هفته",
}

# Executive KPI Metrics
EXECUTIVE_METRICS = [
    {
        "title_fa": "شاخص توده بدنی (BMI)",
        "value": "24.62",
        "unit": "kg/m²",
        "status": "محدوده نرمال و کات عضلانی",
        "status_class": "badge-optimal",
        "desc": "وزن ۷۸ کیلوگرم / قد ۱۷۸ سانتی‌متر"
    },
    {
        "title_fa": "نرخ فیلتراسیون کلیوی (eGFR)",
        "value": "> 90",
        "unit": "mL/min/1.73m²",
        "status": "فیلتراسیون عالی (Stage 1)",
        "status_class": "badge-optimal",
        "desc": "کراتینین ۰.۹۴ سرم و تصفیه بهینه"
    },
    {
        "title_fa": "شاخص فیبروز کبدی (FIB-4)",
        "value": "0.90",
        "unit": "Score",
        "status": "بدون فیبروز و کبد کاملاً پاک",
        "status_class": "badge-optimal",
        "desc": "ALT: 28 U/L | AST: 29 U/L"
    },
    {
        "title_fa": "ویتامین دی سرم (25-OH D3)",
        "value": "58.1",
        "unit": "ng/mL",
        "status": "اشباع مطلوب و مهار پادرد",
        "status_class": "badge-optimal",
        "desc": "رشد پیوسته از ۴۹ به ۵۸.۱"
    },
    {
        "title_fa": "نسبت آتروژنیک (TG / HDL)",
        "value": "1.02",
        "unit": "Ratio",
        "status": "ریسک قلبی بسیار ناچیز",
        "status_class": "badge-optimal",
        "desc": "TG: 48 mg/dL | HDL: 47 mg/dL"
    },
    {
        "title_fa": "سطح پایه متابولیسم (BMR)",
        "value": "1,740",
        "unit": "kcal/day",
        "status": "سوخت‌وساز فعال عضلانی",
        "status_class": "badge-optimal",
        "desc": "مصرف پایه در فاز تثبیت وزن"
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
    
    # Check PATH
    for name in ["msedge.exe", "chrome.exe", "msedge", "google-chrome"]:
        found = shutil.which(name)
        if found:
            return found
            
    return candidates[0]
