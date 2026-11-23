# The World in One Page — Sunday Edition

A 1024×1024 broadsheet front page summing up the world news of
**Sunday 22 November 2026** in one image: 50 real stories across
7 regions, 18 of them drawn as original SVG illustrations, with a
world map, a UTC timeline of the day, a stat strip and a date check.

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/AdelineZiv24/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/AdelineZiv24/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>

Live values from `GET https://make.fun/api/competitions/news-image-20261122/requirements`
(read 23 Nov 2026): competition `news-image-20261122`, status **open**,
prize pool **$100** (#1 $20 · #2 $12 · #3 $6 · #4–10 $2 · #11–50 $1.20),
entries close **2026-11-24 00:00 UTC** (Tue 24 Nov 07:00 WIB), results due
**2026-12-08 08:00 UTC**. Dev leaderboard at build time: 11,328 entries;
top cohort runs 35–39 stories with 13–15 illustrated cards.

## What's on the page

- **Masthead** — the date as the giant headline, "22 NOVEMBER", with an
  italic deck naming the day's top three stories: 186 drones over
  Ukraine, COP31 collapsing in Antalya, Iran's radar claim in Bahrain.
- **50 stories** — Asia-Pacific 9 · Europe 10 · Americas 10 · Mideast 11 ·
  Africa 4 · Oceania 4 · World/Space 2.
- **18 drawn stories** — 3 leads + 15 grid cards, every illustration an
  original SVG drawn for this edition, each carrying a REPORTED / DISPUTED /
  CLAIM / FORECAST pill and a numbered pin on the map.
- **Stat strip** — 6 stats from the day's stories, numerals 32px in red.
- **The day in UTC** — 8 timed stops, 00:22 to 17:45 UTC.
- **Map** — schematic world map, 600×185, 18 numbered pins, on a dark
  panel with the reading guide beside it.
- **Date check** — 14 near-miss stories from other days kept out, 5 items
  reported Sunday but dated earlier, 3 "Not yet" items, and the claim:
  every story here is Sunday 22 November 2026, except items the page
  dates earlier.
- **Briefs 19–50** — every brief sourced.

## Measured against the 21 Nov edition

| | 21 Nov | 22 Nov |
| --- | --- | --- |
| Stories | 50 | 50 |
| Drawn / illustrated | 16 | **18** |
| Dark share | 0.353 | **0.418** |
| Thumbnail dark @256 | 0.301 | **0.374** |
| Stat numerals | 32px red | 32px red |
| Self-audit | 35/35 | **35/35** |

## Files

| File | What it is |
| --- | --- |
| `frontpage.html` | The whole page: HTML + CSS + inline SVG art |
| `entry.png` | Rendered 1024×1024 front page |
| `tools/render.py` | Headless-Chromium renderer (window 1024×1024, scale 1) |
| `tools/audit.py` | 35-check self-audit (HTML rules + PNG gates) |
| `main.py` | Copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png |
| `SOURCES.md` | Numbered sources 1–50 with date evidence |
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
see `SOURCES.md` for the outlet, headline and date evidence of each of
the 50. All illustrations are original SVG art drawn for this edition;
all text is our own writing.
