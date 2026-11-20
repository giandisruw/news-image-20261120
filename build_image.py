#!/usr/bin/env python3
"""Draw the front page for Friday 20 November 2026.

Reads nothing but the story constants below, uses only the standard
library plus Pillow, touches no network, no clock and no randomness:
running it twice produces the same bytes. Writes entry.png next to
this file (or to the path in --out).
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
MARGIN = 34
CW = W - 2 * MARGIN  # 956

PAPER = (247, 243, 231)
INK = (18, 18, 18)
RED = (140, 22, 22)
GREY = (96, 90, 80)
DARK = (24, 24, 24)
PALE_LINE = (120, 112, 96)

FONT_DIR = "/usr/share/fonts/truetype/liberation"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = "LiberationSerif-Bold.ttf"
SERIF = "LiberationSerif-Regular.ttf"
SERIF_I = "LiberationSerif-Italic.ttf"
SANS_B = "LiberationSans-Bold.ttf"
SANS = "LiberationSans-Regular.ttf"

F_MAST = font(SERIF_B, 78)
F_DATE = font(SANS_B, 25)
F_TAG = font(SANS, 14)
F_KICK = font(SANS_B, 19)
F_LEAD_HEAD = font(SERIF_B, 50)
F_LEAD_SUB = font(SERIF_I, 22)
F_LEAD_BODY = font(SERIF, 16)
F_FACT = font(SANS_B, 14)
F_HEAD = font(SERIF_B, 30)
F_HEAD_SM = font(SERIF_B, 24)
F_BODY = font(SERIF, 16)
F_BODY_SM = font(SERIF, 15)
F_TICK = font(SANS_B, 15)
F_FOOT = font(SANS, 13)


def wrap(d, text, f, width):
    """Greedy word wrap; returns a list of lines that fit in width."""
    lines = []
    for chunk in text.split("\n"):
        words = chunk.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for w in words[1:]:
            trial = cur + " " + w
            if d.textlength(trial, font=f) <= width:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def para(d, x, y, width, text, f, leading, fill=INK):
    """Draw wrapped paragraph; return y just below the last line."""
    for line in wrap(d, text, f, width):
        d.text((x, y), line, font=f, fill=fill)
        y += leading
    return y


def rule(d, y, weight=2, x0=None, x1=None):
    x0 = MARGIN if x0 is None else x0
    x1 = W - MARGIN if x1 is None else x1
    d.line([(x0, y), (x1, y)], fill=INK, width=weight)
    return y + weight


def double_rule(d, y):
    rule(d, y, 3)
    rule(d, y + 6, 1)
    return y + 10


def kicker(d, x, y, text):
    d.text((x, y), text, font=F_KICK, fill=RED)
    return y + 26


def story_block(d, x, y, width, kick, headline, body, head_font, head_lead,
                 body_font=F_BODY, body_lead=20):
    """One headed story; returns y below the block."""
    y = kicker(d, x, y, kick)
    head_lines = wrap(d, headline, head_font, width)
    for line in head_lines:
        d.text((x, y), line, font=head_font, fill=INK)
        y += head_lead
    y += 2
    y = para(d, x, y, width, body, body_font, body_lead)
    return y


LEAD_HEAD = "MYANMAR GUILTY OF GENOCIDE"
LEAD_SUB = ("The Hague finds the 2017 crackdown was carried out with intent "
            "to destroy the Rohingya \u2014 a first for the court.")
LEAD_BODY_L = ("THE HAGUE \u2014 The International Court of Justice ruled on "
               "Thursday that Myanmar committed genocide against its Rohingya "
               "minority \u2014 the first time in the court\u2019s 80-year "
               "history it has held a state responsible for the crime.")
LEAD_BODY_R = ("By nine votes to six, the judges found the 2017 "
               "\u201cclearance operations\u201d in Rakhine state were carried "
               "out with intent to destroy a substantial part of the group. "
               "About 10,000 were violently killed, the court found, and it "
               "ordered Myanmar to pay reparations.")
LEAD_FACTS = ("THE VOTE  9\u20136      \u00b7      ABOUT 10,000 KILLED IN 2017      "
              "\u00b7      REPARATIONS ORDERED      \u00b7      CASE BROUGHT BY THE GAMBIA, 2019")

STORIES_2 = [
    ("WASHINGTON",
     "TRUMP DELAYS IRAN DECISION TO 2027",
     "President Trump said on Thursday he was in no rush to order new "
     "strikes on Iran, telling reporters he would decide \u201cafter the "
     "beginning of the year\u201d. He spoke aboard Air Force One, as Israel "
     "presses for a new bombing campaign."),
    ("SHENZHEN",
     "THREE LEADERS SIGN PEACE DECLARATION",
     "The first-ever three-way meeting of the US, China and Russia ended "
     "on Thursday with a four-point declaration: a nuclear war \u201ccannot "
     "be won and must never be fought\u201d, more oil output, UN reform and "
     "limits on the ICC."),
]

STORIES_3 = [
    ("ODISHA",
     "AKVAN DUE AT NOON",
     "Severe Cyclone Akvan is due to cross the Odisha coast near Gopalpur "
     "around noon today, with winds of 90\u2013100 km/h. About 300,000 "
     "people have moved to safety."),
    ("RIYADH",
     "MISSILE HITS RIYADH",
     "A suspected Houthi missile struck Riyadh\u2019s PIF Tower on Thursday, "
     "blowing out windows across seven to eight floors of the 80-storey "
     "tower. No one was hurt."),
    ("KYIV",
     "DRONES HIT KYIV",
     "Russian drones killed one person and damaged the Dutch and Austrian "
     "embassies in Kyiv on Thursday, after Ukraine hit the Crimean Bridge "
     "a third time."),
]

STORIES_4 = [
    ("CULTURE",
     "GTA VI TAKES $1.84BN IN A DAY",
     "Rockstar\u2019s Grand Theft Auto VI sold about 19 million copies by "
     "launch day, Sensor Tower estimates \u2014 more than the $1.805bn "
     "Nolan\u2019s The Odyssey took in its whole cinema run. Analysts expect "
     "$3bn by year-end."),
    ("MARKETS",
     "ANTHROPIC UP 17% DAY ONE",
     "Anthropic closed its first day on the Nasdaq at $97.17, up 17% on its "
     "$83 issue price, after opening at $111.50. The $81.3bn listing is the "
     "largest IPO on record. The offering is due to close today."),
]

TICKER_1 = ("VOYAGER 1 \u00b7 NASA confirms the probe is one light-day from "
           "Earth      \u00b7      SOUTH KOREA \u00b7 Top court clears ex-PM "
           "Han Duck-soo")
TICKER_2 = ("FIJI \u00b7 Drought disaster declared      \u00b7      "
           "US\u2013VENEZUELA \u00b7 Military ties restored      \u00b7      "
           "CRICKET \u00b7 Nicholls 113* as NZ reach 243\u20135")
TICKER_3 = ("GERMANY \u00b7 \u2018Coalition of the Willing\u2019 meets in Berlin "
           "\u2014 Europe ready to negotiate      \u00b7      INDIA \u00b7 "
           "Sensex gains 1.2% on Thursday")


def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    y = 22
    # ---- masthead ------------------------------------------------------
    mast = "THE WORLD"
    mw = d.textlength(mast, font=F_MAST)
    d.text(((W - mw) / 2, y), mast, font=F_MAST, fill=INK)
    y += 86
    date = "FRIDAY  20  NOVEMBER  2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, y), date, font=F_DATE, fill=RED)
    y += 36
    tag = "THE DAY\u2019S WORLD NEWS IN ONE PAGE"
    tw = d.textlength(tag, font=F_TAG)
    d.text(((W - tw) / 2, y), tag, font=F_TAG, fill=GREY)
    y += 22
    y = double_rule(d, y)
    y += 8

    # ---- lead story ----------------------------------------------------
    y = kicker(d, MARGIN, y, "THE HAGUE  \u2014  WORLD COURT")
    for line in wrap(d, LEAD_HEAD, F_LEAD_HEAD, CW):
        d.text((MARGIN, y), line, font=F_LEAD_HEAD, fill=INK)
        y += 56
    y += 2
    y = para(d, MARGIN, y, CW, LEAD_SUB, F_LEAD_SUB, 27)
    y += 6
    col_w = (CW - 24) // 2
    y_left = para(d, MARGIN, y, col_w, LEAD_BODY_L, F_LEAD_BODY, 20)
    y_right = para(d, MARGIN + col_w + 24, y, col_w, LEAD_BODY_R,
                  F_LEAD_BODY, 20)
    y = max(y_left, y_right) + 5
    fw = d.textlength(LEAD_FACTS, font=F_FACT)
    d.text(((W - fw) / 2, y), LEAD_FACTS, font=F_FACT, fill=RED)
    y += 20
    y = rule(d, y, 2)
    y += 8

    # ---- row 2: two stories --------------------------------------------
    col_w = (CW - 28) // 2
    y2 = story_block(d, MARGIN, y, col_w, STORIES_2[0][0], STORIES_2[0][1],
                     STORIES_2[0][2], F_HEAD, 34)
    y2b = story_block(d, MARGIN + col_w + 28, y, col_w, STORIES_2[1][0],
                      STORIES_2[1][1], STORIES_2[1][2], F_HEAD, 34)
    y = max(y2, y2b) + 3
    y = rule(d, y, 1)
    y += 8

    # ---- row 3: three stories ------------------------------------------
    col_w = (CW - 2 * 24) // 3
    ends = []
    for i, (kick, head, body) in enumerate(STORIES_3):
        x = MARGIN + i * (col_w + 24)
        ends.append(story_block(d, x, y, col_w, kick, head, body,
                                F_HEAD_SM, 28, F_BODY_SM, 18))
    y = max(ends) + 3
    y = rule(d, y, 1)
    y += 8

    # ---- row 4: two stories --------------------------------------------
    col_w = (CW - 28) // 2
    y4 = story_block(d, MARGIN, y, col_w, STORIES_4[0][0], STORIES_4[0][1],
                     STORIES_4[0][2], F_HEAD, 34, F_BODY, 19)
    y4b = story_block(d, MARGIN + col_w + 28, y, col_w, STORIES_4[1][0],
                      STORIES_4[1][1], STORIES_4[1][2], F_HEAD, 34, F_BODY,
                      19)
    y = max(y4, y4b) + 8

    # ---- ticker ---------------------------------------------------------
    band_y = y
    band_h = 76
    d.rectangle([(MARGIN, band_y), (W - MARGIN, band_y + band_h)], fill=DARK)
    ty = band_y + 8
    for line in (TICKER_1, TICKER_2, TICKER_3):
        for seg in wrap(d, line, F_TICK, CW - 20):
            d.text((MARGIN + 10, ty), seg, font=F_TICK, fill=(240, 238, 230))
            ty += 19
    y = band_y + band_h + 6

    if y > H - 8:
        raise SystemExit("layout overflow: content ends at y=%d" % y)
    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    out = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "entry.png")
    img = draw_page()
    img.save(out, format="PNG", optimize=True)
    print("wrote %s (%dx%d)" % (out, W, H))


if __name__ == "__main__":
    main()
