"""
ROW Swim Club — reusable page-building helpers.

Upload this file alongside any new page request so future sessions have the
literal, current helper functions to import/paste from, instead of
re-deriving them from old build scripts. Keep this file in sync whenever a
helper changes — see ROW_Embedded_Page_Build_Guide.md for the full writeup
of conventions, sanitizer rules, and verification steps.

Last synced: all monospace set to font-weight:700 per the style guide (Courier New is thin and reads as faint at normal weight). Prior sync: framework components merged in (framed, switch_bar, table, numbered_row, layer_row, zone_tag, flag_badge, zone_row) so there's one UI module, not two. Prior sync: heroes no longer carry the ROW logo — the site header already shows it, and embedding it added ~75KB of base64 per page. Prior sync: doc_row() LINK badge switched from CYAN to FOAM. Prior sync: color baseline update — eyebrow tags and small circular/pill
badges use FOAM (#FFFFFF) instead of CYAN for text on a NAVY background.
"""

# ================= Colors =================
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
CAUTION = "#B8791A"   # amber warning badge (not brand RED, which is a zone colour)
OK_GREEN = "#2E8B4F"  # green confirmation badge

# Training zone swatches (How We Train page family)
Z_WHITE = "#FFFFFF"
Z_PINK = "#E39BAE"
Z_RED = "#D64545"
Z_PURPLE = "#7A5AA8"
Z_GREEN = "#3FA35C"

# ================= Fonts =================
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
            f'padding:{pad};margin:0 0 20px;">{inner_html}</div>')


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
    badge_fg = FOAM   # small pills on NAVY use FOAM per the current colour baseline
    return (
        f'<div style="padding:14px 18px;background:{bg};border-top:1px solid {LINE};">'
        f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;font-size:10px;'
        f'letter-spacing:0.04em;background:{badge_bg};color:{badge_fg};border-radius:4px;padding:2px 7px;'
        f'margin-right:10px;vertical-align:middle;">{badge_type}</span>'
        f'<a href="{href}" target="_blank" style="font-family:{BODY_FONT};font-size:15px;font-weight:700;'
        f'color:{NAVY};text-decoration:none;">{label}</a>'
        f'</div>'
    )


def circular_badge(text, size_px=54, font_size_px=19, bg=NAVY, color=FOAM):
    """Small circular badge (initials, step numbers, etc). Text on NAVY = FOAM per current baseline."""
    return (
        f'<div style="flex:none;width:{size_px}px;height:{size_px}px;border-radius:50%;background:{bg};'
        f'display:flex;align-items:center;justify-content:center;">'
        f'<span style="font-family:{DISPLAY_FONT};font-size:{font_size_px}px;color:{color};">{text}</span></div>'
    )


def eyebrow(text):
    """Small-caps label at the top of every hero. Text on NAVY = FOAM per current baseline."""
    return (f'<span style="font-family:{MONO_FONT};font-weight:700;font-size:13px;letter-spacing:0.14em;'
            f'text-transform:uppercase;color:{FOAM};margin-bottom:14px;display:block;">{text}</span>')


def hero(eyebrow_text, title, subtitle=""):
    """Text-only hero. Do NOT add the ROW logo: the site header already displays it."""
    subtitle_html = ""
    if subtitle:
        subtitle_html = (f'<p style="max-width:660px;margin:16px 0 0;font-size:16px;color:#CBDDE1;'
                          f'line-height:1.6;font-family:{BODY_FONT};">{subtitle}</p>')
    return f'''<div style="background:radial-gradient(1100px 500px at 15% -10%, #114C5E 0%, {NAVY} 55%, #062029 100%);
color:{FOAM};padding:44px 32px;border-radius:14px;">
{eyebrow(eyebrow_text)}
<h1 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.01em;color:{FOAM};
font-size:34px;line-height:1.1;font-weight:800;margin:0;">{title}</h1>
{subtitle_html}
</div>'''


def lanes_divider():
    lanes_colors = [RED, FOAM, TEAL, FOAM, CYAN, FOAM, RED, FOAM]
    lanes = "".join(f'<div style="flex:1;background:{c};"></div>' for c in lanes_colors)
    return f'<div style="height:8px;display:flex;border-radius:4px;overflow:hidden;margin:24px 0;">{lanes}</div>'


