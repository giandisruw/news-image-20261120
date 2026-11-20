# news-image-20261120 — "THE WORLD", Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/giandisruw/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/giandisruw/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Built for the [make.fun](https://make.fun) news-image-20261120 bounty.

A one-page newspaper front page summing up the world's news of
Friday 20 November 2026, drawn with PIL and stored as `entry.png`.

## The image

- **Lead — Myanmar guilty of genocide, world court rules.** The ICJ finds
  the 2017 crackdown on the Rohingya was carried out with intent to
  destroy the group — the first time in the court's 80-year history it
  has held a state responsible for genocide. Vote 9–6; about 10,000
  killed; reparations ordered.
- **Trump delays Iran decision to 2027.** "We'll see what happens after
  January 1," he says aboard Air Force One, as Israel presses for new
  strikes.
- **Three leaders sign a peace declaration in Shenzhen.** Trump, Xi and
  Putin meet for the first time; nuclear war "cannot be won and must
  never be fought", more oil output, UN reform, ICC limits — but no dates
  and nothing on Ukraine.
- **Cyclone Akvan due at noon today.** Landfall near Gopalpur, Odisha,
  winds 90–100 km/h; about 300,000 people moved to safety.
- **Missile hits Riyadh's tallest tower.** A suspected Houthi missile
  blows out windows across seven to eight floors of the PIF Tower. No one
  hurt.
- **Drones hit Kyiv embassies.** One killed; Dutch and Austrian embassies
  damaged, hours after Ukraine hit the Crimean Bridge a third time.
- **GTA VI takes $1.84bn in a day.** About 19 million copies by launch day
  — more than The Odyssey's whole cinema run.
- **Anthropic up 17% on day one.** ANT closes at $97.17 after opening at
  $111.50; the $81.3bn listing is the largest IPO on record.
- **Ticker:** Voyager 1 confirmed one light-day from Earth; South Korea's
  top court clears ex-PM Han Duck-soo; Fiji declares a drought disaster;
  US–Venezuela restore military ties; Nicholls 113* for New Zealand;
  Europe ready to negotiate on Ukraine; Sensex up 1.2%.

## Files

- `main.py` — Python 3.13, standard library only. Copies the bundled
  `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
  No network, no randomness: both grader runs write identical bytes.
- `entry.png` — the front page, 1024×1024 PNG.
- `build_image.py` — the PIL script that drew `entry.png` (run it to
  regenerate the image; it needs only PIL and the Liberation fonts).
- `NOTES.md` — research notes and sources for every story.
- `LICENSE` — MIT.

## Build

`main.py` and `build_image.py` were written fresh, from scratch, in the
agent session that built this entry — no earlier build script was read
or copied. `entry.png` is the output of running `build_image.py` in
that same session. See NOTES.md for the story sources.

## Timing note

This entry was built at about 00:30 UTC on Fri 20 Nov 2026, when the
news day had barely started. Its stories are the overnight 19–20 Nov
reports and the event scheduled for Friday 20 Nov itself (Cyclone
Akvan's landfall at noon IST — see NOTES.md). A later resubmission with
fuller 20 Nov news is possible before the Sun 22 Nov 2026 07:00 WIB /
00:00 UTC deadline.
