# ROW Swim Club — Embedded Page Build Guide

Reference for building new sanitizer-safe HTML page fragments for rowswimming.ca. Copy the
Python block below into a new `build_<page>.py` script and start from there.

**Companion file:** `row_page_helpers.py` (same output folder) has these exact functions as a
literal, importable/pasteable module — kept in sync with this guide. Upload both files together
when starting a new page-build session, since the sandbox resets between sessions.

## Standing rules (never break these)

- **The CMS is SportsEngine Motion (formerly TeamUnify) and works from an allowlist.** Anything
  not on the list is stripped on save.
- **Allowed tags:** `a b br blockquote caption cite code col colgroup dd div dl dt em h1-h6 hr i
  iframe img li ol p pre q small strike strong span sub sup table tbody td tfoot th thead tr u ul`.
  `style` and `class` are allowed on every tag.
- **Stripped:** `<script>`, `<style>`, `<link>`, `<title>`, `<nav>`, `<section>`, `<footer>`.
- **CORRECTION:** `id=` and `mailto:` are **not** banned. The `a` tag permits `href title target
  id name` and the protocols `ftp http https mailto`. Avoiding them is house style, not a
  sanitizer requirement. Do not cite the sanitizer as the reason.
- **External links:** always `target="_blank"` (never `rel=`, it's stripped anyway).
- **Email addresses:** bold plain text only, e.g. `<strong>office@rowswimming.ca</strong>`.
  Never use `mailto:` links.
- **Images:** self-hosted only, as base64 data URIs. Resize to max 700px wide before encoding.
  Use `face_position.py` (OpenCV Haar cascade) for `object-position` on headshots.
- **No logo in page heroes.** The site header already shows the ROW logo. Repeating it inside an
  embedded fragment duplicates the branding and adds ~75KB of base64 per page. Heroes are text
  only: eyebrow, `<h1>`, subtitle.
- **Max content width:** 1000px, centred.
- **File naming:** `row_<section>_<h1 in lower snake case>_embed.html`. The eight section
  prefixes match the site navigation: `about_ coaches_ devplan_ meets_ news_ parents_
  programs_ swimmers_`. So The ROW Way, which sits under Our Development Plan, is
  `row_devplan_the_row_way_embed.html`. Pages that sit at the top level of the navigation
  take no prefix: the two home fragments and Sport Safety. The `<h1>` still supplies the
  rest of the name, so renaming a page renames its file. Build scripts are
  `build_<page>.py`. (Older files used an `fpp_` prefix; that is retired.)
- **Always verify after building:** check for `<script`, `id=`, `mailto:`, and any `<a>` missing
  `target="_blank"` before delivering. Run the verification snippet at the bottom of this guide.

## Colours

```python
NAVY = "#0A2E3F"
TEAL = "#136B77"
CYAN = "#3FBFB0"
RED = "#D64545"
SAND = "#F3EFE4"
FOAM = "#FFFFFF"
INK = "#152225"
INK_SOFT = "#4B5B60"
LINE = "#DAD3C2"
ROW_ALT = "#FAF8F2"   # alternating row background (used in lists/FAQs)
```

### Text-on-NAVY rule (baseline, confirmed)

Any text sitting directly on a `{NAVY}` background must be `{FOAM}` (`#FFFFFF`) — this includes:

- Hero `<h1>` and subtitle text (already the default, unchanged)
- Table header cells (`<th>` on `{NAVY}`, already the default, unchanged)
- **Eyebrow tags** — the small-caps label at the top of every hero (e.g. "ROW Swim Club",
  "Age Group Development Programs") — previously `{CYAN}`, **now `{FOAM}`**
- **Small circular/pill badges** — board/coach initials circles, step-number circles, the
  program tier tag, and the pool code tag — previously `{CYAN}`, **now `{FOAM}`**

`{CYAN}` was too low-contrast for small text at these sizes. It's still fine to use `{CYAN}` for
larger decorative elements, borders, or accents that aren't primarily text-legibility-dependent —
just not for eyebrow tags or small circular badges going forward.

**Not affected by this change** (intentional exceptions, confirmed earlier):

- Footer body copy on `{NAVY}` stays `#B9CCD0` (deliberately muted/quieter than body text)
- Links and body text in `{CYAN}` that sit on light/`{FOAM}` backgrounds (not on NAVY) are unrelated
  to this rule and unchanged

## Typography rule: bold all monospace

`'Courier New'` is a thin typeface. At normal weight it reads as faint even in near-black, and
gets reported as a contrast failure when measured contrast is fine. **Every time, number, formula,
mono eyebrow and pill badge must be `font-weight:700`,** and body-level mono text should be 14px
or larger. Greyed placeholder text needs `#6E6A5E` or darker to pass WCAG AA.

## Fonts

```python
DISPLAY_FONT = "'Arial Black', Arial, Helvetica, sans-serif"   # headers, uppercase, tracked
BODY_FONT = "Arial, Helvetica, sans-serif"                     # body copy
MONO_FONT = "'Courier New', Courier, monospace"                 # numbers, badges, eyebrows
BASE = "https://www.rowswimming.ca"                             # site root for relative links
```

## Core helper functions

Paste this block at the top of any new build script. It covers every reusable UI piece used
across the site (paragraphs, headers, cards, FAQs, callouts, numbered steps, document/link rows).

```python
NAVY = "#0A2E3F"
TEAL = "#136B77"
CYAN = "#3FBFB0"
RED = "#D64545"
SAND = "#F3EFE4"
FOAM = "#FFFFFF"
INK = "#152225"
INK_SOFT = "#4B5B60"
LINE = "#DAD3C2"

DISPLAY_FONT = "'Arial Black', Arial, Helvetica, sans-serif"
BODY_FONT = "Arial, Helvetica, sans-serif"
MONO_FONT = "'Courier New', Courier, monospace"
BASE = "https://www.rowswimming.ca"

def p(text, size="16px", color=INK, margin="0 0 16px"):
    return f'<p style="font-family:{BODY_FONT};font-size:{size};color:{color};line-height:1.65;margin:{margin};">{text}</p>'

def h2(text):
    return (f'<h2 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.02em;'
            f'color:{NAVY};margin:0 0 8px;font-size:24px;">{text}</h2>')

def faq_item(question, answer_html, i=0):
    bg = "#FAF8F2" if i % 2 == 1 else FOAM
    return (
        f'<div style="padding:18px 22px;background:{bg};border-top:1px solid {LINE};">'
        f'<div style="font-family:{BODY_FONT};font-size:15.5px;font-weight:700;color:{NAVY};margin-bottom:6px;">{question}</div>'
        f'<div style="font-family:{BODY_FONT};font-size:14.5px;color:{INK};line-height:1.65;">{answer_html}</div>'
        f'</div>'
    )

def faq_list(faq_html):
    return (f'<div style="border:1px solid {LINE};border-radius:10px;overflow:hidden;'
            f'box-shadow:0 6px 20px rgba(10,46,63,0.10);background:{FOAM};">{faq_html}</div>')

def card(inner_html, pad="24px 26px"):
    return (f'<div style="background:{FOAM};border:1px solid {LINE};border-radius:12px;'
            f'padding:{pad};">{inner_html}</div>')

def callout(body_html, warn=False):
    border = RED if warn else CYAN
    bg = "#FBEEEE" if warn else "#EFFAF8"
    return (f'<div style="border-left:4px solid {border};background:{bg};'
            f'border-radius:0 10px 10px 0;padding:16px 20px;margin:20px 0 0;font-size:14.5px;'
            f'color:{INK};font-family:{BODY_FONT};line-height:1.6;">{body_html}</div>')

def step_card(number, title, body_html):
    return (
        f'<div style="display:flex;gap:16px;padding:20px 0;border-top:1px solid {LINE};">'
        f'<span style="flex:none;font-family:{MONO_FONT};font-weight:700;font-size:15px;'
        f'width:34px;height:34px;border-radius:50%;background:{TEAL};color:{FOAM};'
        f'display:flex;align-items:center;justify-content:center;">{number}</span>'
        f'<div>'
        f'<h3 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.01em;'
        f'color:{NAVY};font-size:16px;margin:0 0 6px;">{title}</h3>'
        f'<div style="font-family:{BODY_FONT};font-size:14.5px;color:{INK};line-height:1.6;">{body_html}</div>'
        f'</div></div>'
    )

def doc_row(label, href, i=0, badge_type="PDF"):
    bg = "#FAF8F2" if i % 2 == 1 else FOAM
    badge_bg = NAVY if badge_type == "LINK" else RED
    badge_fg = CYAN if badge_type == "LINK" else FOAM
    return (
        f'<div style="padding:14px 18px;background:{bg};border-top:1px solid {LINE};">'
        f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;font-size:10px;'
        f'letter-spacing:0.04em;background:{badge_bg};color:{badge_fg};border-radius:4px;padding:2px 7px;'
        f'margin-right:10px;vertical-align:middle;">{badge_type}</span>'
        f'<a href="{href}" target="_blank" style="font-family:{BODY_FONT};font-size:15px;font-weight:700;'
        f'color:{NAVY};text-decoration:none;">{label}</a>'
        f'</div>'
    )
```

## Hero block pattern

Every page opens with a dark radial-gradient hero. Swap the eyebrow text, `<h1>`, and subtitle
paragraph for each new page; keep the gradient and structure identical for visual consistency.

No logo image — the site header supplies it.

```python
hero = f'''<div style="background:radial-gradient(1100px 500px at 15% -10%, #114C5E 0%, {NAVY} 55%, #062029 100%);
color:{FOAM};padding:44px 32px;border-radius:14px;">
<span style="font-family:{MONO_FONT};font-size:13px;letter-spacing:0.14em;text-transform:uppercase;
color:{FOAM};margin-bottom:14px;display:block;">ROW Swim Club</span>
<h1 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.01em;color:{FOAM};
font-size:34px;line-height:1.1;font-weight:800;margin:0;">Page Title Here</h1>
<p style="max-width:660px;margin:16px 0 0;font-size:16px;color:#CBDDE1;line-height:1.6;font-family:{BODY_FONT};">
One or two sentences summarizing what this page covers.</p>
</div>'''

# Optional lane-stripe divider (used under hero or between major sections)
lanes_colors = [RED, FOAM, TEAL, FOAM, CYAN, FOAM, RED, FOAM]
lanes = "".join(f'<div style="flex:1;background:{c};"></div>' for c in lanes_colors)
lanes_div = f'<div style="height:8px;display:flex;border-radius:4px;overflow:hidden;margin:24px 0;">{lanes}</div>'
```

## Page assembly pattern

```python
wrap_style = f'max-width:1000px;margin:0 auto;font-family:{BODY_FONT};background:{SAND};padding:24px;'
full = (
    f'<div style="{wrap_style}">'
    f'{hero}'
    f'{lanes_div}'
    # ... your card()/faq_list()/step_card() sections here ...
    f'</div>'
)

with open('/mnt/user-data/outputs/row_<page>_embed.html', 'w', encoding='utf-8') as f:
    f.write(full)
```

## The shared stylesheet

Every page uses `build/row_stylesheet.css`, pasted into the page's **custom CSS** field.
The page HTML goes in the **content editor** via the Source button. Two fields, not one.
A page pasted into only the content editor renders unstyled.

**Never put a comment in the stylesheet.** The CMS custom CSS field silently rejects the
whole file when it contains one, and the page renders as plain text with no error. This
cost an afternoon on 15 August 2026. Explanations belong in the decisions record.

**Block spacing lives in the stylesheet**, under `.row-wrap > *`. Do not reintroduce
`<div style="margin:24px 0 0;">` spacer divs from older build scripts; they would double
the gap.

**Structure and typography in the stylesheet. Colour that varies per row stays inline.**
Zone colours, meet tag colours and layer states all come from data in `layers_common.py`.
A clean-up that purges every inline style will break the zone tables.

The stylesheet is scoped: every rule begins `.row-wrap`. A page without a
`<div class="row-wrap">` wrapper gets no styling at all.

## Never edit in the CMS visual editor

The visual editor clones the class of whatever block the cursor is in. Pressing Enter
inside a `<div class="row-stage-head">` produces another one. Our Olympians and
Paralympians accumulated 34 heading blocks where the build makes 16, seventeen of them
empty, plus a stray heading around "1980 Moscow". Senior Development picked up three cells
wrapped in hardcoded `font-family: Arial, Helvetica; background-color: rgb(255,255,255)`.

Source button only. If a page has drifted, rebuild it rather than patching what is live.

## The three checkers

Run all three before pasting anything:

```
python3 row_vocabulary.py  pages/row_<name>_embed.html
python3 row_style_check.py pages/row_<name>_embed.html
python3 row_css_check.py   row_stylesheet.css pages/row_<name>_embed.html
```

- `row_vocabulary.py` catches retired words: stream, zone colours, taper, quality,
  age bands trailing a group name, and variants of the goal statement.
- `row_style_check.py` checks the sanitizer allowlist.
- `row_css_check.py` fails when a page uses a class the stylesheet does not define. Add
  `--all` with the whole page set to also list classes defined and never used.

Every page pulled from the CMS on 15 August turned up classes the stylesheet had never
defined, meaning those parts had never rendered correctly. Expect more.

## URLs

Every URL lives in `layers_common.py` as a constant. Never hard-code one in a build
script. The same goes for the goal statement, group names, pathways, zones and phases:
if it is a shared fact, it has a constant.


## Post-build verification snippet

Run this after every build to catch sanitizer violations before delivering:

```python
import re
content = open('/mnt/user-data/outputs/row_<page>_embed.html', encoding='utf-8').read()
print('id= occurrences:', len(re.findall(r'\bid=', content)))
print('mailto count:', content.count('mailto:'))
print('script tag:', '<script' in content)
print('style tag:', '<style' in content)
print('nav/section/footer:', any(t in content for t in ('<nav', '<section', '<footer', '<title')))
links_no_target = re.findall(r'<a(?![^>]*target="_blank")[^>]*href="https?://[^"]*"[^>]*>', content)
print('external links missing target=_blank:', len(links_no_target))
print('logo/base64 in page (should be 0):', content.count('base64'))
```

Note: if a page embeds a base64 data URI (e.g. an inline PDF), the verification script's raw
output can be enormous — grep or filter for `href="https?://` links specifically rather than
scanning the whole `links_no_target`-style list, to avoid flooding the terminal.

## FAQ category pattern (for handbook-style pages)

When a page has more than ~6 FAQ items, group them into labelled categories instead of one long
list, so it scans easily:

```python
category_head = (
    f'<h3 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.01em;'
    f'color:{NAVY};font-size:18px;margin:28px 0 10px;">Category Name</h3>'
)
category_faq = faq_list(
    faq_item("Question one?", "Answer one.", i=0)
    + faq_item("Question two?", "Answer two.", i=1)
)
```

Keep index `i` continuous within a category (alternates row background) but it can restart at 0
for each new category — it only controls striping, not numbering.

## Page inventory

Do not keep an inventory here; it goes stale. `PAGE_STATUS.md` in the repo root is the
live record of all 61 pages, which have been verified against the site and which have
not. `PULL_LIST.md` is the working list of those still to check.
