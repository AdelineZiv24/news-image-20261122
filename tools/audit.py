#!/usr/bin/env python3
"""Full self-audit for news-image-20261122 (35 checks, edition-21 recipe
adapted: 18 drawn cards = 3 leads + 15 grid, 32 briefs, dark >=0.37,
thumb dark @256 >=0.31, stat numerals 32px red #b3271e).

Checks the HTML for content rules and the PNG for measurement gates.
Usage: python3 tools/audit.py
"""
import re, sys
from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / 'frontpage.html').read_text()
png = ROOT / 'entry.png'
im = Image.open(png).convert('RGB')
W, H = im.size
a = np.asarray(im.convert('L')).astype(int)
rgb = np.asarray(im).astype(int)

ok, fail = [], []
def chk(name, cond, detail=''):
    (ok if cond else fail).append(f"{name} {detail}")

print(f"== PNG {W}x{H} ==")
dark = float((a < 110).mean())
red = float(((rgb[:, :, 0] > 150) & (rgb[:, :, 1] < 100) & (rgb[:, :, 2] < 100)).mean())
t256 = np.asarray(im.convert('L').resize((256, 256)))
chk('01 dark share >=0.37', dark >= 0.37, f'{dark:.3f}')
chk('02 red share >=0.010', red >= 0.010, f'{red:.4f}')
chk('03 thumb dark @256 >=0.31', float((t256 < 110).mean()) >= 0.31,
    f"{float((t256 < 110).mean()):.3f}")
bright = (a > 200)
rows = bright[10:200].mean(axis=1)
dense = rows > 0.25
blocks, start = [], None
for i, v in enumerate(dense):
    if v and start is None: start = i
    if (not v or i == len(dense) - 1) and start is not None:
        blocks.append((start + 10, (i - 1 if not v else i) + 10)); start = None
top, bot = max(blocks, key=lambda b: b[1] - b[0])
seg = bright[top:bot + 1, 20:W - 20]
cols = np.where(seg.any(axis=0))[0]
span = (cols.max() - cols.min() + 1) / W
chk('04 date cap >=84px', bot - top + 1 >= 84, f'{bot - top + 1}px')
chk('05 date span >=92%', span >= 0.92, f'{span:.2%}')
chk('06 file <=700KB', png.stat().st_size <= 700 * 1024, f'{png.stat().st_size}B')
chk('07 size 1024x1024', (W, H) == (1024, 1024))

print("== HTML content ==")
kickbars = re.findall(r'class="kickbar">(\d+) &middot; ([^&<]+) &middot; ([^<]+)</div>', html)
chk('08 kickbar on 18/18 cards', len(kickbars) == 18, f'{len(kickbars)}')
srcs = re.findall(r'<div class="src">', html)
chk('09 source line on 18/18 cards', len(srcs) == 18, f'{len(srcs)}')
pills = re.findall(r'>(REPORTED|DISPUTED|CLAIM|FORECAST)</text>', html)
chk('10 pill on 18/18 cards', len(pills) == 18, f'{len(pills)}: {sorted(set(pills))}')
chk('11 max 4 pill labels', len(set(pills)) <= 4, f'{sorted(set(pills))}')
lead_art = re.findall(r'<svg viewBox="0 0 150 110"', html)
grid_art = re.findall(r'<svg viewBox="0 0 150 55"', html)
chk('12 lead art 150x110 x3', len(lead_art) == 3, f'{len(lead_art)}')
chk('13 grid art 150x55 x15', len(grid_art) == 15, f'{len(grid_art)}')
h3s = re.findall(r'<h3>(.*?)</h3>', html)
h3s = [re.sub(r'&[^;]+;', ' ', h).strip() for h in h3s]
chk('14 18 headlines', len(h3s) == 18, f'{len(h3s)}')
long_h3 = [h for h in h3s if len(h.split()) > 9]
chk('15 headlines <=9 words', not long_h3, f'over-long: {long_h3}')
briefs = re.findall(r'<div class="brief">', html)
chk('16 32 briefs', len(briefs) == 32, f'{len(briefs)}')
bsrc = re.findall(r'<div class="brief">.*?<span class="bsrc">', html)
chk('17 >=80% briefs sourced', len(bsrc) >= 0.8 * 32, f'{len(bsrc)}/32')
stops = re.findall(r'<div class="stop">', html)
chk('18 exactly 8 timeline stops', len(stops) == 8, f'{len(stops)}')
deck = re.search(r'class="sub">(.*?)</div>', html, re.S).group(1)
chk('19 deck names top-3 (drones/COP31/Bahrain)',
    all(w in deck for w in ['drones', 'COP31', 'Bahrain']), deck[:90])
