"""Two generated diagrams for the pathways.

    python3 row_diagrams.py        writes previews to /tmp for checking

  pathway_diagram()   four verticals, Junior spanning below, Foundation at the base
  ladder_diagram()    every group as a rung, ordered by hours a week

Both are built from PROGRAMS in layers_common.py, so a group cannot appear in a
diagram under a name it no longer has. That is what went wrong with the previous
ladder: it still said TOPS 2x and REC-AG 14&U.

Everything is positioned by calculation rather than by hand, so labels cannot
end up on top of each other.
"""

import base64
import math
import re

from layers_common import PROGRAMS, pathway

DISP = "'Arial Black', Arial, Helvetica, sans-serif"
SANS = "Arial, Helvetica, sans-serif"

NAVY, TEAL, CYAN, RED, INK, INK_SOFT, LINE, FOAM = (
    "#0A2E3F", "#136B77", "#3FBFB0", "#D64545", "#152225", "#4B5B60", "#DAD3C2", "#FFFFFF")
PURPLE = "#7A5AA8"

# Six pathways, six colours, all from the ROW palette. Recreation is deliberately
# the neutral grey: it is a different choice rather than a lower one, and a
# colour that read as "less" would say the wrong thing.
COLOUR = {"Foundation": CYAN, "Junior": TEAL, "Recreation": INK_SOFT,
          "Regional": RED, "Provincial": PURPLE, "National": NAVY}
TEXT_ON = {CYAN: INK, INK_SOFT: FOAM, RED: FOAM, PURPLE: FOAM, NAVY: FOAM, TEAL: FOAM}

# Within a vertical the highest group sits at the top, so progression reads
# upward from the Junior layer.
ORDER = {"Recreation": ["REC AM", "REC PM"],
         "Regional": ["SD", "AGD 1", "AGD 2"],
         "Provincial": ["PD1", "PD2", "PD3"],
         "National": ["ND"],
         "Junior": ["TOPS 2", "TOPS 1", "JD2", "JD1"],
         "Foundation": ["RSA"]}

SESSIONS = {short: sess for _pw, _n, short, sess, _h in PROGRAMS}
HOURS = {short: hrs for _pw, _n, short, _s, hrs in PROGRAMS}


def _txt(x, y, s, size=13, fill=INK, font=SANS, anchor="middle", weight=None):
    # An SVG is XML, so a bare ampersand is a parse error. "18&U" has to be
    # written "18&amp;U" or the whole image fails to render.
    s = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+);)", "&amp;", str(s))
    w = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{w}>{s}</text>')


