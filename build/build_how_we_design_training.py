"""Build the How We Design Training page fragment (parent, coach-facing).

Reconstructed August 2026 from the live HTML. Replaces build_how_we_train.py /
fpp_how_we_train_embed.html: the H1 is How We Design Training, so all four names
move with it.

This page owns the five zones. The four layers are written in its vocabulary and
point back here rather than repeating it.

Coach page, under the permissioned /page/coaching-at-row tree. No links out.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, step_card, hero, lanes_divider, wrap_page,
    list_shell, data_table, lede, zone_tag,
)

from layers_common import (
    ZONES, ZONE, ZONE_AGE, FLAG_OK, FLAG_CARE, PROGRAMS,
)


# ---------------------------------------------------------------------------
# Hero
#
# Eyebrow was "Coaching Framework - Coach Reference". Coaching Framework is not
# a page; the hub is Coaching at ROW. Layer pages read
# "How We Design Training - Layer N", so the parent names the hub.
# ---------------------------------------------------------------------------

page_hero = hero(
    "Coaching at ROW",
    "How We Design Training",
    "What ROW believes about training, and the words we all use to describe it. "
    "Four documents sit underneath this one. They cover the season, the block, "
    "the practice, and the swimmer.")


# ---------------------------------------------------------------------------
# What we believe
#
# Principle 7 was "We are working ourselves out of a job". Reworded August 2026.
# COACH PAGES ONLY. The family version must not carry this line: to a family
# paying fees it reads as a plan to sell them less coaching, which is the failure
# mode the decisions record names for principle 6.
# ---------------------------------------------------------------------------

PRINCIPLES = [
    ("Aerobic development comes first",
     "At every age, in every group. The aerobic base is what everything else is built on, and "
     "it is the one thing that cannot be rushed later. Fast swimming built on a thin base does "
     "not hold up."),
    ("Adaptation comes from the unload, not the load",
     "Swimmers do not improve during hard training. They improve while recovering from it. Easy "
     "weeks are not time off from the plan. They are the part of the plan that pays."),
    ("Skill is developed under fatigue",
     "Perfect technique when fresh is a starting point, not the goal. Races are swum tired, so "
     "skill work belongs inside hard sets and not only in the warm-up."),
    ("Speed is maintained, never rebuilt",
     "Short, fast work appears in every phase and every group, all year. Speed is lost quickly "
     "and costs very little to keep."),
    ("We prescribe effort, not pace",
     "A zone tells a swimmer how hard to work. It does not tell them what time to hold. That is "
     "what lets one set serve a whole lane of different abilities. It also means the rest is "
     "usually the thing to fix, not the send-off."),
    ("Every season adds a layer to the foundation",
     "Each year is trained fully and raced hard, and each year is built on the one before it. "
     "The aim is a swimmer whose full potential is there to be used when physical and "
     "psychological maturity arrive. That takes patience in the early years and it pays back "
     "for the rest of a career."),
    ("Every year they need us less",
     "Our goal is to graduate athletes who are experts in their own performance. A swimmer who "
     "only performs when a coach is watching has not finished developing."),
    ("A shared language, not a recipe book",
     "The plan is written down so it can be handed over, questioned, and improved. What is "
     "shared across ROW is the language and the philosophy. The creativity each coach brings to "
     "their own group is the point of the work, not a departure from it."),
]

principles_section = card(
    h2("What we believe")
    + lede("Eight principles. Everything in the four layers below follows from these.")
    + "".join(step_card(n + 1, title, body) for n, (title, body) in enumerate(PRINCIPLES))
    + callout(
        "These principles describe how we train. <strong>The ROW Way</strong> describes what we "
        "are developing. Four dimensions, twelve markers written in the swimmer's own words, and "
        "a four-step scale from &ldquo;learning it&rdquo; to &ldquo;when it&rsquo;s hard&rdquo;. "
        "It is open to every member, and it is what swimmer reviews and group move conversations "
        "are built on.")
)


# ---------------------------------------------------------------------------
# The five zones
# ---------------------------------------------------------------------------

def age_flag(kind):
    ok = kind == "ok"
    bg, glyph, label = ((FLAG_OK, "&#10003;", "All ages") if ok
                        else (FLAG_CARE, "&#9888;", "Use with care"))
    return (f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;'
            f'font-size:10px;letter-spacing:0.06em;text-transform:uppercase;background:{bg};'
            f'color:{FOAM};border-radius:4px;padding:3px 8px;white-space:nowrap;">'
            f'{glyph}&nbsp; {label}</span>')


def _field(label, value_html):
    return (f'<div style="margin:0 0 10px;">'
            f'<span style="display:block;font-family:{MONO_FONT};font-weight:700;font-size:10.5px;'
            f'letter-spacing:0.08em;text-transform:uppercase;color:{INK_SOFT};margin:0 0 3px;">'
            f'{label}</span>{value_html}</div>')


def dl_prose(label, value):
    """A field whose value is a sentence. Body font, normal weight, like any
    other copy on the page."""
    return _field(label, f'<span style="display:block;font-family:{BODY_FONT};font-size:14px;'
                         f'color:{INK};line-height:1.55;">{value}</span>')


def dl_data(label, value):
    """A field whose value is a name, a number or a set. Mono and bold, so it
    reads as data rather than as prose, and so it is legible at 15px per the
    build guide. Applied to every data field or none: the earlier version bolded
    three of six with no rule behind which."""
    return _field(label, f'<span style="display:block;font-family:{MONO_FONT};font-size:15px;'
                         f'font-weight:700;color:{NAVY};line-height:1.5;">{value}</span>')


def zone_card(num, feels, used_for, typical, i=0):
    colour, title, bg, fg, br, hr, hr10 = ZONE[num]
    row_bg = ROW_ALT if i % 2 == 1 else FOAM
    return (
        f'<div style="padding:18px 22px;background:{row_bg};border-top:1px solid {LINE};">'
        f'<div style="margin:0 0 12px;">{zone_tag(num)}{age_flag(ZONE_AGE[num])}</div>'
        f'{dl_data("Descriptor", f"{colour} &mdash; {title}")}'
        f'{dl_data("Heart rate", hr)}'
        f'{dl_data("Beats in 10 seconds", hr10)}'
        f'{dl_data("Typical set", typical)}'
        f'{dl_prose("Feels like", feels)}'
        f'{dl_prose("Used for", used_for)}'
        f'</div>'
    )


ZONE_DETAIL = {
    1: ("Very easy. Could hold a conversation. No strain anywhere.",
        "Warm-up, cool-down, recovery between hard efforts, technique work at low speed.",
        "Continuous swim, or 100s on generous rest"),
    2: ("Steady and comfortable. Could keep going a long time. Breathing is settled.",
        "Building the engine. The bulk of Accumulation work. Technique held under mild fatigue.",
        "400s to 1500s, 10 to 20 sec rest"),
    3: ("Comfortably hard through to hard but sustainable. Working, controlled, talking gets "
        "short.",
        "The whole high-end aerobic range, and the zone that carries most of our hard work. Set "
        "design does the fine tuning inside it: rep length, rest, and target pace.",
        "50s to 400s, 10 to 30 sec rest"),
    4: ("Goal race speed. Hard. Needs real rest to repeat it well.",
        "Learning and holding target pace for the swimmer's events. The core of Intensification.",
        "25s to 200s, rest 1:1 or more"),
    5: ("Maximum. Full effort, full recovery, every repeat as fast as the first.",
        "Top-end speed, starts, turns, breakouts, stroke rate. Used in every phase, all ages.",
        "10m to 25m, rest 30 sec to 2 min"),
}

zones_section = card(
    h2("The five zones")
    + lede("The shared language for all four layers. A season, a week, a practice and a single "
           "swimmer's lane are all described in these five words.")
    + body("<strong>The number is the name.</strong> Zone 3 in writing, Z3 on a board. The colour "
        "is kept as a descriptor, because it runs roughly the way a swimmer looks at that "
        "effort, but it is not how a zone is called. One handle, so nobody has to translate.")
    + body("The heart rate bands come from Swimming Canada's training zone terminology, which "
        "already works in beats below maximum. Our five zones map onto their categories without "
        "forcing, and Zone 3 covers two of them, which is why it is the widest zone on the page.")
    + list_shell("".join(
        zone_card(num, *ZONE_DETAIL[num], i=i)
        for i, (num, *_rest) in enumerate(ZONES)))
    + callout(
        "<strong>A zone is an effort, not a time.</strong> That holds across ages, and it holds "
        "just as strongly inside a single group. A 12&U swimmer and an 18&U national swimmer can "
        "both swim a Zone 3 set in the same block. So can a 50 freestyler and an 800 freestyler, in "
        "the same lane, on the same clock.")
    + callout(
        "<strong>Count for ten seconds and read the number straight off the card.</strong> "
        "No multiplying, because that is where the mistakes come from. Start the count within "
        "two or three seconds of the wall, since the rate falls quickly once a swimmer stops.")
    + callout(
        "<strong>Why beats below maximum, and not a percentage or a set of fixed numbers.</strong> "
        "The heart rate a swimmer reaches at hard aerobic work falls a long way through "
        "adolescence, so any chart written for "
        "adults sits wrong for a 12&U swimmer. Working from each swimmer's own maximum removes "
        "that problem instead of correcting for it. It also means a swimmer's bands still work "
        "when they move up a group.")
)


# ---------------------------------------------------------------------------
# The zones in each phase
# ---------------------------------------------------------------------------

PHASE_ZONES = [
    ("Introduction", (1, 2, 5),
     "Technique and habit. Short Zone 5 work keeps speed alive while volume is low."),
    ("Accumulation", (2, 3, 5),
     "High volume. Zone 3 sits at its lower end here: long reps, short rest, even pacing."),
    ("Consolidation", (1, 3, 5),
     "Volume drops, intensity holds. Keep a short Zone 3 or Zone 5 touch so sharpness is not lost."),
    ("Intensification", (3, 4, 5),
     "Zone 4 is the point of this phase. Zone 3 shifts to its top end: shorter, faster, broken."),
    ("Peaking", (4, 5, 1),
     "Short, sharp, and rare. Total volume is low. Every fast swim should feel easy to produce."),
    ("Transition", (1, 2),
     "Easy swimming only, if any. Other sports welcome."),
]

phase_zones_section = card(
    h2("The zones in each phase")
    + lede("The phase decides the zone mix. This is where the vocabulary meets the season plan.")
    + data_table(
        ["Phase", "Main zones", "Notes"],
        [[name, "".join(zone_tag(z) for z in zs), note] for name, zs, note in PHASE_ZONES])
    + note("Week by week percentages are on The Training Week.", margin="14px 0 0")
)


# ---------------------------------------------------------------------------
# Pathways and groups
# ---------------------------------------------------------------------------

pathways_section = card(
    h2("Our pathways and groups")
    + lede("Six pathways. A pathway describes what a swimmer is training for, "
           "and swimmers progress through the groups within it. Only the last three build a "
           "season around a peak meet.")
    + data_table(
        ["Pathway", "Group", "Short", "Sessions", "Hours a week"],
        [[pw, name, short, sess, hrs] for pw, name, short, sess, hrs in PROGRAMS])
    + callout(
        "<strong>&Under is a stage, not a birthday.</strong> The bands let a swimmer move when "
        "they are ready by training and maturity, not on a date. Read 12&U as a level of "
        "readiness. Some 13-year-olds belong there and some 11-year-olds do not.")
)


# ---------------------------------------------------------------------------
# What each group uses
# ---------------------------------------------------------------------------

GROUP_ZONES = [
    ("10&U", "TOPS 2, TOPS 1", (1, 2, 5),
     "Skills, play, and aerobic exposure. Speed in short bursts.",
     "No formal Zone 3 or Zone 4 sets. Effort comes from games and racing, not from a target."),
    ("12&U", "JD2, JD1, AGD 2, PD3", (1, 2, 5),
     "Aerobic base and pure speed. Skill drives everything.",
     "Zone 3 only in short, low-end designs. No Zone 4 sets."),
    ("14&U", "AGD 1, PD2", (1, 2, 3, 5),
     "Aerobic capacity is the priority. Speed stays year round.",
     "Zone 3 grows through the year. Zone 4 only near peak meets."),
    ("18&U", "SD, PD1, ND", (1, 2, 3, 4, 5),
     "Full range, with Zone 2 and Zone 3 carrying the volume.",
     "Zone 4 with real rest. ND and PD1 plan zone use week by week against the season map."),
]

group_zones_section = card(
    h2("What each group uses")
    + lede("Same five zones everywhere. The mix follows the &Under band, not the pathway. A 12&U "
           "swimmer in PD3 and a 12&U swimmer in JD2 use the same zones; they differ in how "
           "much, not in which. What the pathway changes is which meet they peak for.")
    + data_table(
        ["Age band and groups", "Zones in regular use", "Emphasis", "Handle with care"],
        [[f'{band} <span style="font-weight:400;color:{INK_SOFT};">{groups}</span>',
          "".join(zone_tag(z) for z in zs), emphasis, care]
         for band, groups, zs, emphasis, care in GROUP_ZONES])
    + callout(
        "<strong>Do not rush the top of Zone 3, or Zone 4, with young swimmers.</strong> Hard "
        "anaerobic work buys quick short-term gains and costs long-term development. If a 12&U "
        "set leaves swimmers unable to hold technique, it was the wrong zone.", warn=True)
)


# ---------------------------------------------------------------------------
# The layer map is gone from all five pages. It lives on the hub only, which is
# the one page that changes when a page is added. layer_row and parent_row stay
# in row_page_helpers.py for that page.
#
# The closing note is kept: it tells a coach where to start, which the map never
# did.
# ---------------------------------------------------------------------------

closing = callout(
    "<strong>New to this? Read How We Plan Training first.</strong> The six phases come before "
    "everything else, and nothing below them makes sense without them.")


full = wrap_page(
    page_hero,
    lanes_divider(),
    principles_section,
    f'<div style="margin:24px 0 0;">{zones_section}</div>',
    f'<div style="margin:24px 0 0;">{phase_zones_section}</div>',
    f'<div style="margin:24px 0 0;">{pathways_section}</div>',
    f'<div style="margin:24px 0 0;">{group_zones_section}</div>',
    closing,
)

OUT = "/mnt/user-data/outputs/row_how_we_design_training_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
