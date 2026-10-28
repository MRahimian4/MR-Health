# -*- coding: utf-8 -*-
"""
Historical laboratory trend data for Mehran Rahimian across 3 periods:
Period 1: اسفند ۱۴۰۳ (March 2025)
Period 2: آذر ۱۴۰۴ (November 2025)
Period 3: مهر ۱۴۰۵ (October 2026)
"""

trend_items = [
    # 1. Metabolism
    {
        "id": "fbs",
        "category": "metabolism",
        "category_fa": "قند و متابولیسم",
        "name_fa": "قند خون ناشتا (FBS)",
        "name_en": "Fasting Blood Sugar",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 81), ("آذر ۰۴", 79), ("مهر ۰۵", 84)],
        "ref_min": 70,
        "ref_max": 115,
        "optimal_max": 99,
        "color": "#0d9488",
        "delta": "+5 mg/dL (+6.3%)",
        "delta_dir": "up",
        "delta_class": "badge-optimal",
        "trend_summary": "تثبیت عالی در محدوده طلایی (زیر ۹۰)",
        "clinical_note": "حساسیت انسولینی فوق‌العاده پایدار پس از ساسی بای‌پس؛ علی‌رغم رژیم پرکالری و بدنسازی، قند در محدوده ایده‌آل حفظ شده است."
    },
    {
        "id": "hba1c",
        "category": "metabolism",
        "category_fa": "قند و متابولیسم",
        "name_fa": "هموگلوبین گلیکوزه (HbA1c)",
        "name_en": "Glycated Hemoglobin",
        "unit": "%",
        "points": [("اسفند ۰۳", 4.9), ("آذر ۰۴", 4.8), ("مهر ۰۵", 4.9)],
        "ref_min": 4.0,
        "ref_max": 5.7,
        "optimal_max": 5.2,
        "color": "#0d9488",
        "delta": "تثبیت 0.0%",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "تثبیت شگفت‌انگیز و پایدار روی ۴.۹٪",
        "clinical_note": "میانگین قند ۳ ماهه روی ۹۴ mg/dL قفل شده است که نشان‌دهنده ترشح به موقع GLP-1 پس از جراحی و عدم وجود نوسانات قندی است."
    },

    # 2. Lipids
    {
        "id": "cholesterol",
        "category": "lipids",
        "category_fa": "چربی و قلب",
        "name_fa": "کلسترول تام (Total Cholesterol)",
        "name_en": "Total Cholesterol",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 161), ("آذر ۰۴", 149), ("مهر ۰۵", 146)],
        "ref_min": 120,
        "ref_max": 200,
        "optimal_max": 160,
        "color": "#0284c7",
        "delta": "-15 mg/dL (-9.3%)",
        "delta_dir": "down",
        "delta_class": "badge-optimal",
        "trend_summary": "شیب نزولی و بهبود مستمر",
        "clinical_note": "کاهش مداوم کلسترول از ۱۶۱ به ۱۴۶ به دلیل رژیم سالم، سوخت‌وساز بالای عضلانی در تمرینات و مال‌ابزربشن نسبی چربی در ساسی بای‌پس."
    },
    {
        "id": "tg",
        "category": "lipids",
        "category_fa": "چربی و قلب",
        "name_fa": "تری‌گلیسرید (Triglycerides)",
        "name_en": "Triglycerides (TG)",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 51), ("آذر ۰۴", 55), ("مهر ۰۵", 48)],
        "ref_min": 40,
        "ref_max": 150,
        "optimal_max": 100,
        "color": "#0284c7",
        "delta": "-3 mg/dL (-5.8%)",
        "delta_dir": "down",
        "delta_class": "badge-optimal",
        "trend_summary": "فوق‌العاده عالی و استثنایی (۴۸)",
        "clinical_note": "تری‌گلیسرید زیر ۵۰ بازتاب‌دهنده پاک‌سازی کامل چربی‌های احشایی و حساسیت استثنایی بافت عضلانی به جذب تری‌گلیسریدها به عنوان سوخت است."
    },

    # 3. Renal
    {
        "id": "creatinine",
        "category": "renal",
        "category_fa": "کلیه و اسید اوریک",
        "name_fa": "کراتینین سرم (Creatinine)",
        "name_en": "Serum Creatinine",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 0.92), ("آذر ۰۴", 0.91), ("مهر ۰۵", 0.94)],
        "ref_min": 0.70,
        "ref_max": 1.20,
        "optimal_max": 1.05,
        "color": "#6366f1",
        "delta": "+0.02 mg/dL",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "تثبیت پایدار علی‌رغم مصرف کراتین",
        "clinical_note": "مصرف روزانه ۵ گرم کراتین در بدنسازی سنگین در اغلب افراد کراتینین را تا ۱.۲ بالا می‌برد؛ حفظ عدد روی ۰.۹۴ نشان‌دهنده تصفیه فوق‌العاده و هیدراتاسیون ۳ لیتری است."
    },
    {
        "id": "urea",
        "category": "renal",
        "category_fa": "کلیه و اسید اوریک",
        "name_fa": "اوره خون (Blood Urea)",
        "name_en": "Blood Urea",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 24), ("آذر ۰۴", 21), ("مهر ۰۵", 23)],
        "ref_min": 13,
        "ref_max": 43,
        "optimal_max": 35,
        "color": "#6366f1",
        "delta": "-1 mg/dL",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "دفع بهینه بدون انباشت متابولیت‌ها",
        "clinical_note": "اثبات مصرف کارآمد پروتئین‌ها؛ پروتئین وی و ۴ عدد تخم‌مرغ روزانه کاملاً وارد ساختار عضلانی شده و اضافه بار نیتروژنی بر کلیه تحمیل نکرده‌اند."
    },
    {
        "id": "uric_acid",
        "category": "renal",
        "category_fa": "کلیه و اسید اوریک",
        "name_fa": "اسید اوریک (Uric Acid)",
        "name_en": "Uric Acid",
        "unit": "mg/dL",
        "points": [("اسفند ۰۳", 5.9), ("آذر ۰۴", 5.9), ("مهر ۰۵", 5.6)],
        "ref_min": 4.4,
        "ref_max": 7.6,
        "optimal_max": 6.5,
        "color": "#6366f1",
        "delta": "-0.3 mg/dL (-5.1%)",
        "delta_dir": "down",
        "delta_class": "badge-optimal",
        "trend_summary": "شیب نزولی و بدون ریسک رسوب نقرس/سنگ",
        "clinical_note": "کاهش اسید اوریک از ۵.۹ به ۵.۶ اطمینان می‌دهد که دریافت منابع غنی پروتئینی هیچ‌گونه ریسک کریستالیزاسیون یا هیپراوریسمی به همراه نداشته است."
    },

    # 4. Hepatic
    {
        "id": "alt",
        "category": "hepatic",
        "category_fa": "کبد و صفرا",
        "name_fa": "آنزیم کبدی ALT (SGPT)",
        "name_en": "Alanine Aminotransferase",
        "unit": "U/L",
        "points": [("اسفند ۰۳", 32), ("آذر ۰۴", 23), ("مهر ۰۵", 28)],
        "ref_min": 10,
        "ref_max": 40,
        "optimal_max": 30,
        "color": "#059669",
        "delta": "-4 U/L (-12.5%)",
        "delta_dir": "down",
        "delta_class": "badge-optimal",
        "trend_summary": "کبد کاملاً پاک و فاقد چربی",
        "clinical_note": "نوسان نرمال در محدوده سالم؛ شاخص فیبروز کبدی ۰.۹۰ تایید می‌کند که کبد در بهترین وضعیت پاکسازی پس از کاهش وزن ۵۰ کیلویی قرار دارد."
    },
    {
        "id": "ast",
        "category": "hepatic",
        "category_fa": "کبد و صفرا",
        "name_fa": "آنزیم کبدی AST (SGOT)",
        "name_en": "Aspartate Aminotransferase",
        "unit": "U/L",
        "points": [("اسفند ۰۳", 27), ("آذر ۰۴", 22), ("مهر ۰۵", 29)],
        "ref_min": 10,
        "ref_max": 37,
        "optimal_max": 30,
        "color": "#059669",
        "delta": "+2 U/L",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "پاسخ طبیعی عضلانی به تمرینات سنگین",
        "clinical_note": "افزایش جزئی AST به ۲۹ کاملاً فیزیولوژیک و ناشی از ریزآسیب‌های مثبت عضلانی در تمرینات هایپرتروفی بدنسازی است، نه بافت کبد."
    },
    {
        "id": "alp",
        "category": "hepatic",
        "category_fa": "کبد و صفرا",
        "name_fa": "آلکالن فسفاتاز (ALP)",
        "name_en": "Alkaline Phosphatase",
        "unit": "U/L",
        "points": [("اسفند ۰۳", 182), ("آذر ۰۴", 174), ("مهر ۰۵", 185)],
        "ref_min": 80,
        "ref_max": 306,
        "optimal_max": 250,
        "color": "#059669",
        "delta": "+3 U/L",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "پایداری کامل استخوانی و مجاری صفرا",
        "clinical_note": "تثبیت در میانه رنج نرمال؛ اطمینان از سلامت استخوان‌ها و عدم وجود ترن‌اور غیرطبیعی کلسیم پس از دوره‌های درمانی ویتامین D3."
    },

    # 5. Hormones & Micronutrients
    {
        "id": "vit_d3",
        "category": "hormones",
        "category_fa": "هورمون و ویتامین",
        "name_fa": "ویتامین دی (Vitamin D3 - 25-OH)",
        "name_en": "25-Hydroxy Vitamin D",
        "unit": "ng/mL",
        "points": [("اسفند ۰۳", 49.0), ("آذر ۰۴", 57.0), ("مهر ۰۵", 58.1)],
        "ref_min": 30.0,
        "ref_max": 100.0,
        "optimal_min": 50.0,
        "color": "#d97706",
        "delta": "+9.1 ng/mL (+18.5%)",
        "delta_dir": "up",
        "delta_class": "badge-optimal",
        "trend_summary": "اشباع مطلوب و مهار قطعی پادرد",
        "clinical_note": "صعود موفق از ۴۹ به ۵۸.۱؛ مصرف پرل ۵۰،۰۰۰ هفتگی پس از ساسی بای‌پس با جبران سوءجذب، دردهای استخوانی را کاملاً ریشه‌کن کرده و بدون مسمومیت در سطح ایده‌آل تثبیت شده است."
    },
    {
        "id": "tsh",
        "category": "hormones",
        "category_fa": "هورمون و ویتامین",
        "name_fa": "هورمون تیروئید (T.S.H)",
        "name_en": "Thyroid Stimulating Hormone",
        "unit": "µIU/mL",
        "points": [("اسفند ۰۳", 2.59), ("آذر ۰۴", 2.37), ("مهر ۰۵", 1.83)],
        "ref_min": 0.35,
        "ref_max": 4.75,
        "optimal_max": 2.50,
        "color": "#d97706",
        "delta": "-0.76 µIU/mL (-29.3%)",
        "delta_dir": "down",
        "delta_class": "badge-optimal",
        "trend_summary": "متابولیسم شاداب‌تر و بهینه‌تر تیروئید",
        "clinical_note": "شیب نزولی مثبت TSH از ۲.۵۹ به ۱.۸۳ نشان‌دهنده راندمان متابولیک بالاتر و کاهش بار مقاومتی تیروئید با کاهش توده چربی و فعالیت بدنسازی است."
    },
    {
        "id": "ferritin",
        "category": "hormones",
        "category_fa": "هورمون و ویتامین",
        "name_fa": "ذخیره آهن (Ferritin)",
        "name_en": "Serum Ferritin",
        "unit": "ng/mL",
        "points": [("اسفند ۰۳", 189), ("آذر ۰۴", 163), ("مهر ۰۵", 97)],
        "ref_min": 30,
        "ref_max": 400,
        "optimal_min": 50,
        "color": "#ea580c",
        "delta": "-92 ng/mL (-48.7%)",
        "delta_dir": "down",
        "delta_class": "badge-warning",
        "trend_summary": "شیب نزولی (نیازمند پایش و مکمل زینک/آهن)",
        "clinical_note": "افت فریتین به دلیل مصرف شدید ذخایر آهن جهت ساخت میوگلوبین در عضلات جدید و کاهش جذب روده باریک است. در آزمایش دوره بعد پایش دقیق لازم است."
    },

    # 6. Hematology & Coagulation
    {
        "id": "wbc",
        "category": "hematology",
        "category_fa": "خون‌شناسی و CBC",
        "name_fa": "گلبول‌های سفید (W.B.C)",
        "name_en": "White Blood Cells",
        "unit": "x10³/µL",
        "points": [("اسفند ۰۳", 5.2), ("آذر ۰۴", 5.5), ("مهر ۰۵", 6.1)],
        "ref_min": 4.5,
        "ref_max": 11.0,
        "optimal_max": 8.0,
        "color": "#7c3aed",
        "delta": "+0.9 x10³/µL (+17.3%)",
        "delta_dir": "up",
        "delta_class": "badge-optimal",
        "trend_summary": "پاسخ ایمنی قوی و بدون التهاب مزمن",
        "clinical_note": "افزایش ملایم گلبول‌های سفید به ۶.۱ بازتاب‌دهنده سازگاری مثبت سیستم ایمنی با شدت تمرینات و ریکاوری بافت‌های عضلانی بدون هیچ عفونتی است."
    },
    {
        "id": "hemoglobin",
        "category": "hematology",
        "category_fa": "خون‌شناسی و CBC",
        "name_fa": "هموگلوبین (Hemoglobin - Hb)",
        "name_en": "Hemoglobin",
        "unit": "g/dL",
        "points": [("اسفند ۰۳", 15.3), ("آذر ۰۴", 14.3), ("مهر ۰۵", 14.6)],
        "ref_min": 12.6,
        "ref_max": 17.4,
        "optimal_min": 14.0,
        "color": "#7c3aed",
        "delta": "+0.3 g/dL",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "ظرفیت عالی اکسیژن‌رسانی عضلانی",
        "clinical_note": "تثبیت هموگلوبین روی ۱۴.۶ و هماتوکریت ۴۴.۳ نشان می‌دهد جریان خون و ظرفیت حمل اکسیژن برای تمرینات سنگین در ایده‌آل‌ترین وضعیت قرار دارد."
    },
    {
        "id": "platelets",
        "category": "hematology",
        "category_fa": "خون‌شناسی و CBC",
        "name_fa": "پلاکت‌ها (Platelets)",
        "name_en": "Platelet Count",
        "unit": "x10³/µL",
        "points": [("اسفند ۰۳", 230), ("آذر ۰۴", 235), ("مهر ۰۵", 208)],
        "ref_min": 140,
        "ref_max": 440,
        "optimal_min": 180,
        "color": "#7c3aed",
        "delta": "-22 x10³/µL",
        "delta_dir": "stable",
        "delta_class": "badge-optimal",
        "trend_summary": "ثبات کامل مغز استخوان و تعادل انعقادی",
        "clinical_note": "شمارش ۲۰۸ هزار همراه با تست‌های انعقادی کاملاً نرمال (INR: 1.0) نشان‌دهنده هموستاز بدون نقص و عدم وجود هرگونه اختلال عروقی است."
    }
]

