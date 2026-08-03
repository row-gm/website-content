"""Build The Training Week page fragment (Layer 2, coach-facing).

Reconstructed August 2026 from the live HTML. Replaces build_training_week.py /
fpp_training_week_embed.html.

Coach page, under the permissioned /page/coaching-at-row tree. No links out, and
no layer map: that lives on How We Design Training and on the hub only.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede, zone_tag,
)

from layers_common import LOAD_BANDS


def h3(text):
    return (f'<h3 style="font-family:{DISPLAY_FONT};text-transform:uppercase;letter-spacing:0.01em;'
            f'color:{NAVY};font-size:18px;margin:26px 0 10px;">{text}</h3>')


def zones(*nums):
    return "".join(zone_tag(n) for n in nums)


page_hero = hero(
    "How We Design Training &nbsp;&middot;&nbsp; Layer 2",
    "The Training Week",
    "How a phase becomes weeks, and a week becomes sessions. This is the layer that turns a "
    "season plan into something a coach can actually write on a Sunday night.")


# ---------------------------------------------------------------------------
# What every week contains
#
# "Quality day" is retired. A hard day is the session type; intensity is the
# dial. Both were being carried by one word.
# ---------------------------------------------------------------------------

NON_NEGOTIABLES = [
    "<strong>One long aerobic session every week.</strong> In every phase, including Peaking, "
    "though it shrinks. It is the session that holds the base together when everything else is "
    "getting shorter and faster.",
    "<strong>Speed touched at least twice a week.</strong> Short Zone 5 work, in every phase, at "
    "every age. Speed is lost faster than it is built and it costs almost nothing to maintain.",
    "<strong>Never two hard days back to back at 14&U and below.</strong> AGD 14&U, PD2 14&U and every "
    "group below them. Put an aerobic or recovery day between. SD, PD1 and ND can stack hard "
    "days when the two sessions train different systems, but it should be a decision, not an "
    "accident.",
    "<strong>Every session names one skill focus.</strong> Written on the board with the set. A "
    "week with no stated skill focus is a week of maintenance.",
    "<strong>One session a week is genuinely easy.</strong> Not a short hard session. Easy. If "
    "nobody in the group is bored during it, it was not recovery.",
    "<strong>Dryland does not sit right before a hard swim.</strong> After the swim, or on its "
    "own day. Loading tired shoulders before a Zone 4 set trains poor technique and raises "
    "injury risk.",
    "<strong>Something from The ROW Way in every session.</strong> Not a talk and not a theme "
    "week. One named focus, one correction actually checked, one standard held. Mental and "
    "character development happens inside sessions or it does not happen.",
    "<strong>At least one full day off.</strong> Every group, every week, all year. This is a "
    "floor, not a target.",
]

contains_section = card(
    h2("What every week contains")
    + lede("Eight things hold in every phase and every group. Everything else about the week "
           "is yours.")
    + list_shell("".join(numbered_row(n + 1, t, i=n) for n, t in enumerate(NON_NEGOTIABLES)))
)


# ---------------------------------------------------------------------------
# How many sessions the group trains
# ---------------------------------------------------------------------------

SESSION_BANDS = [
    ("0 to 1", "Every session",
     "There is no room for a dedicated recovery session. Skills and aerobic work in every "
     "session, speed in most. Phases show up as a change of emphasis, not a change of "
     "structure."),
    ("1 to 2", "2 to 3",
     "One clear hard day, two in a heavy Accumulation week. Never back to back. The rest of the "
     "week is aerobic and technical."),
    ("2", "3 to 4",
     "The template on this page is written for this load. Two hard days with at least one day "
     "between them, one long aerobic session, one genuinely easy session."),
    ("2 to 3", "4 to 5",
     "Doubles appear. Hard days can sit closer together when the two sessions train different "
     "systems, but that is a planned decision, not a scheduling accident."),
]

sessions_section = card(
    h2("How many sessions the group trains")
    + lede("Week structure follows the number of sessions, not the age band. A 14&U group at "
           "five sessions and an 18&U group at five sessions build a similar week; what differs "
           "is the zones inside it.")
    + data_table(
        ["Sessions per week", "Hard", "Supporting", "What that means"],
        [[f'{band} <span style="font-weight:400;color:{INK_SOFT};">{groups}</span>', q, s, note]
         for (band, groups), (q, s, note) in zip(LOAD_BANDS, SESSION_BANDS)])
    + callout(
        "<strong>Cut supporting sessions first.</strong> When water time is lost, protect the "
        "hard session and the long aerobic session. A week that loses its easy session is a week "
        "that stopped recovering.")
)


# ---------------------------------------------------------------------------
# Junior Pathway weeks
# ---------------------------------------------------------------------------

JUNIOR_ROWS = [
    ("Every session", "Skills first",
     "Technique is the main set. Kick, body position, breathing, starts, turns. Everything else "
     "supports it."),
    ("Every session", "Short fast swimming",
     "10 to 25 metres, full recovery, made into a game. Speed is easiest to build at this stage "
     "and hardest to add later."),
    ("Most sessions", "Aerobic swimming",
     "Continuous or long reps at an easy, steady effort. Zone 1 and Zone 2. Build the habit of "
     "swimming for a while without stopping."),
    ("Never", "Hard days, targets, Peaking",
     "No Zone 3 or Zone 4 sets, no pace targets, no Peaking. These swimmers race often and race "
     "through."),
]

junior_section = card(
    h2("Junior Pathway weeks")
    + lede("TOPS 3x, JD2 and JD1 train two to four times a week, before pathway placement. There "
           "is not enough water time to build a week around a hard day, and there is no reason "
           "to. Build every session the same way and let the phase change the emphasis.")
    + data_table(["How often", "What", "Why"], [[a, b, c] for a, b, c in JUNIOR_ROWS])
    + note("The phases still apply. Introduction after a break, Accumulation through the middle of "
        "a block, Consolidation as a lighter week, Transition at the end. What changes is the "
        "amount, not the vocabulary. TOPS 2x and the ROW Swim Academy swim once or twice a week; "
        "keep it to "
        "skills and play.",
        margin="14px 0 0")
)


# ---------------------------------------------------------------------------
# Week shapes by phase
# ---------------------------------------------------------------------------

PHASE_SHAPES = [
    ("Introduction", "0 to 1", "3 to 4", "2",
     "Volume rises week to week. Skill sessions dominate. No hard days early."),
    ("Accumulation", "2", "3 to 4", "2 to 3",
     "The heaviest weeks of the year. Hard days are Zone 3, and Zone 3 sits at its lower end."),
    ("Consolidation", "1", "2 to 3", "2",
     "Total volume drops 30 to 40 percent. Keep the hard day, shorten it. Race-through meets fit "
     "here."),
    ("Intensification", "2 to 3", "2 to 3", "3",
     "Hard days are Zone 4, supported by Zone 3. Recovery between them matters more than in "
     "Accumulation."),
    ("Peaking", "2 short", "1 to 2", "3",
     "Everything shortens. Fast work stays, volume goes. Race rehearsal replaces one hard day."),
    ("Transition", "0", "0 to 2", "0 to 1",
     "Optional swimming only. Other sports encouraged. No structure required."),
]

shapes_section = card(
    h2("Week shapes by phase")
    + lede("Counts assume a six-session week. Scale them with the table above, and cut "
           "supporting sessions before hard sessions.")
    + data_table(
        ["Phase", "Hard sessions", "Supporting sessions", "Speed touches", "Notes"],
        [[a, b, c, d, e] for a, b, c, d, e in PHASE_SHAPES])
)


# ---------------------------------------------------------------------------
# How load builds across a block
# ---------------------------------------------------------------------------

BLOCK_WEEKS = [
    ("Week 1", "Introduce", "New sets appear. Moderate volume. Swimmers learn the pace and the "
     "format.", "Should feel manageable. If week 1 buries them, the block is wrong."),
    ("Week 2", "Extend", "Same sets, more of them, or less rest. One variable changes, not two.",
     "Should feel harder than week 1 at the same pace."),
    ("Week 3", "Overload", "The hardest version of the block. Highest volume or the tightest "
     "intervals.", "Fatigue is expected here. Watch technique, not times."),
    ("Week 4", "Consolidate", "Volume drops 30 to 40 percent. Intensity is held so sharpness is "
     "not lost.", "Adaptation lands here. This is where the block pays out."),
]

block_section = card(
    h2("How load builds across a block")
    + lede("Three weeks of building, one week of absorbing. That fourth week is the "
           "Consolidation phase from How We Plan Training, used as a repeating unload rather "
           "than a one-time event.")
    + data_table(["Week", "Job", "What changes", "What to watch"],
                 [[a, b, c, d] for a, b, c, d in BLOCK_WEEKS])
    + callout(
        "<strong>Build on two weeks, not three, at 12&U and below.</strong> JD2, JD1, AGD 12&U and "
        "PD3 usually need the unload after two weeks. AGD 14&U and PD2 14&U sit either side of the line: "
        "use three weeks in Accumulation and two in Intensification.")
)


# ---------------------------------------------------------------------------
# Weekly zone balance
#
# The live page headed these columns W / Pk / R / Pu / G. Nobody can decode that
# and it is a sixth way of writing a zone, so the numbers carry it now.
# ---------------------------------------------------------------------------

ZONE_MIX = [
    ("Introduction", "30 / 55 / 10 / 0 / 5"),
    ("Accumulation", "15 / 55 / 25 / 0 / 5"),
    ("Consolidation", "30 / 45 / 18 / 2 / 5"),
    ("Intensification", "20 / 40 / 25 / 10 / 5"),
    ("Peaking", "35 / 40 / 12 / 8 / 5"),
    ("Transition", "60 / 40 / 0 / 0 / 0"),
]

mix_section = card(
    h2("Weekly zone balance")
    + lede("Share of weekly distance, as a starting point for SD, PD1 and ND. At 14&U shift "
           "Zone 3 down and Zone 1 and Zone 2 up. At 12&U and below, Zone 4 goes to zero. "
           "Adjust and record what you actually did.")
    + f'<div style="margin:0 0 14px;">{zones(1, 2, 3, 4, 5)}</div>'
    + data_table(["Phase", "Z1 / Z2 / Z3 / Z4 / Z5"], [[a, b] for a, b in ZONE_MIX])
    + callout(
        "These are planning numbers, not targets to hit. If a week comes out at 20 percent "
        "Zone 3 instead of 25, nothing is broken. If it comes out at 45, something drifted.")
)


# ---------------------------------------------------------------------------
# Adjusting the mix for the swimmer
# ---------------------------------------------------------------------------

BY_EVENT = [
    ("Distance free, 400 and up", "Zone 2 +5, Zone 3 +5", "Zone 4 &minus;5, Zone 5 &minus;5",
     "More time at the low end of Zone 3, longer reps. Keep some Zone 5; distance swimmers "
     "still finish races."),
    ("200s and IM", "No change", "No change",
     "The default mix is written for this swimmer. What changes is stroke distribution inside "
     "Zone 3, not the amount of it."),
    ("100s", "Zone 4 +3", "Zone 2 &minus;3",
     "Slightly more race pace in Intensification. Everything else holds."),
    ("50s and 100s, sprint focus", "Zone 4 +5, Zone 5 +5", "Zone 2 &minus;5, Zone 3 &minus;5",
     "Fewer Zone 3 metres at a higher intensity. This is a shift, not a swap. Sprinters who "
     "skip aerobic work cannot repeat a fast swim in a prelim and a final."),
]

BY_RESPONSE = [
    ("Recovers fast between reps, holds technique late in a set", "Zone 3 +5, Zone 1 &minus;5",
     "Can carry more intensity in a week. Watch the next block, not the next session."),
    ("Slow to recover, technique goes before the set does", "Zone 1 +5, Zone 3 &minus;5",
     "The set was too hard, not the swimmer too weak. Add rest before you subtract reps."),
    ("Improves sharply from speed work, little from added volume",
     "Zone 5 +2, Zone 4 +3, Zone 2 &minus;5",
     "Common in later-maturing sprinters. Shift, do not swap. The aerobic floor still applies."),
    ("Improves steadily from volume, flat off speed work", "Zone 2 +5, Zone 4 &minus;5",
     "Often an early-season picture rather than a permanent one. Recheck at the end of the "
     "block."),
    ("Growing quickly, coordination is off", "Zone 1 +5, Zone 5 +5, Zone 3 &minus;10",
     "Protect skill and speed, ease the grind. This is temporary and it is not a setback."),
]

adjust_section = card(
    h2("Adjusting the mix for the swimmer")
    + lede("The table above is a group starting point. These are the adjustments worth making, "
           "expressed as percentage points moved from the default. They are small on purpose. "
           "Two swimmers in the same lane should still be doing recognizably the same week.")
    + h3("By event")
    + data_table(["Swimmer", "Add", "Take from", "Why"], [[a, b, c, d] for a, b, c, d in BY_EVENT])
    + h3("By how the swimmer responds")
    + data_table(["What you see", "Adjust", "What it means"],
                 [[a, b, c] for a, b, c in BY_RESPONSE])
    + callout(
        "<strong>The aerobic floor: Zone 1 plus Zone 2 never drops below half the week.</strong> "
        "In any load phase, at any age, for any specialty. Below that line a swimmer stops "
        "building the base that everything else sits on, and the cost shows up two seasons later "
        "rather than next month.")
    + note("Event adjustments apply from 14&U up. At 12&U and below nobody is a specialist yet, and "
        "response adjustments are usually about growth rather than physiology. How the same set "
        "is then fitted to the individual swimmer is on The Individual Swimmer.",
        margin="16px 0 0")
)


# ---------------------------------------------------------------------------
# Where meets and testing land
#
# Three tiers, agreed August 2026. The live page had low-priority, mid-priority
# and target meets here while How We Plan Training had only two states, so the
# two pages described different calendars.
# ---------------------------------------------------------------------------

MEETS = [
    ("Race-through meet", "Consolidation week",
     "Volume was already coming down. The swimmer races fresher and the block still ends where "
     "planned."),
    ("Tune-up meet", "End of a block, before the unload",
     "Race tired on purpose. Use it to test pacing and skills, not to judge fitness."),
    ("Peak meet", "End of Peaking",
     "The only meets that get Peaking. Named before the season starts."),
    ("Testing", "First and last week of a block",
     "Same test, same conditions, same time of day. A test on a tired Friday is not comparable "
     "to one on a fresh Monday."),
]

meets_section = card(
    h2("Where meets and testing land")
    + lede("The calendar has more meets than peak meets. Placing them deliberately is most of "
           "the skill.")
    + data_table(["What", "Where it goes", "Why"], [[a, b, c] for a, b, c in MEETS])
)


# ---------------------------------------------------------------------------
# Same week, different swimmers
#
# One lever row only. The full eight are on The Individual Swimmer, and the
# decisions record puts the depth there rather than here.
# ---------------------------------------------------------------------------

levers_section = card(
    h2("Same week, different swimmers")
    + body("A zone is a prescription of effort, not of time. Two swimmers in the same Zone 3 set, "
        "on different intervals, holding different stroke counts, are both doing Zone 3. Nothing "
        "about the week has to change for the week to fit the swimmer.")
    + callout(
        "<strong>The rest interval is the lever that matters most in a training week.</strong> "
        "On a shared send-off the fastest swimmer can get four times the rest of the slowest, so "
        "they are not doing the same set. Writing 8 x 100 on 15 seconds rest gives everyone the "
        "same recovery. It is the fairest lever for aerobic work, which is most of the week.")
    + body("Seven more levers do the rest of the work, and the full set is on The Individual "
        "Swimmer: the send-off set per lane, target time or pace, rep count, distance per rep, "
        "stroke or event, equipment, and position in the range. Change one at a time, for the "
        "reason you chose it.", margin="20px 0 0")
)


full = wrap_page(
    page_hero,
    lanes_divider(),
    contains_section,
    f'<div style="margin:24px 0 0;">{sessions_section}</div>',
    f'<div style="margin:24px 0 0;">{junior_section}</div>',
    f'<div style="margin:24px 0 0;">{shapes_section}</div>',
    f'<div style="margin:24px 0 0;">{block_section}</div>',
    f'<div style="margin:24px 0 0;">{mix_section}</div>',
    f'<div style="margin:24px 0 0;">{adjust_section}</div>',
    f'<div style="margin:24px 0 0;">{meets_section}</div>',
    f'<div style="margin:24px 0 0;">{levers_section}</div>',
)

OUT = "/mnt/user-data/outputs/row_the_training_week_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
