# -*- coding: utf-8 -*-
"""
SVG vector charts and visual card generator for MR.Health.
Produces standalone responsive SVG charts with shaded normal reference bands.
"""

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
        return pad_top + (max_v - v) / v_range * plot_h
        
    coords = [(get_x(i), get_y(v)) for i, v in enumerate(vals)]
    path_d = " ".join([f"{'M' if i==0 else 'L'} {x:.1f},{y:.1f}" for i, (x, y) in enumerate(coords)])
    
    y_floor = pad_top + plot_h
    area_d = f"{path_d} L {coords[-1][0]:.1f},{y_floor:.1f} L {coords[0][0]:.1f},{y_floor:.1f} Z"
    
    ref_y_top = max(pad_top, get_y(ref_max))
    ref_y_bot = min(pad_top + plot_h, get_y(ref_min))
    ref_h = abs(ref_y_bot - ref_y_top)
    
    gid = f"grad_{item['id']}"
    
    points_svg = ""
    for i, (x, y) in enumerate(coords):
        v = vals[i]
        v_str = f"{v:.1f}" if isinstance(v, float) and v % 1 != 0 else str(v)
        is_last = (i == len(coords) - 1)
        r = 5.5 if is_last else 4.0
        stroke_w = 2.5 if is_last else 2.0
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
    <div class="trend-card" data-category="{item['category']}" onclick="openTrendHUD('{item['id']}')" style="background:#ffffff; border:1px solid #cbd5e1; border-radius:8px; padding:10px 12px; box-shadow:0 1px 3px rgba(0,0,0,0.03); display:flex; flex-direction:column; justify-content:space-between; cursor:pointer;">
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
