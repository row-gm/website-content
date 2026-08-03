"""Build all thirteen program pages from one template.

    python3 build_program_pages.py

One page per group. Recreation is the one exception, carrying both REC-AG
options on a single page at the club's direction.

Content and schedules live in layers_common.py. Change the layout here and
every program page follows.

Needs row_stylesheet.css in each page's custom CSS field.
"""

from row_page_helpers import (
    NAVY, TEAL, RED, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import (
    PROGRAM_PAGES, SCHEDULES, OPTIONS, GROUP_SIZE, URL_ASSESSMENT, URL_EQUIPMENT_LIST,
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


def build(slug, h1, pathway, key, coach, sessions, hours, blurb):
    size, how = GROUP_SIZE[key]
    page = wrap_page(
        hero(f"{pathway} pathway", h1, blurb.split(".")[0] + "."),
        lanes_divider(),
        chips(("Pathway", pathway), ("Sessions a week", sessions),
              ("Hours a week", hours), ("Group size", size),
              ("Lead coach", coach), ("Season start", "TBC")),
        card(h2("About this group") + body(blurb, margin="0")),

        '<div style="margin:24px 0 0;">' + card(
            h2("2026-27 schedule")
            + draft_banner()
            + schedule_block(key)
            + note("WLU = Wilfrid Laurier University &middot; Cameron Heights &middot; "
                   "Rec Complex = Waterloo Recreation Complex. A version using the 24 hour "
                   "clock is published alongside this one.")
            + note(f"<strong>Group size:</strong> {size}. {how} Every group keeps the same "
                   f"lanes for a whole session.")
            + callout("<strong>Dryland is not in the times above.</strong> Dryland schedules and "
                      "room access are being confirmed with Laurier, and will be published by "
                      "9 August.")) + '</div>',

        '<div style="margin:24px 0 0;">' + card(
            h2("How this group fits the plan")
            + body("Every ROW group is part of one development plan. It sets out what we are "
                   "developing, how training is built, and why a swimmer's progress does not "
                   "run in a straight line.")
            + data_table(["Read", "What it covers"], [
                [link(URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan"),
                 "How the whole plan fits together, and where this group sits in it."],
                [link(URL_HOW_WE_DEVELOP_SWIMMERS, "The ROW Way"),
                 "The four dimensions and twelve markers we develop in every swimmer, in their "
                 "own words."],
                [link(URL_THE_GROWTH_SPURT, "The Growth Spurt"),
                 "Why times can stall for a few months while a swimmer grows, and what to do "
                 "about it."],
                [link(URL_THE_BIRTHDAY_GAP, "The Birthday Gap"),
                 "Why results at twelve tell you less than they appear to."]])) + '</div>',

        f'<div style="margin:24px 0 0;">{cta()}</div>',

        '<div style="margin:24px 0 0;">' + card(
            h2("What every group gets")
            + data_table(["What", "Detail"], [
                ["A written season plan", "The phases, the technical priorities and the "
                                          "objectives for this group, shared with families."],
                ["Work that fits the swimmer", "Sprint, middle distance and distance swimmers "
                                               "are not doing the same set."],
                ["Technical work on a plan", "Starts, turns, underwaters and stroke mechanics "
                                             "taught on a named cycle, not when time allows."],
                ["Underwater video", "Used regularly, with the footage shown to the swimmer."],
                ["A GoSwim account", "For every swimmer outside the ROW Swim Academy, and every "
                                     "coach."],
                ["Dryland with a plan", "And someone who owns it."],
                ["Two progress conversations a year", "With the swimmer and the family, against "
                                                      "the objectives set for the phase."]])) + '</div>',

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
