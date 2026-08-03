"""Build all thirteen program pages from one template.

    python3 build_program_pages.py

One page per group. Recreation is the one exception, carrying both REC
options on a single page at the club's direction.

Content and schedules live in layers_common.py. Change the layout here and
every program page follows.

Needs row_stylesheet.css in each page's custom CSS field.

WHAT YOUR SWIMMER GETS is a placeholder for now. The heading stays on the page
with a short "being updated" note, so the text can be typed straight into the
CMS when the club is ready.

  IMPORTANT. Anything typed into the CMS is lost the next time that page is
  built. If the section has been written in by hand and the page then needs
  rebuilding, copy the text into GETS in layers_common.py first and set
  SHOW_GETS to True. The per-pathway lists are already drafted there.
"""

# False keeps the placeholder note. True renders the drafted lists from
# layers_common.py. One line, and all thirteen pages change together.
SHOW_GETS = False

from row_page_helpers import (
    NAVY, TEAL, RED, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import (
    PROGRAMS_TREE as URL_PROGRAMS,
    PROGRAM_PAGES, SCHEDULES, OPTIONS, GROUP_SIZE, GETS, GETS_FOR, CHIP_OVERRIDE,
    RSA_SESSIONS,
    URL_ASSESSMENT, URL_EQUIPMENT_LIST,
    URL_OUR_DEVELOPMENT_PLAN, URL_HOW_WE_DEVELOP_SWIMMERS,
    URL_THE_GROWTH_SPURT, URL_THE_BIRTHDAY_GAP,
)


def draft_banner():
    """Unmistakable, at the club's instruction. Above every schedule. Remove it
    here once the schedule is signed off and all thirteen pages lose it."""
    return ('<div class="row-draft"><b>Draft &mdash; not yet final</b>'
            '<span>These times are still being confirmed and may change before '
            'the season starts.</span></div>')


def sched_table(rows):
    return data_table(["Day", "Time", "Pool", "Lanes"], [list(r) for r in rows])


def schedule_block(key):
    if key in OPTIONS:
        out = ""
        for label, rows in OPTIONS[key]:
            out += f'<div class="row-opt">{label}</div>' + sched_table(rows)
        return out
    return sched_table(SCHEDULES[key])


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def cta():
    return (f'<a href="{URL_ASSESSMENT}" target="_blank" class="row-cta">'
            f'<b>Not sure where your swimmer fits?</b>'
            f'<span>Book an assessment and we will place them in the right group '
            f'from day one.</span><em>Book an assessment &rarr;</em></a>')


def chips(*pairs):
    inner = "".join(f'<div class="row-chip"><b>{a}</b><span>{v}</span></div>' for a, v in pairs)
    return f'<div class="row-chips">{inner}</div>'


def _gets_placeholder():
    """The section header stays, with a short note in place of the list. Replace
    this block in the CMS Source view to write the section by hand."""
    return callout("<strong>Updating.</strong>")


def _chips(key, pathway, sessions, hours, size, coach):
    """The quick facts row. RSA overrides it: at the Academy a session is a ten
    week registration block, so "sessions a week" would mean the wrong thing."""
    default = {"Pathway": pathway, "Group size": size, "Lead coach": coach}
    if key in CHIP_OVERRIDE:
        return [(lbl, val if val is not None else default[lbl])
                for lbl, val in CHIP_OVERRIDE[key]]
    return [("Pathway", pathway), ("Sessions a week", sessions), ("Hours a week", hours),
            ("Group size", size), ("Lead coach", coach), ("Season start", "TBC")]


def build(slug, h1, pathway, key, coach, sessions, hours, blurb):
    size, how = GROUP_SIZE[key]
    page = wrap_page(
        hero(f"{pathway} pathway", h1, blurb.split(".")[0] + "."),
        lanes_divider(),
        chips(*_chips(key, pathway, sessions, hours, size, coach)),
        card(h2("About this group") + body(blurb, margin="0")),

        '<div style="margin:24px 0 0;">' + card(
            h2("2026-27 schedule")
            + ("" if key == "RSA" else draft_banner())
            + schedule_block(key)
            + ("" if key == "RSA" else
               note("WLU = Wilfrid Laurier University &middot; Cameron Heights &middot; "
                    "Rec Complex = Waterloo Recreation Complex. A version using the 24 hour "
                    "clock is published alongside this one."))
            + note(f"<strong>Group size:</strong> {how}" if key == "RSA" else
                   f"<strong>Group size:</strong> {size}. {how} A group keeps the same lanes "
                   f"through a practice.")
            + (note("Registration runs in ten week sessions: "
                    + ", ".join(RSA_SESSIONS).lower() + ". Dates are confirmed before each one "
                    "opens.") if key == "RSA" else "")
            + ("" if key == "RSA" else
               callout("<strong>Dryland is not in the times above.</strong> Dryland schedules "
                       "and room access are being confirmed with Laurier, and will be published "
                       "by 9 August."))) + '</div>',

        # Two links, both to the top of a section. Listing the individual pages
        # inside a section meant every new page forced an edit on thirteen
        # others, and the drop-down already shows them. Same reasoning that took
        # the layer map off the coach pages.
        '<div style="margin:24px 0 0;">' + card(
            h2("How this group fits the plan")
            + body("ROW groups share one development plan. It sets out what we are developing, "
                   "how training is built, and why a swimmer&rsquo;s progress does not run in a "
                   "straight line.")
            + body("How the programs connect as swimmers develop is on "
                   + link(URL_PROGRAMS, "Programs Overview") + ". What we are developing, and "
                   "why, is in " + link(URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan") + ".",
                   margin="0")) + '</div>',

        f'<div style="margin:24px 0 0;">{cta()}</div>',

        '<div style="margin:24px 0 0;">' + card(
            h2("What to Expect")
            + (data_table(["What", "Detail"], [[w, d] for w, d in GETS[GETS_FOR[key]]])
               if SHOW_GETS else _gets_placeholder())) + '</div>',

        '<div style="margin:24px 0 0;">' + card(
            h2("Equipment")
            + body("See the " + link(URL_EQUIPMENT_LIST, "ROW Equipment List")
                   + " for this group&rsquo;s equipment standards.", margin="0")) + '</div>',
    )
    stem = slug.replace("-", "_")
    stem = stem[4:] if stem.startswith("row_") else stem
    out = f"/mnt/user-data/outputs/row_{stem}_embed.html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    return out, len(page)


if __name__ == "__main__":
    total = 0
    for row in PROGRAM_PAGES:
        out, n = build(*row)
        total += n
        print(f"  {out.split('/')[-1]:<46}{n // 1024:>4} KB")
    print(f"\n{len(PROGRAM_PAGES)} pages, {total // 1024} KB total")