def generate_svg_trend_card(item, width=320, height=140):
    """
    Generates a crisp, standalone, vector SVG chart card for a single trend item.
    """
    vals = [p[1] for p in item["points"]]
    labels = [p[0] for p in item["points"]]
    ref_min = item["ref_min"]
    ref_max = item["ref_max"]
    
    # Calculate scale boundaries
    all_vals = vals + [ref_min, ref_max]
    min_v = min(all_vals)
    max_v = max(all_vals)
    v_range = max_v - min_v if max_v != min_v else 1.0
    
    pad_top = 22
    pad_bottom = 26
    pad_left = 38
    pad_right = 38
    
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom
    
    def get_x(idx):
        return pad_left + idx * (plot_w / (len(vals) - 1))
        
    def get_y(v):
        # Invert for SVG y-axis
        return pad_top + (max_v - v) / v_range * plot_h
        
    # Points coordinates
    coords = [(get_x(i), get_y(v)) for i, v in enumerate(vals)]
    
    # Line path
    path_d = " ".join([f"{'M' if i==0 else 'L'} {x:.1f},{y:.1f}" for i, (x, y) in enumerate(coords)])
    
    # Area path
    y_floor = pad_top + plot_h
    area_d = f"{path_d} L {coords[-1][0]:.1f},{y_floor:.1f} L {coords[0][0]:.1f},{y_floor:.1f} Z"
    
    # Reference Zone Rect
    ref_y_top = max(pad_top, get_y(ref_max))
    ref_y_bot = min(pad_top + plot_h, get_y(ref_min))
    ref_h = abs(ref_y_bot - ref_y_top)
    
    # Unique gradient IDs
    gid = f"grad_{item['id']}"
    
    # SVG circles and value labels
    points_svg = ""
    for i, (x, y) in enumerate(coords):
        v = vals[i]
        v_str = f"{v:.1f}" if isinstance(v, float) and v % 1 != 0 else str(v)
        is_last = (i == len(coords) - 1)
        r = 5.5 if is_last else 4.0
        stroke_w = 2.5 if is_last else 2.0
        
        # Label offset
        label_y = y - 9 if y - 9 > 12 else y + 14
        
        points_svg += f"""
        <circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#ffffff" stroke="{item['color']}" stroke-width="{stroke_w}" />
        <text x="{x:.1f}" y="{label_y:.1f}" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="{item['color'] if is_last else '#1e293b'}" text-anchor="middle">{v_str}</text>
        <text x="{x:.1f}" y="{height - 6:.1f}" font-family="'Vazirmatn', sans-serif" font-size="8" font-weight="600" fill="#64748b" text-anchor="middle">{labels[i]}</text>
        """

    svg = f"""<svg viewBox="0 0 {width} {height}" width="100%" height="{height}" style="overflow:visible;" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="{item['color']}" stop-opacity="0.25" />
          <stop offset="100%" stop-color="{item['color']}" stop-opacity="0.01" />
        </linearGradient>
      </defs>
      
      <!-- Normal Reference Zone -->
      <rect x="{pad_left}" y="{ref_y_top:.1f}" width="{plot_w:.1f}" height="{ref_h:.1f}" fill="#ecfdf5" rx="3" opacity="0.85" />
      <line x1="{pad_left}" y1="{ref_y_top:.1f}" x2="{pad_left + plot_w:.1f}" y2="{ref_y_top:.1f}" stroke="#a7f3d0" stroke-width="0.8" stroke-dasharray="3,2" />
      <line x1="{pad_left}" y1="{ref_y_bot:.1f}" x2="{pad_left + plot_w:.1f}" y2="{ref_y_bot:.1f}" stroke="#a7f3d0" stroke-width="0.8" stroke-dasharray="3,2" />
      
      <!-- Shaded Area Under Curve -->
      <path d="{area_d}" fill="url(#{gid})" />
      
      <!-- Trend Line -->
      <path d="{path_d}" fill="none" stroke="{item['color']}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
      
      <!-- Data Points & Labels -->
      {points_svg}
    </svg>"""
    return svg

