"""Build the How We Plan Training page fragment (Layer 1, coach-facing).

Reconstructed August 2026 from the live HTML, which was the only surviving copy.
Replaces the legacy build_training_phases.py / fpp_training_phases_embed.html pair:
the H1 changed to How We Plan Training, so all four names move with it.

Coach page. Lives at /page/coaching-at-row/how-we-plan-training, which is
permissioned. No cross-page links: only the hub carries those.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, phase_row, numbered_row, data_table, lede,
)

# The layer map lives on the parent and the hub only, so this page imports
# neither LAYERS nor PARENT.
from layers_common import PATHWAY_PEAKS


# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------

page_hero = hero(
    "How We Design Training &nbsp;&middot;&nbsp; Layer 1",
    "How We Plan Training",
    "Six names for what training is doing, shared by every group from 10&U to 18&U. "
    "The names never change. How much of the season each one takes does.")


# ---------------------------------------------------------------------------
# Where this sits
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# How to use this
# ---------------------------------------------------------------------------

how_to_use = card(
    h2("How to use this")
    + body("These six names describe what training is doing right now. They are not a calendar "
        "and they are not in a fixed order. A phase can repeat as often as the plan needs it. "
        "Use the same name for the same purpose in every group, so a swimmer moving from "
        "10&U to 18&U hears one consistent story.", margin="0 0 10px")
    # Closes an orphan: the page used block and cycle interchangeably and never
    # said they were different things.
    + body("A <strong>block</strong> is one run of a phase. A <strong>cycle</strong> is a run of "
        "phases that ends in Transition.", margin="0 0 10px")
    + body("Each phase does one of three jobs. <strong>Load</strong> adds volume or intensity. "
        "<strong>Unload</strong> takes it away, for three different reasons. "
        "<strong>Entry</strong> brings a swimmer back into training.", margin="0")
)


# ---------------------------------------------------------------------------
# The six phases
#
# One word per idea, held across the whole page:
#   volume     not metres, total work, or training stress
#   intensity  not quality or harder work
#   Peaking    not taper, except the single gloss in the Peaking row
#   peak meet  not designated peak meet or a meet named as a peak
#   race through  for every meet that is not a peak
# ---------------------------------------------------------------------------

PHASES = [
    ("Introduction", "Get ready to train.", "ENTRY", "2 to 4 weeks",
     "Technique reset, skill drills, and basic dryland movement. Volume returns gradually. "
     "Rebuild attendance, sleep, and warm-up routines. Use this phase any time a swimmer "
     "returns from four or more weeks away, not just at season start.",
     "Volume: low, rising &nbsp;&middot;&nbsp; Intensity: low",
     (1, 2)),

    ("Accumulation", "Build the engine.", "LOAD", "4 to 12 weeks",
     "Aerobic capacity and durability. Long sets, high volume, general strength. Hold stroke "
     "technique under fatigue. Expect slower race times here. That is planned, and it is the "
     "message families need most.",
     "Volume: high &nbsp;&middot;&nbsp; Intensity: low to moderate",
     (2, 3)),

    ("Consolidation", "Absorb the work.", "UNLOAD", "4 to 7 days",
     "A short unload so the last block can settle before the next one starts. Volume drops "
     "clearly. Intensity is held, so sharpness is not lost. Best home for a race-through "
     "meet. This is not Peaking and it is not a break. Use it after every hard block.",
     "Volume: down 30 to 40% &nbsp;&middot;&nbsp; Intensity: held",
     (2, 4)),

    ("Intensification", "Sharpen at race pace.", "LOAD", "3 to 5 weeks",
     "Race-specific work. This is where general fitness becomes race fitness. Starts, turns "
     "and finishes at full speed, pacing and race strategy. Volume drops, intensity rises, "
     "and swimmers need more recovery between sessions.",
     "Volume: down &nbsp;&middot;&nbsp; Intensity: high",
     (4, 5)),

    # "This is the taper" is the one place the word taper is allowed to appear.
    # It glosses the name once, then the page uses Peaking everywhere.
    ("Peaking", "Rest and race fast.", "UNLOAD", "1 to 3 weeks",
     "This is the taper. Volume drops clearly while intensity stays sharp. Race rehearsal, "
     "warm-up routine, and mental prep. Only use this name for a peak meet, named before the "
     "season starts. Most groups get two or three peaks in a season, not more.",
     "Volume: low &nbsp;&middot;&nbsp; Intensity: sharp",
     (4, 5)),

    ("Transition", "Recover and reset.", "UNLOAD", "1 to 2 weeks",
     "Repair and review before the next cycle. Other sports, injury care, season debrief, and "
     "goal setting. This is where swimmer reviews against The ROW Way belong. Schedule it in "
     "the plan first. If it is left as whatever time remains, it disappears.",
     "Volume: low &nbsp;&middot;&nbsp; Intensity: low",
     (1,)),
]

phases_section = card(
    h2("The six phases")
    + lede("Each phase has a job, a rough length, the zones it leans on, and a volume and "
           "intensity setting. That is what a visitor would see on deck.")
    + list_shell("".join(
        phase_row(name, tagline, role, length, body, meta, zones=zones, i=i)
        for i, (name, tagline, role, length, body, meta, zones) in enumerate(PHASES)))
)


# ---------------------------------------------------------------------------
# What each pathway peaks for
# ---------------------------------------------------------------------------

pathway_section = card(
    h2("What each pathway peaks for")
    + body("Peaking is the one phase that points at a single meet, and the pathway decides which. "
        "That is what separates Peaking from any other unload.", margin="0 0 14px")
    + data_table(["Pathway", "Groups", "Peak meet"],
                 [[a, b, c] for a, b, c in PATHWAY_PEAKS])
    + lede("The Foundation, Junior and Recreation pathways have no peak meet. They race often "
           "and race through. That is correct, not a gap.")
    + body("Every meet on the calendar is one of three things, and naming which before the season "
        "starts is most of the planning. Where each one sits in a block is on The Training Week.", margin="16px 0 0")
    + data_table(
        ["Kind of meet", "What it is for"],
        [["Peak meet", "The target. The only meets that get Peaking, and the pathway names them."],
         ["Tune-up meet", "Raced tired on purpose, at the end of a block. Tests pacing and "
                          "skills, not fitness."],
         ["Race-through meet", "Raced without changing the plan. Most of the calendar."]])
    + callout(
        "<strong>Most swimmers get two peak meets a year, not more.</strong> One short course, "
        "one long course. Name your two before the season starts and tell families which they "
        "are.")
)


# ---------------------------------------------------------------------------
# Five rules
# ---------------------------------------------------------------------------

RULES = [
    "A load phase is always followed by an unload phase. Never run two load phases back to back.",
    "Consolidation follows a load phase and leads back into one. It never follows Peaking.",
    "Peaking is only for a peak meet, and the pathway names it. Regional peaks at Westerns, "
    "Provincial at OAG or OSC, National at Trials or Nationals.",
    "Transition follows a peak meet or closes a cycle. It is the only phase that resets "
    "everything.",
    "Introduction follows any break of four weeks or more, for a group or for one swimmer.",
]

rules_section = card(
    h2("Five rules")
    + lede("Everything else is your call as lead coach.")
    + list_shell("".join(numbered_row(n + 1, text, i=n) for n, text in enumerate(RULES)))
    + callout(
        "<strong>Meets do not change the phase.</strong> Most meets on our calendar sit inside "
        "Accumulation or Consolidation. A swimmer can race well without Peaking. Tell families "
        "this in September, not in November.")
)


# ---------------------------------------------------------------------------
# Same words, different mix
#
# Finer than AGE_BANDS in layers_common.py, which keeps 12&U as one row. This
# page splits 12&U into Junior and competitive because Peaking differs between
# them. Kept local rather than widening the shared constant.
# ---------------------------------------------------------------------------

MIX_ROWS = [
    ("10&U", "TOPS 2, TOPS 1", "Introduction, Accumulation",
     "Not used", "Long, and encouraged"),
    ("12&U Junior", "JD2, JD1", "Introduction, Accumulation",
     "Not used yet", "1 to 2 weeks, encouraged"),
    ("12&U competitive", "AGD 2, PD3", "Introduction, Accumulation",
     "A few days of lower volume", "1 to 2 weeks, encouraged"),
    ("14&U", "AGD 1, PD2", "Accumulation, Consolidation",
     "About 1 week, once or twice a year", "1 to 2 weeks per cycle"),
    ("18&U", "SD, PD1, ND", "All six, two to three cycles",
     "1 to 3 weeks, two or three times", "1 week, scheduled and protected"),
]

mix_rows = [
    [f'{band} <span style="font-weight:400;color:{INK_SOFT};">{groups}</span>',
     most, peak, trans]
    for band, groups, most, peak, trans in MIX_ROWS
]

mix_section = card(
    h2("Same words, different mix")
    + lede("The vocabulary does not change by group or by pathway. What changes is the share of "
           "the season each phase takes, and that follows the age band.")
    + data_table(
        ["Age band and groups", "Most of the season sits in", "Peaking", "Transition"],
        mix_rows)
    + note("Questions about how this applies to your group go to the Head Coach. "
           "Bring your season plan.", margin="14px 0 0")
)


# ---------------------------------------------------------------------------
# Assemble
# ---------------------------------------------------------------------------

full = wrap_page(
    page_hero,
    lanes_divider(),
    how_to_use,
    f'<div style="margin:24px 0 0;">{phases_section}</div>',
    f'<div style="margin:24px 0 0;">{pathway_section}</div>',
    f'<div style="margin:24px 0 0;">{rules_section}</div>',
    f'<div style="margin:24px 0 0;">{mix_section}</div>',
)

OUT = "/mnt/user-data/outputs/row_how_we_plan_training_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
