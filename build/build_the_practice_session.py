"""Build The Practice Session page fragment (Layer 3, coach-facing).

Reconstructed August 2026 from the live HTML. Replaces build_practice_session.py
/ fpp_practice_session_embed.html.

Coach page, under the permissioned /page/coaching-at-row tree. No links out, and
no layer map.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE, ROW_ALT,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    p, body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede,
)


def set_line(text, i=0):
    """A set as it would appear on a board. Mono, bold and 15px per the build
    guide, on a tint so it reads as a written set rather than as prose."""
    bg = ROW_ALT if i % 2 == 1 else SAND
    return (f'<div style="font-family:{MONO_FONT};font-size:15px;font-weight:700;color:{NAVY};'
            f'background:{bg};border-left:3px solid {CYAN};border-radius:0 8px 8px 0;'
            f'padding:11px 14px;margin:0 0 8px;line-height:1.5;">{text}</div>')


page_hero = hero(
    "How We Design Training &nbsp;&middot;&nbsp; Layer 3",
    "The Practice Session",
    "How a single session is built and written. One shape, one purpose, and one way to put a set "
    "on the board, so a swimmer can read any ROW whiteboard.")


# ---------------------------------------------------------------------------
# The one rule
# ---------------------------------------------------------------------------

one_rule = card(
    h2("The one rule")
    + body("<strong>Every session has one purpose. Name it before you write it.</strong> If you "
        "cannot say in one sentence what a session is for, the swimmers will not know either, "
        "and the set will drift towards moderate work that trains nothing well.")
    + body("A session also develops the swimmer, not only the swim. What that looks like in "
        "practice is at the bottom of this page.")
    + note("The five zones and the age guidance behind them are on How We Design Training. This "
           "document assumes you already have the session's zone from your weekly plan.",
           margin="0")
)


# ---------------------------------------------------------------------------
# Session template
# ---------------------------------------------------------------------------

TEMPLATE = [
    ("Warm-up", "15 to 20%",
     "Raise heart rate, open the shoulders and hips, and get the feel of the water. Ends faster "
     "than it starts. Mostly Zone 1 and Zone 2."),
    ("Skill focus", "10 to 15%",
     "One technical point per session, stated out loud. Drills, then the same point held while "
     "swimming. Low speed, high attention."),
    ("Pre-set", "10%",
     "Bridges the warm-up and the main set. Builds towards the zone the main set will use, so "
     "the first repeat is not the throwaway one."),
    ("Main set", "35 to 45%",
     "The reason the session exists. One zone, or two that support each other. This is the part "
     "you would protect if the session got cut short."),
    ("Speed or race skills", "10%",
     "Starts, turns, breakouts, finishes, or short Zone 5 work. Do it before fatigue spoils the "
     "execution, or keep it deliberately short at the end."),
    ("Cool-down", "10%",
     "Genuine easy swimming, not a token 100. Longer after Zone 3 and Zone 4 sets than after "
     "Zone 2."),
]

template_section = card(
    h2("Session template")
    + lede("A shape, not a straitjacket. Percentages are of total session distance, and assume a "
           "session of 90 minutes or more. Shorter sessions cut the pre-set and shorten the "
           "warm-up first.")
    + data_table(["Part", "Share", "What it does"], [[a, b, c] for a, b, c in TEMPLATE])
    + callout(
        "<strong>One main set per session.</strong> Two big main sets means neither gets done "
        "properly. If the plan needs two, one of them belongs in a different session.")
)


# ---------------------------------------------------------------------------
# How to write a set
# ---------------------------------------------------------------------------

SET_EXAMPLES = [
    "8 x 100 @ 1:30 &middot; Z3 &middot; hold 14 strokes",
    "10 x 200 :15 rest &middot; Z2 &middot; even pace, breathe every 5 on the last 50",
    "6 x 50 @ 1:30 &middot; Z4 &middot; 200 goal pace, breathe every 3",
    "10 x 25 from push @ 1:00 &middot; Z5 &middot; max speed, 5 dolphin kicks off the wall",
]

write_section = card(
    h2("How to write a set")
    + lede("One format, every deck. Reps, distance, interval, zone, focus. The interval is "
           "either a send-off (@ 1:30) or a rest interval (:15 rest). Both are written the "
           "same way.")
    + "".join(set_line(s, i) for i, s in enumerate(SET_EXAMPLES))
    + body("The zone tells the swimmer how hard. The focus tells them what to think about. A set "
        "with no focus is a set the swimmer will just get through.",
        margin="20px 0 16px")
    + body("Write one interval on the board, then adjust by lane or by swimmer. Fitting the set to "
        "the individual is on The Individual Swimmer, and it does not change what is written "
        "here.",
        margin="0")
)


# ---------------------------------------------------------------------------
# Rest interval or send-off
# ---------------------------------------------------------------------------

rest_section = card(
    h2("Rest interval or send-off")
    + lede("A send-off looks more organized. It is often less fair. On a shared interval the "
           "fastest swimmer earns rest and the slowest is punished for being slow, and the two "
           "are no longer doing the same set.")
    + set_line("8 x 100 @ 1:30 &middot; Z3")
    + data_table(
        ["Swimmer", "Holds", "Rest they get", "Cycle on 15 sec rest"],
        [["Swimmer A", "1:10", "20 seconds", "1:25"],
         ["Swimmer B", "1:18", "12 seconds", "1:33"],
         ["Swimmer C", "1:25", "5 seconds", "1:40"]])
    + body("Swimmer A gets four times the rest of Swimmer C. A is doing a comfortable Zone 3 set. C "
        "is working at the top of Zone 3 and will fade before the end. The board said Zone 3. "
        "Only one of them got Zone 3.",
        margin="16px 0 16px")
    + set_line("8 x 100 :15 rest &middot; Z3")
    + body("That gives all three the same recovery. They finish at different times, which is the "
        "part coaches dislike, and it is a smaller problem than three swimmers doing three "
        "different sets.",
        margin="16px 0 0")
    + data_table(
        ["Set type", "Use", "Why"],
        [["Long aerobic reps, mixed lane", "Rest interval",
          "Everyone gets the same recovery. This is the set most damaged by a shared send-off."],
         ["Work at the top of Zone 3", "Send-off, set per lane",
          "Pace control matters, so the clock is useful. Give each lane its own send-off from "
          "test times."],
         ["Race pace and speed", "Send-off with generous rest",
          "Rest is long enough that the difference between swimmers no longer distorts the set."],
         ["Recovery", "Rest interval or continuous",
          "Nothing is gained by putting recovery on a clock."]])
)


TIDY = [
    "<strong>Regroup at round breaks.</strong> Rest interval inside each round, everyone back on "
    "the top of the clock between rounds. The drift never grows past one round.",
    "<strong>Give each lane its own send-off.</strong> Same set, three send-offs. Organized like "
    "a clock set, fair like a rest set. The middle ground most coaches are looking for.",
    "<strong>Order the lane by speed.</strong> Within a lane, similar swimmers means similar "
    "cycles, so the lane stays together on its own.",
    "<strong>Say the rest out loud each rep early on.</strong> Swimmers new to rest intervals "
    "need two or three sessions to learn to watch the clock for themselves. It is a skill, and "
    "it is worth teaching.",
]

tidy_section = card(
    h2("Keeping it tidy")
    + lede("The organization concern is real. These four fixes handle almost all of it.")
    + list_shell("".join(numbered_row(n + 1, t, i=n) for n, t in enumerate(TIDY)))
)


# ---------------------------------------------------------------------------
# Coaching the whole swimmer
# ---------------------------------------------------------------------------

MARKERS = [
    ("Stay with the focus",
     "Name one focus out loud and put it on the board. At the halfway point, ask two swimmers to "
     "say it back to you.",
     "Thirty seconds. If nobody can repeat it, they were never working on it."),
    ("Come back from a setback",
     "When a swimmer misses the interval, the next rep is the reset. Say &ldquo;next one&rdquo;, "
     "not &ldquo;that&rsquo;s fine&rdquo;. Build one set a week where holding on is not expected.",
     "Nothing. It is a choice of words and a choice of set."),
    ("Know what I'm aiming at",
     "At the start of a block, every swimmer names one thing they are chasing. Refer to it by "
     "name at least once a week, to that swimmer.",
     "Five minutes once a block, then a sentence here and there."),
    ("Ready to train",
     "Start on time. Do not re-explain the set for a swimmer who arrived late. Do not wait for "
     "the lane that is still talking.",
     "Nothing, and it is the habit that decides whether the other eleven are possible."),
    ("Coachable",
     "Give a correction, then watch the next rep and tell them whether it changed. Every time.",
     "Attention. If you never check, you have taught them that corrections are optional."),
    ("Part of the team",
     "The last swimmer in the lane gets counted in by the others. Equipment away before anyone "
     "leaves the deck.",
     "Nothing. It is a standard you hold or quietly drop."),
]

whole_swimmer_section = card(
    h2("Coaching the whole swimmer")
    + lede("Physical and technical development happen by default in a well-built session. Mental "
           "and character development only happen if you build them in. These are the six "
           "markers from The ROW Way that a normal session either develops or quietly neglects.")
    + data_table(["Marker", "What it looks like on deck", "What it costs you"],
                 [[a, b, c] for a, b, c in MARKERS])
    + callout(
        "<strong>This is not a talk at the end of practice.</strong> If developing these needs a "
        "speech, they are not embedded. They are habits inside the session, or they are nothing.")
    + note("The full model, including the physical and technical markers and the four-step scale, "
           "is on The ROW Way.")
)


# ---------------------------------------------------------------------------
# One set, four specialties
# ---------------------------------------------------------------------------

specialties_section = card(
    h2("One set, four specialties")
    + lede("Swimmers with different events do not need separate sets. Here is one set serving "
           "four swimmers in the same lane block.")
    + set_line("MAIN SET &middot; 8 x 100 &middot; Z3 &middot; hold even pace")
    + data_table(
        ["Swimmer", "What they swim", "Why"],
        [["Distance freestyle", "8 x 100 free, 15 sec rest",
          "Holds even pace across the whole set. The set as written is already their event."],
         ["200 IM", "8 x 100 IM order, one stroke per round",
          "Same zone, same rest. The stroke rotation adds the demand their event needs."],
         ["100 butterfly", "8 x 100 as 50 fly / 50 free, or 8 x 75",
          "Shortens the fly exposure so the zone is held honestly instead of degrading into "
          "survival."],
         ["50 and 100 freestyle", "6 x 100 free, more rest, faster target",
          "Still a Zone 3 set. Fewer reps at a higher intensity suits the swimmer without "
          "dropping the aerobic work they need."]])
    + callout(
        "<strong>The zone is fixed. The prescription moves.</strong> Interval, rep count, "
        "distance, stroke, rest and target pace are all available to you. Change one at a time "
        "and for a stated reason.")
    + note("The Individual Swimmer covers the full set of eight levers, how to set targets from "
        "test results, and how to organize a lane so this runs smoothly.",
        margin="16px 0 0")
)


full = wrap_page(
    page_hero,
    lanes_divider(),
    one_rule,
    f'<div style="margin:24px 0 0;">{template_section}</div>',
    f'<div style="margin:24px 0 0;">{write_section}</div>',
    f'<div style="margin:24px 0 0;">{rest_section}</div>',
    f'<div style="margin:24px 0 0;">{tidy_section}</div>',
    f'<div style="margin:24px 0 0;">{whole_swimmer_section}</div>',
    f'<div style="margin:24px 0 0;">{specialties_section}</div>',
)

OUT = "/mnt/user-data/outputs/row_the_practice_session_embed.html"
with open(OUT, "w", encoding="utf-8") as f:
    f.write(full)

print("wrote", OUT, len(full), "chars")