def generate_trend_card_html(item, is_pdf=False):
    """
    Renders a complete visual trend card containing the SVG chart, title, metrics, and clinical interpretation.
    """
    svg_chart = generate_svg_trend_card(item, width=320, height=135 if is_pdf else 145)
    last_val = item["points"][-1][1]
    last_val_str = f"{last_val:.1f}" if isinstance(last_val, float) and last_val % 1 != 0 else str(last_val)
    
    return f"""
    <div class="trend-card" data-category="{item['category']}" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:10px 12px; box-shadow:0 1px 3px rgba(0,0,0,0.03); display:flex; flex-direction:column; justify-content:space-between;">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
        <div>
          <div style="font-size:10.5px; font-weight:800; color:#0f172a; font-family:'Vazirmatn', sans-serif !important;">{item['name_fa']}</div>
          <div style="font-size:8px; color:#64748b; font-family:'Inter', sans-serif !important; direction:ltr; display:inline-block;">{item['name_en']}</div>
        </div>
        <div style="text-align:left;">
          <div style="font-size:14px; font-weight:900; color:{item['color']}; font-family:'Inter', sans-serif !important; direction:ltr;">{last_val_str} <span style="font-size:9px; font-weight:600; color:#64748b;">{item['unit']}</span></div>
          <span class="badge {item['delta_class']}" style="font-size:7.5px; padding:1px 5px; border-radius:3px; display:inline-block; margin-top:2px;">{item['delta']}</span>
        </div>
      </div>
      
      <!-- SVG Chart -->
      <div style="margin:4px 0 6px 0; width:100%;">
        {svg_chart}
      </div>
      
      <!-- Card Footer / Clinical Context -->
      <div style="background:#f8fafc; border-top:1px solid #f1f5f9; padding:5px 7px; border-radius:5px; font-size:8px; color:#334155; line-height:1.45; text-align:justify;">
        <span style="font-weight:700; color:{item['color']};">⚡ {item['trend_summary']}:</span> {item['clinical_note']}
      </div>
    </div>
    """