def _chip(x, y, w, h, label, sub, colour):
    """A group inside a pathway area. White, so the pathway colour stays the
    thing that groups them, with the name in navy and the sessions beside it."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{FOAM}" '
            f'stroke="{colour}" stroke-width="2"/>'
            + _txt(x + w / 2, y + h / 2 + 1, label, 13.5, NAVY, DISP)
            + _txt(x + w / 2, y + h - 7, sub, 9.5, INK_SOFT, SANS))


# Tier, group, age guide, sessions. Built to match the club's own pathway chart:
# three tiers with the entry rung at the bottom, Junior spanning beneath, and the
# Academy at the base.
#
# Recreation has two groups and they are NOT a progression: REC AM and REC PM are
# the same age range and differ only in when they train. So no arrow is drawn
# between them, which is the whole point.
TIERS = ["Performance", "Development", "Entry"]
GRID = {
    "Recreation": {"Development": "REC AM", "Entry": "REC PM"},
    "Regional":   {"Performance": "SD", "Development": "AGD 1", "Entry": "AGD 2"},
    "Provincial": {"Performance": "PD1", "Development": "PD2", "Entry": "PD3"},
    "National":   {"Performance": "ND"},
}
FULL = {"REC AM": "Recreation, mornings", "REC PM": "Recreation, evenings",
        "SD": "Senior Development", "AGD 1": "Age Group Development 1",
        "AGD 2": "Age Group Development 2", "PD1": "Provincial Development 1",
        "PD2": "Provincial Development 2", "PD3": "Provincial Development 3",
        "ND": "National Development", "TOPS 1": "TOPS, three a week",
        "TOPS 2": "TOPS, two a week", "JD1": "Junior Development 1",
        "JD2": "Junior Development 2", "RSA": "ROW Swim Academy"}
AGES = {"REC AM": "18&U", "REC PM": "18&U", "SD": "18&U", "AGD 1": "14&U", "AGD 2": "12&U",
        "PD1": "18&U", "PD2": "14&U", "PD3": "12&U", "ND": "18&U",
        "TOPS 1": "10&U", "TOPS 2": "10&U", "JD1": "12&U", "JD2": "12&U", "RSA": "8&U"}
# A swimmer joins here after an assessment.
ENTRY_POINTS = {"RSA", "TOPS 2", "REC AM", "REC PM", "AGD 2"}
ENTRY_RED = "#C0392B"

# Colour deepens with the tier, so the chart reads bottom to top.
TIER_SHADE = {"Entry": 0.34, "Development": 0.62, "Performance": 1.0}


def _mix(hexcol, t):
    """Blend a colour towards white. t=1 is the colour, t=0 is white."""
    r, g, b = (int(hexcol[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % tuple(round(255 - (255 - c) * t) for c in (r, g, b))


def _arrow_up(x, y1, y2, colour=INK, w=1.6):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 + 7}" stroke="{colour}" '
            f'stroke-width="{w}"/>'
            f'<polygon points="{x - 5},{y2 + 8} {x + 5},{y2 + 8} {x},{y2}" fill="{colour}"/>')


def _arrow_right(x1, x2, y, colour=INK, w=1.6):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 7}" y2="{y}" stroke="{colour}" '
            f'stroke-width="{w}"/>'
            f'<polygon points="{x2 - 8},{y - 5} {x2 - 8},{y + 5} {x2},{y} " fill="{colour}"/>')


def _head(px, py, dx, dy, colour, size=7, w=4.5):
    """An arrowhead at (px,py) pointing along (dx,dy)."""
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    bx, by = px - ux * size, py - uy * size
    return (f'<polygon points="{px:.1f},{py:.1f} {bx - uy * w:.1f},{by + ux * w:.1f} '
            f'{bx + uy * w:.1f},{by - ux * w:.1f}" fill="{colour}"/>')


def _transfer_line(x1, y1, x2, y2, colour=INK_SOFT):
    """Dashed, arrowheads both ends: a swimmer can move either way. Works on a
    diagonal, which is what a move between pathways at different stages needs."""
    L = math.hypot(x2 - x1, y2 - y1) or 1
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return (f'<line x1="{x1 + ux * 7:.1f}" y1="{y1 + uy * 7:.1f}" '
            f'x2="{x2 - ux * 7:.1f}" y2="{y2 - uy * 7:.1f}" stroke="{colour}" '
            f'stroke-width="1.3" stroke-dasharray="4 3"/>'
            + _head(x1, y1, -ux, -uy, colour) + _head(x2, y2, ux, uy, colour))


def _transfer(x1, x2, y):
    return _transfer_line(x1, y, x2, y)


def _sessions_label(code):
    """RSA is a Saturday class rather than a session count, so it does not take
    the "sessions a week" suffix."""
    v = SESSIONS[code]
    return "3 Saturday classes, 40 min each" if code == "RSA" else f"{v} sessions a week"


def _group_box(x, y, w, h, code, colour, shade):
    fill = _mix(colour, shade)
    dark = shade > 0.5
    fg = FOAM if dark else INK
    sub = "#CBDDE1" if dark else INK_SOFT
    age = AGES[code]
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>'
        + _txt(x + 12, y + 27, code, 19, fg, DISP, anchor="start")
        + f'<rect x="{x + w - 54}" y="{y + 11}" width="44" height="17" rx="8" '
          f'fill="{FOAM}" opacity="{0.9 if dark else 0.75}"/>'
        + _txt(x + w - 32, y + 24, age, 10, NAVY, DISP)
        + _txt(x + 12, y + 44, FULL[code], 10.5, sub, SANS, anchor="start")
        + _txt(x + 12, y + h - 11, _sessions_label(code), 11, fg, SANS,
               anchor="start", weight="bold")
    )


def pathway_diagram():
    LBL = 140                     # left column: tier label, then a lane for the
                                  # red entry arrows, which used to cross the text
    W, M, GAP = 980, 14, 12
    COLS = ["Recreation", "Regional", "Provincial", "National"]
    CW = (W - LBL - M - 3 * GAP) / 4
    BH, TG = 82, 34               # box height, gap between tiers
    PANEL_TOP = 34
    ROW_Y = {t: PANEL_TOP + 14 + i * (BH + TG) for i, t in enumerate(TIERS)}
    PANEL_BOT = ROW_Y["Entry"] + BH + 14
    JUN_Y = PANEL_BOT + 54
    RSA_Y = JUN_Y + BH + 46
    H = RSA_Y + BH + 16

    def cx(i):
        return LBL + i * (CW + GAP)

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
         f'<rect width="{W}" height="{H}" fill="{FOAM}"/>']

    # tier labels down the left
    for t in TIERS:
        p.append(_txt(LBL - 50, ROW_Y[t] + BH / 2 + 4, t.upper(), 11, INK_SOFT, DISP,
                      anchor="end"))

    # pathway panels and headings
    for i, pw in enumerate(COLS):
        x = cx(i)
        p.append(f'<rect x="{x}" y="{PANEL_TOP}" width="{CW}" height="{PANEL_BOT - PANEL_TOP}" '
                 f'rx="10" fill="{COLOUR[pw]}" opacity="0.07"/>')
        p.append(_txt(x + CW / 2, PANEL_TOP - 12, pw.upper(), 11.5, INK_SOFT, DISP))

    # group boxes, progression arrows, entry arrows
    for i, pw in enumerate(COLS):
        x = cx(i)
        col = COLOUR[pw]
        present = [t for t in TIERS if t in GRID[pw]]
        for t in present:
            code = GRID[pw][t]
            y = ROW_Y[t]
            p.append(_group_box(x + 10, y, CW - 20, BH, code, col, TIER_SHADE[t]))
            # progression up to the tier above, only where it is a real step up
            above = TIERS[TIERS.index(t) - 1] if TIERS.index(t) > 0 else None
            if above and above in GRID[pw] and pw != "Recreation":
                p.append(_arrow_up(x + CW / 2, y - 4, ROW_Y[above] + BH + 4))
            if code in ENTRY_POINTS:
                p.append(_arrow_right(x - 32, x + 6, y + BH - 18, ENTRY_RED, 2.2))

    # transfers between pathways, on the tiers where two neighbours both sit
    for t in TIERS:
        for i in range(len(COLS) - 1):
            a, b = COLS[i], COLS[i + 1]
            if t in GRID[a] and t in GRID[b]:
                p.append(_transfer(cx(i) + CW - 8, cx(i + 1) + 8, ROW_Y[t] + BH / 2))

    # Recreation into Regional. Two diagonals alongside the same-tier transfers:
    # REC PM up to AGD 1, and REC AM across to AGD 2. Set by the club.
    rec_r = cx(0) + CW - 10
    reg_l = cx(1) + 10
    for frm, to in [("Entry", "Development"), ("Development", "Entry")]:
        up = TIERS.index(to) < TIERS.index(frm)
        p.append(_transfer_line(rec_r, ROW_Y[frm] + BH / 2 + (-8 if up else 8),
                                reg_l, ROW_Y[to] + BH / 2 + (8 if up else -8)))

    # Junior, spanning, with left to right progression
    jg = ORDER["Junior"]
    jw = (W - LBL - M - (len(jg) - 1) * GAP) / len(jg)
    p.append(_txt(LBL - 50, JUN_Y + BH / 2 + 4, "JUNIOR", 11, INK_SOFT, DISP, anchor="end"))
    for j, g in enumerate(jg):
        x = LBL + j * (jw + GAP)
        p.append(_group_box(x, JUN_Y, jw, BH, g, COLOUR["Junior"], 0.30 + 0.14 * j))
        if j:
            p.append(_arrow_right(x - GAP - 2, x - 2, JUN_Y + BH / 2))
        if g in ENTRY_POINTS:
            p.append(_arrow_right(LBL - 38, LBL + 4, JUN_Y + BH / 2, ENTRY_RED, 2.2))
    # Junior feeds every pathway: one line up to a rail, then into each column
    rail = JUN_Y - 26
    p.append(f'<line x1="{LBL + jw / 2}" y1="{JUN_Y}" x2="{LBL + jw / 2}" y2="{rail}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    # The rail stops at Provincial: there is no route from Junior into National.
    p.append(f'<line x1="{LBL + jw / 2}" y1="{rail}" x2="{cx(2) + CW / 2}" y2="{rail}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    for i, pw in enumerate(COLS[:3]):
        lowest = [t for t in TIERS if t in GRID[pw]][-1]
        p.append(_arrow_up(cx(i) + CW / 2, rail, ROW_Y[lowest] + BH + 4))

    # PD2 into ND, the second of the two routes into National. PD1 into ND is the
    # dashed transfer already drawn on the Performance tier.
    pd2_y = ROW_Y["Development"] + BH / 2
    nd_x = cx(3) + 46
    p.append(f'<line x1="{cx(2) + CW - 10}" y1="{pd2_y}" x2="{nd_x}" y2="{pd2_y}" '
             f'stroke="{INK}" stroke-width="1.6"/>')
    p.append(_arrow_up(nd_x, pd2_y, ROW_Y["Performance"] + BH + 4))

    # Foundation at the base
    p.append(_txt(LBL - 50, RSA_Y + BH / 2 + 4, "FOUNDATION", 11, INK_SOFT, DISP,
                  anchor="end"))
    p.append(_group_box(LBL, RSA_Y, W - LBL - M, BH, "RSA", COLOUR["Foundation"], 0.34))
    p.append(_arrow_right(LBL - 38, LBL + 4, RSA_Y + BH / 2, ENTRY_RED, 2.2))
    p.append(_arrow_up(LBL + 60, RSA_Y - 4, JUN_Y + BH + 4))

    # how to read, in the space the National pathway leaves empty
    lx, ly = cx(3) + 18, ROW_Y["Entry"] + 2
    p.append(_txt(lx, ly, "HOW TO READ", 10.5, NAVY, DISP, anchor="start"))
    legend = [(_arrow_up(lx + 8, ly + 34, ly + 16),
               "progression to the next group"),
              (_transfer(lx, lx + 18, ly + 56), "transfer between pathways, either way"),
              (_arrow_right(lx, lx + 18, ly + 78, ENTRY_RED, 2.2),
               "where a new swimmer joins, after an assessment")]
    for art, text in legend:
        p.append(art)
    p.append(_txt(lx + 26, ly + 30, "progression to the next group", 9.5, INK_SOFT, SANS,
                  anchor="start"))
    p.append(_txt(lx + 26, ly + 60, "transfer between pathways, either way", 9.5, INK_SOFT,
                  SANS, anchor="start"))
    p.append(_txt(lx + 26, ly + 82, "where a new swimmer joins", 9.5, INK_SOFT, SANS,
                  anchor="start"))

    p.append('</svg>')
    return "".join(p)


def ladder_diagram():
    """Every group as a rung, ordered by hours a week. The point of the picture
    is that the gaps between rungs are small."""
    rungs = sorted(
        [(s, float(h)) for _pw, _n, s, _se, h in PROGRAMS if h.replace(".", "").isdigit()],
        key=lambda r: r[1])
    rungs.insert(0, ("RSA", 0.7))          # a Saturday class, shown as the first rung
    W, M = 700, 14
    ROW_H, GAP = 34, 6
    TOP = 44
    H = TOP + len(rungs) * (ROW_H + GAP) + 18
    maxh = max(h for _s, h in rungs)

    pw_of = {s: pw for pw, _n, s, _se, _h in PROGRAMS}
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
         f'<rect width="{W}" height="{H}" fill="{FOAM}"/>',
         _txt(M, 26, "THE LADDER, 2026-27", 14, NAVY, DISP, anchor="start"),
         _txt(W - M, 26, "hours a week", 11.5, INK_SOFT, SANS, anchor="end")]
    for i, (s, h) in enumerate(rungs):
        y = TOP + (len(rungs) - 1 - i) * (ROW_H + GAP)
        col = COLOUR[pw_of[s]]
        bar = (W - 2 * M - 210) * (h / maxh)
        p.append(f'<rect x="{M}" y="{y}" width="{W - 2 * M}" height="{ROW_H}" rx="6" '
                 f'fill="{col}" opacity="0.08"/>')
        p.append(f'<rect x="{M + 118}" y="{y + 7}" width="{max(bar, 3)}" height="{ROW_H - 14}" '
                 f'rx="4" fill="{col}"/>')
        p.append(_txt(M + 10, y + ROW_H / 2 + 4, s, 13, NAVY, DISP, anchor="start"))
        label = "40 min class" if s == "RSA" else f"{HOURS[s]} h"
        p.append(_txt(W - M - 10, y + ROW_H / 2 + 4, label, 12, INK_SOFT, SANS, anchor="end"))
        p.append(_txt(W - M - 62, y + ROW_H / 2 + 4, pw_of[s], 10.5, INK_SOFT, SANS, anchor="end"))
    p.append('</svg>')
    return "".join(p)


def as_img(svg, alt, border=True):
    b = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    edge = f'border:1px solid {LINE};' if border else ""
    return (f'<img src="data:image/svg+xml;base64,{b}" alt="{alt}" '
            f'style="width:100%;height:auto;display:block;border-radius:10px;{edge}'
            f'background:{FOAM};" />')


if __name__ == "__main__":
    for name, svg in [("pathways", pathway_diagram()), ("ladder", ladder_diagram())]:
        open(f"/tmp/{name}.svg", "w", encoding="utf-8").write(svg)
        print(f"  {name}.svg  {len(svg) // 1024} KB")
