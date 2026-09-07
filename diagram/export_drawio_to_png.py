#!/usr/bin/env python3
"""
export_drawio_to_png.py
Xuất file .drawio sang PNG chất lượng cao thông qua viewer Diagrams.net và Edge Headless.
Tự động cắt viền (autocrop) để ảnh vừa khít và xóa file cũ trước khi ghi.
"""
import sys
import os
import json
import html
import subprocess
from PIL import Image, ImageChops

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def export_drawio_to_png(drawio_path, output_png_path=None):
    drawio_path = os.path.abspath(drawio_path)
    if not os.path.exists(drawio_path):
        print(f"Error: Không tìm thấy file {drawio_path}")
        return False

    dir_name = os.path.dirname(drawio_path)
    file_stem = os.path.splitext(os.path.basename(drawio_path))[0]
    
    if output_png_path is None:
        png_dir = os.path.join(dir_name, "png")
        os.makedirs(png_dir, exist_ok=True)
        output_png_path = os.path.join(png_dir, f"{file_stem}.png")

    # Xóa file PNG cũ nếu tồn tại
    if os.path.exists(output_png_path):
        try:
            os.remove(output_png_path)
            print(f"Đã xóa file PNG cũ: {output_png_path}")
        except Exception as e:
            print(f"Cảnh báo: Không thể xóa file cũ ({e})")

    with open(drawio_path, "r", encoding="utf-8") as f:
        xml_data = f.read()

    config = {
        "highlight": "none",
        "nav": False,
        "resize": True,
        "toolbar": "none",
        "edit": "",
        "xml": xml_data
    }
    config_json = json.dumps(config)
    escaped_attr = html.escape(config_json, quote=True)

    temp_html = os.path.join(dir_name, f"_temp_{file_stem}.html")
    temp_raw_png = os.path.join(dir_name, f"_temp_{file_stem}_raw.png")

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{file_stem}</title>
    <style>
        body {{ margin: 0; padding: 30px; background: #ffffff; }}
    </style>
</head>
<body>
    <div class="mxgraph" style="max-width:100%; border:none;" data-mxgraph="{escaped_attr}"></div>
    <script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>
</body>
</html>"""

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    edge_candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    ]
    browser_bin = None
    for cand in edge_candidates:
        if os.path.exists(cand):
            browser_bin = cand
            break

    if not browser_bin:
        print("Error: Không tìm thấy trình duyệt Edge hoặc Chrome")
        return False

    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--virtual-time-budget=6000",
        f"--screenshot={temp_raw_png}",
        "--window-size=1800,1900",
        temp_html
    ]

    print(f"Đang render {file_stem}.drawio sang PNG...")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if not os.path.exists(temp_raw_png):
        print("Render thất bại!")
        if os.path.exists(temp_html):
            os.remove(temp_html)
        return False

    # Autocrop bằng Pillow
    try:
        img = Image.open(temp_raw_png).convert("RGB")
        bg = Image.new("RGB", img.size, (255, 255, 255))
        diff = ImageChops.difference(img, bg)
        bbox = diff.getbbox()
        padding = 30
        if bbox:
            left = max(0, bbox[0] - padding)
            top = max(0, bbox[1] - padding)
            right = min(img.width, bbox[2] + padding)
            bottom = min(img.height, bbox[3] + padding)
            cropped = img.crop((left, top, right, bottom))
            cropped.save(output_png_path, "PNG", optimize=True)
        else:
            img.save(output_png_path, "PNG")
        print(f"-> Đã xuất PNG thành công: {output_png_path} ({os.path.getsize(output_png_path)} bytes)")
    finally:
        # Dọn dẹp file tạm
        if os.path.exists(temp_html):
            os.remove(temp_html)
        if os.path.exists(temp_raw_png):
            os.remove(temp_raw_png)

    return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "crm-lifecycle-swimlane.drawio")
    export_drawio_to_png(target)
