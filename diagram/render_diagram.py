#!/usr/bin/env python3
"""
render_diagram.py - Script tự động render file PlantUML (.puml) sang SVG và PNG
Sử dụng chuẩn encoding từ diagram-skills-package và server PlantUML.
"""
import sys
import os
import zlib
import urllib.request

_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

def _encode6bit(b):
    return _ALPHABET[b & 0x3F]

def _append3bytes(b1, b2, b3):
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return _encode6bit(c1) + _encode6bit(c2) + _encode6bit(c3) + _encode6bit(c4)

def encode_plantuml(data: bytes) -> str:
    out = []
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        b1 = chunk[0]
        b2 = chunk[1] if len(chunk) > 1 else 0
        b3 = chunk[2] if len(chunk) > 2 else 0
        out.append(_append3bytes(b1, b2, b3))
    return "".join(out)

def render(puml_path):
    puml_path = puml_path.strip('"\'')
    if not os.path.exists(puml_path):
        print(f"Error: File không tồn tại: {puml_path}")
        sys.exit(1)
    
    with open(puml_path, "rb") as f:
        data = f.read()
    
    compressed = zlib.compress(data, 9)[2:-4]
    encoded = encode_plantuml(compressed)
    
    dir_name = os.path.dirname(os.path.abspath(puml_path))
    file_stem = os.path.splitext(os.path.basename(puml_path))[0]
    svg_path = os.path.normpath(os.path.join(dir_name, f"{file_stem}.svg"))
    png_dir = os.path.join(dir_name, "png")
    os.makedirs(png_dir, exist_ok=True)
    png_path = os.path.normpath(os.path.join(png_dir, f"{file_stem}.png"))
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Render SVG
    print(f"Rendering SVG for {puml_path}...")
    svg_url = f"https://www.plantuml.com/plantuml/svg/{encoded}"
    req_svg = urllib.request.Request(svg_url, headers=headers)
    with urllib.request.urlopen(req_svg) as resp:
        svg_data = resp.read()
        with open(svg_path, "wb") as f:
            f.write(svg_data)
    print(f"-> Created SVG: {svg_path} ({len(svg_data)} bytes)")
    
    # Render PNG
    try:
        print(f"Rendering PNG for {puml_path}...")
        png_url = f"https://www.plantuml.com/plantuml/png/{encoded}"
        req_png = urllib.request.Request(png_url, headers=headers)
        with urllib.request.urlopen(req_png) as resp:
            png_data = resp.read()
            if os.path.exists(png_path):
                try:
                    os.remove(png_path)
                except Exception:
                    pass
            with open(png_path, "wb") as f:
                f.write(png_data)
        print(f"-> Created PNG: {png_path} ({len(png_data)} bytes)")
    except Exception as e:
        print(f"Warning: Could not update PNG ({e}), but SVG is ready!")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "crm-lifecycle-swimlane.puml")
    render(target)