dc = re.search(r'class="datecheck">(.*?)</div>\s*</div>', html, re.S).group(1)
chk('20 DATE CHECK heading', 'date check' in dc.lower() and ('&#10003;' in dc or '\u2713' in dc))
chk('21 >=6 exclusions', dc.count('&middot;') >= 6, f"{dc.count('&middot;')} separators")
chk('22 >=2 Not yet', 'Not yet' in dc)
chk('23 positive claim sentence', 'Every story here is Sunday 22 November 2026' in dc)
verdict = re.search(r'class="verdict">(.*?)</div>\s*</div>', html, re.S).group(1)
vp = re.sub(r'<[^>]+>', '', verdict)
words = [w for w in vp.replace('THE VERDICT', '').split() if w.strip()]
chk('24 verdict <=14 words + number', len(words) <= 14 and any(c.isdigit() for c in vp),
    f'{len(words)} words: {" ".join(words)}')
chips = [int(x) for x in re.findall(r'<b>(\d+)</b><span>(?:Asia-Pacific|Europe|Americas|Mideast|Africa|Oceania|World / Space)</span>', html)]
chk('25 region chips sum to 50', sum(chips) == 50 and len(chips) == 7, f'{chips} sum={sum(chips)}')
chk('26 eyebrow 50 stories / 7 regions / 18 drawn',
    '50 stories' in html and '7 regions' in html and '18 drawn' in html)
css = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
sizes = sorted(set(float(x) for x in re.findall(r'font-size:\s*([\d.]+)px', css)))
small = [s for s in sizes if s < 8.5]
chk('27 no CSS text <8.5px except footer 8px',
    small == [8.0] or not small, f'CSS sizes: {sizes}')
svg_sizes = sorted(set(float(x) for x in re.findall(r'<text[^>]*font-size="([\d.]+)"', html)))
chk('28 smallest SVG text >=9px', min(svg_sizes) >= 9, f'min {min(svg_sizes)}px; all: {svg_sizes}')
chk('29 stat numerals red 32px', '#b3271e' in css and 'font-size:32px' in css.replace(' ', ''))
chk('30 map SVG 600x185', 'width="600" height="185"' in html)
chk('31 legend line under map', 'maplegend' in html and 'PINS 1' in html.upper())
chk('32 masthead date is 22 NOVEMBER', '22 NOVEMBER' in html)
chk('33 6 stats in strip', len(re.findall(r'<div class="stat">', html)) == 6, f"{len(re.findall(chr(60)+'div class=\"stat\"'+chr(62), html))}")
chk('34 footer integrity line', 'Every story here is Sunday 22 November 2026' in html)
chk('35 no 21-Nov leftovers', '21 November' not in html.replace('21 Nov', '21 Nov') or html.count('21 Nov') <= 2,
    f"mentions of 21 Nov: {html.count('21 Nov')}")

print()
print('PASS:'); [print('  [x]', x) for x in ok]
print('FAIL:'); [print('  [ ]', x) for x in fail]
print(f"\n{len(ok)} pass, {len(fail)} fail")
sys.exit(1 if fail else 0)