def wrap_page(*sections):
    """Assemble a full page from hero/section HTML strings, inside the standard 1000px SAND wrapper."""
    wrap_style = f'max-width:1000px;margin:0 auto;font-family:{BODY_FONT};background:{SAND};padding:24px;'
    return f'<div style="{wrap_style}">' + ''.join(sections) + '</div>'



# ============ Framework components (How We Train page family) ============

def framed(inner_html):
    """Bordered, shadowed container for a stack of rows."""
    return (f'<div style="border:1px solid {LINE};border-radius:10px;overflow:hidden;'
            f'background:{FOAM};box-shadow:0 6px 20px rgba(10,46,63,0.10);">{inner_html}</div>')


def switch_bar(text, label, href):
    """Thin cross-link bar under the hero (audience switch, or link to the parent page)."""
    return (f'<div style="background:{FOAM};border:1px solid {LINE};border-radius:10px;'
            f'padding:12px 20px;margin:0 0 20px;font-family:{BODY_FONT};font-size:13.5px;'
            f'color:{INK_SOFT};">{text} '
            f'<a href="{href}" style="color:{TEAL};font-weight:700;text-decoration:none;">{label}</a></div>')


def table(headers, rows):
    """NAVY header row, alternating body rows. First cell of each row is bolded."""
    th = (f'padding:10px 12px;text-align:left;font-family:{MONO_FONT};font-weight:700;'
          f'font-size:11px;letter-spacing:0.06em;text-transform:uppercase;color:{FOAM};'
          f'background:{NAVY};')
    head = "".join(f'<th style="{th}">{x}</th>' for x in headers)
    body = ""
    for i, r in enumerate(rows):
        bg = ROW_ALT if i % 2 == 1 else FOAM
        td = (f'padding:11px 12px;font-family:{BODY_FONT};font-size:13.2px;color:{INK};'
              f'border-top:1px solid {LINE};background:{bg};line-height:1.45;vertical-align:top;')
        cells = "".join(
            f'<td style="{td}{"font-weight:700;color:" + NAVY + ";" if j == 0 else ""}">{c}</td>'
            for j, c in enumerate(r))
        body += f'<tr>{cells}</tr>'
    return (f'<div style="border:1px solid {LINE};border-radius:10px;overflow:hidden;">'
            f'<table style="width:100%;border-collapse:collapse;"><tr>{head}</tr>{body}</table></div>')


def numbered_row(n, title, body_html, i=0):
    """Numbered rule / step row. Lighter than step_card; use inside framed()."""
    bg = ROW_ALT if i % 2 == 1 else FOAM
    return (
        f'<div style="display:flex;gap:16px;padding:15px 20px;background:{bg};'
        f'border-top:1px solid {LINE};">'
        f'<span style="flex:none;font-family:{MONO_FONT};font-weight:700;font-size:13px;'
        f'width:28px;height:28px;border-radius:50%;background:{TEAL};color:{FOAM};'
        f'display:flex;align-items:center;justify-content:center;">{n}</span>'
        f'<div><div style="font-family:{DISPLAY_FONT};text-transform:uppercase;font-size:13px;'
        f'letter-spacing:0.02em;color:{NAVY};margin:2px 0 5px;">{title}</div>'
        f'<div style="font-family:{BODY_FONT};font-size:13.8px;color:{INK};line-height:1.55;">{body_html}</div>'
        f'</div></div>'
    )


def layer_row(n, title, body_html, href=None, status="plain", i=0):
    """One row of the four-layer map.

    Only the current page is chipped ("On this page"). Other rows are deliberately
    unlabelled, so adding or publishing a layer doesn't force a rebuild of every
    sibling page. Build status lives on the coaching hub, in one place.
    """
    bg = ROW_ALT if i % 2 == 1 else FOAM
    chip = ''
    if status == "current":
        chip = (f'<span style="flex:none;font-family:{MONO_FONT};font-weight:700;font-size:9.5px;'
                f'letter-spacing:0.05em;text-transform:uppercase;background:{TEAL};color:{FOAM};'
                f'border-radius:4px;padding:3px 7px;margin-top:3px;">On this page</span>')
    title_html = title
    if href:
        title_html = f'<a href="{href}" style="color:{NAVY};text-decoration:none;">{title}</a>'
    return (
        f'<div style="display:flex;gap:16px;padding:14px 20px;background:{bg};'
        f'border-top:1px solid {LINE};align-items:flex-start;">'
        f'<span style="flex:none;font-family:{MONO_FONT};font-weight:700;font-size:12px;'
        f'width:26px;height:26px;border-radius:50%;background:{NAVY};color:{FOAM};'
        f'display:flex;align-items:center;justify-content:center;">{n}</span>'
        f'<div style="flex:1;">'
        f'<div style="font-family:{DISPLAY_FONT};text-transform:uppercase;font-size:12.5px;'
        f'letter-spacing:0.01em;color:{NAVY};margin:2px 0 4px;">{title_html}</div>'
        f'<div style="font-family:{BODY_FONT};font-size:13.5px;color:{INK};line-height:1.5;">{body_html}</div>'
        f'</div>{chip}</div>'
    )


