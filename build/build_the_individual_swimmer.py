"""Build The Individual Swimmer page fragment (Layer 4, coach-facing).

Reconstructed August 2026 from the live HTML. Replaces build_individual_swimmer.py
/ fpp_individual_swimmer_embed.html.

This page owns the eight levers. Layers 2 and 3 name a subset and point here.

Coach page, under the permissioned /page/coaching-at-row tree. No links out, and
no layer map.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede,
)


def set_line(text):
    return (f'<div style="font-family:{MONO_FONT};font-size:15px;font-weight:700;color:{NAVY};'
            f'background:{SAND};border-left:3px solid {CYAN};border-radius:0 8px 8px 0;'
            f'padding:11px 14px;margin:0 0 8px;line-height:1.5;">{text}</div>')


page_hero = hero(
    "How We Design Training &nbsp;&middot;&nbsp; Layer 4",
    "The Individual Swimmer",
    "One set, a whole lane. How to fit a written set to the swimmer in front of you without "
    "writing four sets, and without changing what the set is training.")


one_rule = card(
    h2("The one rule")
    + body("<strong>The zone is fixed. The prescription moves.</strong> Everything on this page "
        "changes how hard a set is for one swimmer without changing what the set trains. If a "
        "change moves a swimmer out of the zone on the board, it has gone too far.")
    + body("This is not extra work at the whiteboard. It is one set, written once, with a small "
        "number of adjustments made in the lane. Most of them take a coach a few seconds.")
    + body("Change one thing at a time. Shorten the rest, or add reps, or raise the target. Change "
        "two and you no longer know which one worked, and the set often lands in a different "
        "zone than the one you wrote.",
        margin="0")
)


# ---------------------------------------------------------------------------
# The eight levers
#
# Canonical, agreed August 2026. The Training Week and The Practice Session name
# a subset using these exact names and point here for the full set. Before that
# the three pages published three different lists.
# ---------------------------------------------------------------------------

LEVERS = [
    ("Rest interval", "8 x 100 on :15 rest",
     "Everyone gets the same recovery whatever their speed. The single most useful lever for "
     "aerobic work, and the fairest.", "Zone 1, Zone 2, Zone 3"),
    ("Send-off, set per lane", "Lane 1 @ 1:20, Lane 2 @ 1:30, Lane 3 @ 1:40",
     "Keeps a clock set organized while giving each lane roughly equal rest. Set the send-offs "
     "from test times, not from guesswork.", "Zone 3, Zone 4"),
    ("Target time or pace", "Hold your 200 goal pace",
     "The set defines itself against each swimmer's own race, so it individualizes without any "
     "lane management at all.", "Zone 4"),
    ("Rep count", "8 x 100 becomes 6 x 100",
     "Fewer reps at a higher intensity. Useful for sprinters, for swimmers returning from "
     "illness, and for anyone whose technique goes before the set does.", "Zone 3, Zone 4"),
    ("Distance per rep", "8 x 100 becomes 8 x 75",
     "Holds the zone honest for a slower swimmer or a harder stroke, instead of letting the set "
     "decay into survival.", "Any"),
    ("Stroke or event", "Free, best stroke, or IM order",
     "Same zone, different demand. This is how one set serves a distance freestyler and a 200 "
     "IMer at the same time.", "Any"),
    ("Equipment", "Fins, paddles, snorkel, band",
     "Changes the load or the focus without changing the zone. Also a technique lever, not only "
     "a speed one.", "Any"),
    ("Position in the range", "Bottom of Zone 3, or top of Zone 3",
     "A zone is a band. A younger or newer swimmer sits at the bottom of it; an 18&U swimmer can "
     "work the top. No change to the written set at all.", "Zone 2, Zone 3"),
]

levers_section = card(
    h2("The eight levers")
    + lede("These are the adjustments available to you. Almost every set can be fitted to a lane "
           "with one or two of them.")
    + data_table(["Lever", "Example", "What it does", "Best for"],
                 [[a, b, c, d] for a, b, c, d in LEVERS])
)


targets_section = card(
    h2("Where targets come from")
    + body("Individual targets should come from a number, not from a feeling about a swimmer. "
        "Club-wide tests give you that number. Because every group runs the same tests at the "
        "same points in the season, a swimmer's targets follow them as they move up.")
    + body("Which tests we use, when they run, and how a result converts into a Zone 3 target or a "
        "send-off are covered on the club testing page. Until a swimmer has a current test "
        "result, set the lane by ability and adjust by what you see.")
    + callout(
        "<strong>12&U swimmers do not need pace targets.</strong> Test them, record it, and show "
        "them the improvement. Then let them race the clock rather than chase a number in "
        "training.")
)


LANE_HABITS = [
    "<strong>Order the lane by speed.</strong> Fastest leaves first, five seconds between "
    "swimmers. Similar swimmers together means similar cycles, and the lane holds itself "
    "together.",
    "<strong>Three send-offs maximum.</strong> One per lane, or three across the group. More "
    "than that and you are managing a spreadsheet instead of coaching.",
    "<strong>Regroup at round breaks.</strong> Rest intervals inside a round, everyone back on "
    "the top of the clock between rounds. Drift never grows past one round.",
    "<strong>Put targets on a lane card, not the board.</strong> The board carries the set. A "
    "card at the end of the lane carries the numbers. The board stays readable for everyone.",
    "<strong>Say the adjustment out loud.</strong> &ldquo;Sprinters, six not eight.&rdquo; Ten "
    "seconds of explanation stops a swimmer thinking they are being given less because they are "
    "worth less.",
    "<strong>Teach the clock.</strong> Reading a rest interval is a skill. Two or three sessions "
    "of coaching it, once, pays back for the rest of a swimmer's career.",
]

lane_section = card(
    h2("Running the lane")
    + lede("The reason coaches avoid individual prescriptions is that a lane gets messy. These "
           "six habits handle almost all of it.")
    + list_shell("".join(numbered_row(n + 1, t, i=n) for n, t in enumerate(LANE_HABITS)))
)


board_section = card(
    h2("One board, four lanes")
    + lede("The whiteboard says this:")
    + set_line("MAIN SET &middot; 8 x 100 &middot; Z3 &middot; even pace, hold your stroke count")
    + note("The lane card says this:", margin="16px 0 14px")
    + data_table(
        ["Lane", "Swims", "Interval", "Focus"],
        [["Lane 1 &middot; PD1 distance", "8 x 100 free", "@ 1:25", "Hold 1:10, even split"],
         ["Lane 2 &middot; SD mixed", "8 x 100 free", "on :15 rest", "Hold stroke count"],
         ["Lane 3 &middot; SD sprinters", "6 x 100 free", "on :25 rest",
          "Faster than lane 2, strong finish"],
         ["Lane 4 &middot; AGD 2 swimmers", "8 x 75 free", "on :15 rest",
          "Bottom of Zone 3, breathe every 3"]])
    + callout(
        "Every lane is in Zone 3. Every lane is doing the same set. Nobody is doing less work "
        "than anybody else, and it took one line on the board plus four lines on a card.")
)


not_section = card(
    h2("What not to individualize")
    + lede("The set has to stay recognizable as one set. These are the parts that hold it "
           "together.")
    + data_table(
        ["Element", "Change it?", "Why"],
        [["The zone", "Never",
          "If a swimmer cannot hold the zone, change the distance or the rest. Do not let them "
          "drift into Zone 4 on a Zone 3 set."],
         ["The skill focus", "Never",
          "One focus per session, for everyone. It is what makes the group a group."],
         ["The purpose of the set", "Never",
          "If two swimmers are training different systems, you have written two sets, not fitted "
          "one."],
         ["Total rounds", "Rarely",
          "Cutting a swimmer's rounds should be a recovery decision, not a convenience. Reduce "
          "reps within the round instead."],
         ["Interval, reps, distance, target", "Freely", "These are the levers. Use them."]])
)


BY_GROUP = [
    ("10&U", "TOPS 2, TOPS 1", "Lane level only",
     "Group by ability. Adjust distance and rest only. No numbers, no targets."),
    ("12&U", "JD2, JD1, AGD 2, PD3", "Lane level",
     "Lane send-offs by ability. Record test results, but do not set training pace targets yet."),
    ("14&U", "AGD 1, PD2", "Lane level, some individual",
     "Lane send-offs from test times. Individual targets for one or two swimmers, not the whole "
     "group."),
    ("18&U", "SD, PD1, ND", "Individual within lanes",
     "Targets from testing for most swimmers. In PD1 and ND, intervals and event work are "
     "planned per swimmer against the season map."),
]

group_section = card(
    h2("How far to take it by group")
    + lede("Individualization grows with training age, not with pathway. Starting too early makes "
           "a group feel like a set of individuals who happen to share a pool.")
    + data_table(
        ["Age band and groups", "Level", "What that looks like"],
        [[f'{band} <span style="font-weight:400;color:{INK_SOFT};">{groups}</span>', level, what]
         for band, groups, level, what in BY_GROUP])
    + note("The same is true away from the intervals. A swimmer at &ldquo;with reminders&rdquo; on "
        "staying with a focus needs a different prompt from one at &ldquo;on my own&rdquo;. The "
        "markers and the four-step scale are on The ROW Way.",
        margin="16px 0 0")
    + callout(
        "<strong>A lane is still a team.</strong> Swimmers should leave a session having done "
        "something together. If every swimmer has a different number on a card and nothing in "
        "common, something has been lost that is worth more than the precision gained.")
)


full = wrap_page(
    page_hero,
    lanes_divider(),
    one_rule,
    f'<div style="margin:24px 0 0;">{levers_section}</div>',
    f'<div style="margin:24px 0 0;">{targets_section}</div>',
    f'<div style="margin:24px 0 0;">{lane_section}</div>',
    f'<div style="margin:24px 0 0;">{board_section}</div>',
    f'<div style="margin:24px 0 0;">{not_section}</div>',
    f'<div style="margin:24px 0 0;">{group_section}</div>',
)

OUT = "/mnt/user-data/outputs/row_the_individual_swimmer_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
