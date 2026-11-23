#!/usr/bin/env python3
"""Render frontpage.html to entry.png with headless Chromium.

Window 1024x1024, device scale factor 1, no sandbox (VM has no user
namespaces for the sandbox). Finds the Chromium binary from the
Playwright cache first, then falls back to any chromium on PATH.

Usage:
    python3 tools/render.py            # render entry.png at 1024x1024
    python3 tools/render.py --measure  # render a tall copy and print the
                                       # natural content height (last row
                                       # that is not the body background)
"""
import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "frontpage.html"
PNG = ROOT / "entry.png"

CANDIDATES = [
    Path.home() / ".cache/ms-playwright/chromium-1255/chrome-linux64/chrome",
    Path.home() / ".cache/ms-playwright/chromium_headless_shell-1255/chrome-headless-shell-linux64/chrome-headless-shell",
    Path.home() / ".cache/ms-playwright/chromium-1255/chrome-linux64/chrome-wrapper",
]


def find_chrome():
    for c in CANDIDATES:
        if c.exists():
            return str(c)
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        p = shutil.which(name)
        if p:
            return p
    return None


def shot(chrome, html_path, png_path, width, height):
    cmd = [
        chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        "--virtual-time-budget=5000",
        f"--screenshot={png_path}", f"file://{html_path}",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        print(r.stdout[-2000:], file=sys.stderr)
        print(r.stderr[-2000:], file=sys.stderr)
        raise SystemExit(f"chromium failed (exit {r.returncode})")
    return png_path


def measure(chrome):
    from PIL import Image
    tall = Path("/tmp/news22_tall.html")
    text = HTML.read_text()
    text = text.replace("height:1024px;", "height:auto;", 1)
    tall.write_text(text)
    out = Path("/tmp/news22_tall.png")
    shot(chrome, tall, out, 1024, 2200)
    im = Image.open(out).convert("RGB")
    w, h = im.size
    bg = (207, 200, 184)  # body background #cfc8b8
    px = im.load()
    last = 0
    for y in range(h - 1, -1, -1):
        row_bg = all(px[x, y] == bg for x in (0, 100, 512, 900, 1023))
        if not row_bg:
            last = y + 1
            break
    print(f"tall render {w}x{h}; natural content height = {last}px "
          f"(page budget 1024px; {'OVER by ' + str(last - 1024) if last > 1024 else 'fits, slack ' + str(1024 - last)}px)")
    return last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--measure", action="store_true")
    args = ap.parse_args()
    chrome = find_chrome()
    if not chrome:
        raise SystemExit("no Chromium binary found")
    if args.measure:
        measure(chrome)
        return
    shot(chrome, HTML, PNG, 1024, 1024)
    data = PNG.read_bytes()
    print(f"wrote {PNG} {len(data)} bytes sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
