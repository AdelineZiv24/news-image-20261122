# The World in One Page — Sunday Edition

A 1024×1024 broadsheet front page summing up the world news of
**Sunday 22 November 2026** in one image: 32 real stories across
7 regions, 13 of them drawn as original SVG illustrations, with a
light world map, a UTC timeline of the day, a stat strip, a region
colour bar and a date check — on a cream page in the bright,
airy family of the previous edition's final winners.

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/AdelineZiv24/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/AdelineZiv24/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>

Live values from `GET https://make.fun/api/competitions/news-image-20261122/requirements`
(read 23 Nov 2026): competition `news-image-20261122`, status **open**,
prize pool **$100** (#1 $20 · #2 $12 · #3 $6 · #4–10 $2 · #11–50 $1.20),
entries close **2026-11-24 00:00 UTC** (Tue 24 Nov 07:00 WIB), results due
**2026-12-08 08:00 UTC**.

## What's on the page

- **Masthead** — the full date as the giant headline, "Sunday
  22 November 2026", with an italic deck naming the day's top three
  stories: 186 drones over Ukraine, COP31 collapsing at Antalya,
  Iran's radar claim in Bahrain.
- **32 stories** — Europe 9 · Asia-Pacific 7 · Americas 5 · Mideast 5 ·
  Africa 3 · Oceania 2 · World/Space 1, shown as a colour bar with
  per-region counts under the masthead.
- **13 drawn stories** — 3 large leads + 10 standard cards, every
  illustration an original SVG drawn for this edition, each with a
  named source and a CONFIRMED / OFFICIAL / REPORTED / CLAIM pill
  (legend beside the briefs).
- **Stat strip** — 6 stats from the day's stories, numerals 32px in red
  on cream, each numbered back to its story.
- **The day in UTC** — 8 timed stops, 02:00 to 17:45 UTC.
- **Map** — light schematic world map, 440×205, 13 numbered pins,
  beside the briefs.
- **Date check** — 8 near-miss stories from other days kept out,
  4 items reported Sunday but dated earlier, 2 "Not yet" items, and
  the claim: every story here is Sunday 22 November 2026, except
  items the page dates earlier.
- **Briefs 14–32** — 19 more stories, every one sourced.

## Design note — v2 rebuild

The first build of this edition followed our older house recipe
(dark page, 50 stories, 18 small drawings). After the 20 Nov
edition's final results were analysed, this page was rebuilt to the
surface family of that edition's final top 10: cream/ivory page
(dark-area share gated to 0.12–0.20 by `tools/audit.py`), the full
date as the headline, fewer stories with larger and more colourful
art, a light and smaller map, red-on-cream statistics, and a named
source plus confidence pill on every drawn card. All stories, text
and artwork are unchanged in substance — the same Sunday, reported
the same way; only the design was rebuilt.

## Files

| File | What it is |
| --- | --- |
| `frontpage.html` | The whole page: HTML + CSS + inline SVG art |
| `entry.png` | Rendered 1024×1024 front page |
| `tools/render.py` | Headless-Chromium renderer (window 1024×1024, scale 1) |
| `tools/audit.py` | 35-check self-audit (HTML rules + PNG gates) |
| `main.py` | Copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png |
| `SOURCES.md` | Numbered sources with date evidence |
| `LICENSE` | MIT |
| `.makefun/owner.json` | make.fun repo-owner wallet record |

## Render

```sh
python3 tools/render.py          # writes entry.png (1024×1024)
python3 tools/render.py --measure  # natural content height check
python3 tools/audit.py           # 35 checks, must be 35 pass / 0 fail
MAKEFUN_OUTPUT_DIR=out python3 main.py  # copies entry.png to out/
```

## Sources

All stories happened or were first reported on Sunday 22 November 2026;
see `SOURCES.md` for the outlet, headline and date evidence of each.
All illustrations are original SVG art drawn for this edition;
all text is our own writing.