def zone_tag(swatch, label):
    """Inline zone chip, e.g. zone_tag(Z_RED, "RED")."""
    fg = INK if swatch == Z_WHITE else FOAM
    border = f'border:1px solid {LINE};' if swatch == Z_WHITE else ''
    return (f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;font-size:9.5px;'
            f'letter-spacing:0.05em;background:{swatch};color:{fg};{border}border-radius:4px;'
            f'padding:2px 6px;margin:0 3px 3px 0;">{label}</span>')


def flag_badge(kind):
    """kind: 'ok' = safe at every age, 'care' = introduce gradually."""
    if kind == "ok":
        bg, mark, label = OK_GREEN, "&#10003;", "All ages"
    else:
        bg, mark, label = CAUTION, "&#9888;", "Use with care"
    return (f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;font-size:9.5px;'
            f'letter-spacing:0.05em;text-transform:uppercase;background:{bg};color:{FOAM};'
            f'border-radius:4px;padding:3px 7px;margin:8px 0 0;">'
            f'<span style="font-family:{BODY_FONT};font-size:11px;">{mark}</span>&nbsp;{label}</span>')


def zone_row(swatch, name, feel, purpose, typical, flag="ok", i=0):
    """One training-zone row: swatch, name, age flag, what it feels like, what it's for."""
    bg = ROW_ALT if i % 2 == 1 else FOAM
    border = f'1px solid {LINE}' if swatch == Z_WHITE else f'1px solid {swatch}'
    label = (f'font-family:{MONO_FONT};font-weight:700;font-size:10px;letter-spacing:0.06em;'
             f'text-transform:uppercase;color:{TEAL};margin:0 0 2px;')
    body = f'font-family:{BODY_FONT};font-size:13.5px;color:{INK};line-height:1.5;'
    return (
        f'<div style="display:flex;gap:16px;padding:16px 20px;background:{bg};'
        f'border-top:1px solid {LINE};">'
        f'<div style="flex:none;width:126px;">'
        f'<div style="width:26px;height:26px;border-radius:50%;background:{swatch};'
        f'border:{border};margin:0 0 8px;"></div>'
        f'<div style="font-family:{DISPLAY_FONT};text-transform:uppercase;font-size:12.5px;'
        f'letter-spacing:0.01em;color:{NAVY};line-height:1.2;">{name}</div>'
        f'{flag_badge(flag)}</div>'
        f'<div style="flex:1;"><div style="{label}">Feels like</div>'
        f'<div style="{body}margin:0 0 10px;">{feel}</div>'
        f'<div style="{label}">Used for</div><div style="{body}">{purpose}</div></div>'
        f'<div style="flex:none;width:180px;">'
        f'<div style="{label}">Typical set</div>'
        f'<div style="font-family:{MONO_FONT};font-weight:700;font-size:14px;color:{INK};'
        f'line-height:1.6;">{typical}</div>'
        f'</div></div>'
    )


if __name__ == "__main__":
    # Quick self-test: build a tiny sample page and run the sanitizer checks.
    import re

    sample = wrap_page(
        hero("ROW Swim Club", "Sample Page", "A quick self-test of the helper module."),
        lanes_divider(),
        card(h2("Section") + p("Body copy.")),
    )

    print("Sample page length:", len(sample))
    print("id= occurrences:", len(re.findall(r'\bid=', sample)))
    print("mailto count:", sample.count('mailto:'))
    print("script tag:", '<script' in sample)
    print("style tag present (inline is fine, <style> tag is not):", '<style' in sample)
