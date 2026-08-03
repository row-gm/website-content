"""ROW style check — catches a page drifting away from the template.

The CMS strips stylesheets, so every size and colour is written onto every
element. That is why 56 pages drifted apart: there was no one place to change a
heading size. row_page_helpers.py is the substitute for a stylesheet, and this
file is the check that nothing has slipped past it.

    python3 row_style_check.py /mnt/user-data/outputs/row_<page>_embed.html

Every piece of text on a ROW page must be one of the roles below. Anything else
is drift, and gets reported with the page it was found on.
"""

import re
import sys
from collections import Counter

# (family, size, weight, colour) -> what it is for
# Family: DISPLAY = Arial Black, BODY = Arial, MONO = Courier New
ROLES = {
    ("DISPLAY", "clamp", "800", "#FFFFFF"): "page title",
    ("DISPLAY", 24.0, "400", "#0A2E3F"): "section heading",
    ("DISPLAY", 18.0, "400", "#0A2E3F"): "sub heading",
    ("DISPLAY", 16.0, "400", "#0A2E3F"): "step card title",
    ("DISPLAY", 15.0, "400", "#0A2E3F"): "phase name",

    ("BODY", 16.0, "400", "#CBDDE1"): "page title subtitle",
    ("BODY", 14.5, "400", "#152225"): "body prose, callout",
    ("BODY", 14.0, "400", "#4B5B60"): "muted intro or closing line",
    ("BODY", 14.0, "400", "#152225"): "numbered row",
    ("BODY", 13.5, "700", "#0A2E3F"): "table, first cell",
    ("BODY", 13.5, "400", "#152225"): "table cell",
    ("BODY", 13.0, "400", "#136B77"): "phase tagline",

    ("MONO", 15.0, "700", "#FFFFFF"): "step circle",
    ("MONO", 15.0, "700", "#0A2E3F"): "set line, data field",
    ("MONO", 13.0, "700", "#FFFFFF"): "eyebrow, numbered circle",
    ("MONO", 12.5, "700", "#4B5B60"): "phase length",
    ("MONO", 12.0, "700", "#4B5B60"): "phase meta",
    ("MONO", 11.0, "700", "#FFFFFF"): "table heading",
    ("MONO", 10.5, "700", "#4B5B60"): "field label",
    ("MONO", 10.5, "700", "#152225"): "badge on a light colour",
    ("MONO", 10.5, "700", "#FFFFFF"): "badge on a dark colour",
    ("MONO", 10.0, "700", "#FFFFFF"): "small badge",
}

PALETTE = {
    "#0A2E3F": "navy", "#136B77": "teal", "#3FBFB0": "cyan", "#D64545": "red",
    "#F3EFE4": "sand", "#FFFFFF": "white", "#152225": "ink", "#4B5B60": "soft ink",
    "#DAD3C2": "line", "#FAF8F2": "row tint", "#CBDDE1": "subtitle", "#EFFAF8": "callout tint",
    "#FBEEEE": "warning tint", "#B9CCD0": "footer text", "#114C5E": "hero mid",
    "#062029": "hero deep", "#2E8B4F": "all ages flag", "#B8791A": "use with care flag",
    "#E39BAE": "zone 2", "#7A5AA8": "zone 4", "#3FA35C": "zone 5",
}


def roles_used(markup):
    """Every (family, size, weight, colour) that carries text on the page."""
    found = Counter()
    for style in re.findall(r'style="([^"]*)"', markup):
        size = re.search(r"font-size:(clamp\([^)]*\)|[\d.]+px)", style)
        if not size:
            continue
        fam = re.search(r"font-family:([^;]+)", style)
        fam = ("MONO" if fam and "Courier" in fam.group(1)
               else "DISPLAY" if fam and "Arial Black" in fam.group(1) else "BODY")
        s = size.group(1)
        s = "clamp" if s.startswith("clamp") else float(s[:-2])
        wt = re.search(r"font-weight:(\d+)", style)
        col = re.search(r"(?<!background-)(?<!border-)color:(#[0-9A-Fa-f]{6})", style)
        found[(fam, s, wt.group(1) if wt else "400",
               col.group(1).upper() if col else "-")] += 1
    return found


def check(markup):
    """Return (off_template, off_palette)."""
    off_template = {k: n for k, n in roles_used(markup).items() if k not in ROLES}
    off_palette = Counter()
    for hexcode in re.findall(r"#[0-9A-Fa-f]{6}", markup):
        if hexcode.upper() not in PALETTE:
            off_palette[hexcode.upper()] += 1
    return off_template, off_palette


def report(path):
    markup = open(path, encoding="utf-8").read()
    tmpl, pal = check(markup)
    name = path.split("/")[-1]
    if not tmpl and not pal:
        print(f"\n{name}\n  on template")
        return 0
    print(f"\n{name}")
    if tmpl:
        print("  text that is not one of the agreed roles")
        for (fam, size, wt, col), n in sorted(tmpl.items(), key=lambda x: -x[1]):
            near = [v for k, v in ROLES.items() if k[0] == fam and k[3] == col]
            hint = f"   closest role: {near[0]}" if near else ""
            print(f"    {fam:<8}{str(size):>7}px  weight {wt:<4}{col:<9} x{n}{hint}")
    if pal:
        print("  colours that are not in the palette")
        for c, n in sorted(pal.items(), key=lambda x: -x[1]):
            print(f"    {c}  x{n}")
    return len(tmpl) + len(pal)


if __name__ == "__main__":
    paths = sys.argv[1:]
    if not paths:
        print(__doc__)
        sys.exit(0)
    sys.exit(min(sum(report(p) for p in paths), 1))
