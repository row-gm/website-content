"""Build the Programs Overview page fragment (public, family-facing).

Rebuilt August 2026 from the 2026-27 Program Structure Executive Summary.
Replaces build_programs_overview.py / fpp_programs_overview_embed.html.

Public page. No coach-only wording: the audience guard in row_vocabulary.py is
run against it as a family page.

No links. The program pages are being rebuilt, so the page names the groups
without pointing anywhere. The new slugs are already in layers_common.py as
PROGRAM_SLUGS: add the links back by restoring group_link() when the pages go
live.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    data_table, lede,
)

from layers_common import PROGRAMS, PATHWAYS, pathway, PATHWAY_PEAKS
from row_diagrams import pathway_diagram, as_img


PATHWAY_INTRO = {
    "Foundation": "Where a swimmer starts. Saturday mornings, forty minutes, and no racing. "
                  "Classes run the beginner, intermediate and advanced levels together.",
    "Junior": "The first taste of training as a group. Volume and coaching go up step by step "
              "through TOPS and Junior Development. Swimmers race, but nothing is built around "
              "a championship.",
    "Recreation": "For swimmers up to 18 who want to keep swimming without the "
                  "competitive commitment. Technique, fitness, and a group to belong to. The "
                  "only difference between the two groups is when they train.",
    "Regional": "The first competitive pathway. Three levels that build on each other, with "
                "age recommendations rather than hard cut-offs.",
    "Provincial": "For swimmers racing at the provincial level. More sessions, more mornings, "
                  "and a season built around peak meets.",
    "National": "The top of the pathway. Eight sessions a week, including 50 metre training and "
                "double days, aimed at Trials and Nationals.",
}

PATHWAY_COLOUR = {
    "Foundation": TEAL, "Junior": NAVY, "Recreation": TEAL,
    "Regional": RED, "Provincial": NAVY, "National": RED,
}


page_hero = hero(
    "ROW Swim Club",
    "Programs Overview",
    "The groups we offer for the 2026-27 season, from a first Saturday class to eight sessions "
    "a week. Whether your swimmer is just starting or chasing a national standard, there is a "
    "place for them at ROW.")


intro = card(
    h2("How our programs fit together")
    + body("Our groups are organized into six <strong>pathways</strong>. A pathway describes "
           "what a swimmer is training for. Within a pathway, each group adds a little more "
           "time in the water and a little more coaching than the one before it.")
    + body("We are not only developing faster swimmers. We are helping your child build "
           "confidence, discipline and friendships that last long after the season ends.")
    + body("The groups below are a starting point. When we place a swimmer we also look at "
           "maturity, attitude, and where they are in their own development.", margin="0")
    + as_img(pathway_diagram(), "The six ROW pathways: Foundation at the base, Junior above "
                                "it, and Recreation, Regional, Provincial and National rising "
                                "from there")
    + note("Read it from the bottom up. Swimmers start at Foundation, move through "
           "Junior, then into Recreation, Regional or Provincial. National is reached from PD2 "
           "or PD1 and from nowhere else. The dotted arrows are moves between pathways, and they run "
           "both ways: Recreation is a different choice rather than a lower one. The red arrows "
           "mark where a swimmer joins after an assessment.")
    + callout(
        "<strong>An age band is a stage, not a birthday.</strong> Where a swimmer sits close to "
        "the top of a band we will be flexible, so a swimmer who wants to compete is in the "
        "group that suits them rather than the one their birth year puts them in.")
)


def pathway_head(name):
    bar = PATHWAY_COLOUR[name]
    return (
        f'<div style="border-left:5px solid {bar};padding:0 0 0 16px;margin:0 0 14px;">'
        f'<div style="font-family:{MONO_FONT};font-weight:700;font-size:10.5px;'
        f'letter-spacing:0.12em;text-transform:uppercase;color:{INK_SOFT};margin:0 0 4px;">'
        f'Pathway</div>'
        f'<div style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.02em;'
        f'color:{NAVY};font-size:24px;line-height:1.15;">{name}</div></div>'
    )


def pathway_card(name):
    # No links. The program pages are not ready, and the old page pointed at
    # slugs that are being replaced. program_url() in layers_common.py holds the
    # new ones for when they are.
    rows = [[g, short, sess, hrs] for _pw, g, short, sess, hrs in pathway(name)]
    return card(
        pathway_head(name)
        + lede(PATHWAY_INTRO[name])
        + data_table(["Group", "Short name", "Sessions a week", "Hours a week"], rows)
    )


peaks_section = card(
    h2("What each pathway is working towards")
    + lede("Only the last three pathways build a season around a peak meet. The others "
           "race often and race through, and that is by design rather than something missing.")
    + data_table(["Pathway", "Groups", "Peak meet"],
                 [[a, b, c] for a, b, c in PATHWAY_PEAKS])
)


WHATS_NEW = [
    ("Age Group Development is now two groups",
     "One group of about seventy becomes AGD 2 at four sessions a week and AGD 1 at five. "
     "Each has its own lead coach."),
    ("A Recreation pathway has been added",
     "REC PM trains three evenings a week at Cameron Heights. REC AM has five "
     "available mornings at the Rec Complex, and swimmers attend the ones that suit them."),
    ("Junior Development is offered as JD1 and JD2",
     "JD1 trains four times a week and JD2 three. They train alongside each other on Monday, "
     "Thursday and Saturday, with three lanes each."),
    ("TOPS has more schedule options",
     "TOPS 2 now has three schedule options and TOPS 1 has two. Options run three lanes, five "
     "swimmers to a lane, with a coach per lane."),
    ("The ROW Swim Academy moves to Saturday only",
     "Three class options at Cameron Heights, each forty minutes: 7:45, 8:30 and 9:15."),
    ("Session times have been rebuilt",
     "Rather than adjust the old timetable we rebuilt the schedule around the water, the times "
     "and the coaching we have. The group schedules are published in full."),
]

whats_new = card(
    h2("What is new for 2026-27")
    + lede("The groups keep their names, and the pathways are unchanged. These are the changes "
           "families will notice.")
    + data_table(["Change", "What it means"], [[a, b] for a, b in WHATS_NEW])
    + note("Fees are published with the registration information in mid-August. Dryland "
           "schedules and the meet schedule are published as soon as they are confirmed.")
)


promise = card(
    h2("What your swimmer gets")
    + lede("The commitments below hold across the competitive groups. Each group page sets out "
           "what that looks like at that stage, and the Academy has its own list suited to a "
           "Saturday class.")
    + data_table(
        ["What", "Detail"],
        [["A written season plan", "The phases, the technical priorities and the objectives for "
                                   "the group, shared with families."],
         ["Work set for your swimmer", "Work is set for a swimmer&rsquo;s events and their stage, "
                                       "inside the same set."],
         ["Skills on a schedule", "Starts, turns, underwaters and stroke mechanics taught on a "
                                  "published cycle, in a set order."],
         ["Video they can see themselves in", "Underwater footage, shown to the swimmer."],
         ["A GoSwim account", "For swimmers outside the ROW Swim Academy, and for coaches. "
                              "Thousands of videos of age group and elite swimmers, so a skill "
                              "can be seen before it is tried."],
         ["Dryland with a plan and an owner", "And someone accountable for it, in the groups that "
                                             "do it."],
         ["Club testing", "The same tests in the same conditions, so progress is measured the "
                          "same way across the club."],
         ["Race plans and reviews", "A plan going in and a review afterwards, in the competitive "
                                    "groups."],
         ["Two progress conversations a year", "With the swimmer and the family, about the "
                                              "objectives set for the phase."]])
)


closing = callout(
    "<strong>Not sure where your swimmer fits?</strong> Book a new swimmer assessment, or ask a coach "
    "before or after practice. Written criteria for moving between groups, and between pathways, are "
    "published at the start of the season.")


full = wrap_page(
    page_hero,
    lanes_divider(),
    intro,
    *[f'<div style="margin:24px 0 0;">{pathway_card(pw)}</div>' for pw in PATHWAYS],
    f'<div style="margin:24px 0 0;">{peaks_section}</div>',
    f'<div style="margin:24px 0 0;">{promise}</div>',
    f'<div style="margin:24px 0 0;">{whats_new}</div>',
    closing,
)

OUT = "/mnt/user-data/outputs/row_programs_overview_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
