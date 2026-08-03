"""Shared four-layer model for the ROW How We Train pages.

Imported by build_how_we_train.py and build_training_week.py so the layer map
never drifts between pages. Edit here, rebuild both.
"""

BASE = "https://www.rowswimming.ca"

# --- Live URLs (confirmed) ---
# Slugs match each page's <h1>. Child pages nest under the hub.
HUB = f"{BASE}/page/coaching-at-row"

URL_HUB_COACH = HUB
URL_HOW_WE_PLAN_TRAINING = f"{HUB}/how-we-plan-training"
URL_HOW_WE_DESIGN_TRAINING = f"{HUB}/how-we-design-training"
URL_TRAINING_WEEK = f"{HUB}/the-training-week"
URL_PRACTICE_SESSION = f"{HUB}/the-practice-session"

URL_INDIVIDUAL = f"{HUB}/the-individual-swimmer"


# ---------------------------------------------------------------------------
# Our Development Plan. A member-facing tree, added August 2026.
#
# CHANGED: The ROW Way was standalone at /page/how-we-develop-swimmers. It now
# nests under this parent. The decisions record (section 5b) still describes the
# old location, and section 4b still lists three trees when there are four.
#
# The slug stays how-we-develop-swimmers rather than the-row-way. That is the
# one deliberate exception to naming the slug after the H1, recorded in section
# 5b: descriptive wording for search and navigation.
# ---------------------------------------------------------------------------
URL_OUR_DEVELOPMENT_PLAN = f"{BASE}/page/our-development-plan"
DEV = URL_OUR_DEVELOPMENT_PLAN

URL_HOW_WE_DEVELOP_SWIMMERS = f"{DEV}/how-we-develop-swimmers"   # The ROW Way
URL_THE_GROWTH_SPURT = f"{DEV}/the-growth-spurt"
URL_THE_BIRTHDAY_GAP = f"{DEV}/the-birthday-gap"

# Goal Setting Tool. Sits outside the four-layer model: the layers describe how we design
# training, this describes how a swimmer sets a target. Confirmed live.
# Lives under /page/for-swimmers, NOT under the coach-permissioned /page/coaching-at-row tree,
# so swimmers can reach it without coach permissions.
URL_GOAL_SETTING_TOOL = f"{BASE}/page/for-swimmers/goal-setting-tool"

# Swimmer-facing hub. Third audience tree, alongside the coach tree and The ROW Way.
# ===================== Naming: three jobs, not one =====================
# REVISED August 2026. The old rule said the slug, the H1, the nav label and the
# file name all use the same words. That went too far. Three of them have
# different jobs:
#
#   NAV LABEL   wayfinding. Short, in the visitor's words, whatever helps them
#               find it. "Meet Schedule & Info" is a better nav label than a
#               better page title.
#   H1          the page's real title. As descriptive as the content needs.
#               "Meet and Event Schedule" tells you it covers events and
#               closures too.
#   SLUG        stable and descriptive. It must NOT be rewritten every time a
#               heading is reworded, because that breaks every existing link.
#
# What survives from the old rule, and it is the part that mattered:
#
#   FILE NAME follows the H1. build_<h1>.py and row_<h1>_embed.html. This is
#   what stops the build script for a page becoming unfindable, which has
#   already happened once: the Goal Setting Tool was built as build_swim_math.py.
#
# The limit: the three should still be recognizably the same thing. "Goal Setting
# Tool" against a repo called row-swimming-math was over that line. "For Coaches"
# in the nav against /page/coaching-at-row is not.
#
# So /page/coaching-at-row stays as it is. The nav says For Coaches. Both correct.


# ===================== Nav aliases =====================
# SportsEngine Motion will not allow two navigation entries with the same name.
# So a page that needs to appear in two sections has its real name in one place
# and an alias in the other. This is a platform limit and it is CORRECT. Do not
# "fix" it by making the names match: the nav will reject it.
#
# alias in the nav -> the page it points at
NAV_ALIASES = {
    "Swimmer Equipment List": "ROW Equipment List",
    "Order ROW Clothing & Equipment": "ROW Clothing & Equipment",
}

# The page's real name is what its H1 says, and what a link to it should read.
# The alias exists only to satisfy the nav.


# ===================== The club's own sentences =====================
# These appear on more than one page, so they live here. Four versions of the
# promise were in circulation: cherish or carry, experiences in or through
# competitive swimming. Settled August 2026.
#
# CARRY, not cherish. THROUGH, not in: the club's position is that swimming is
# the vehicle rather than the point, and "through" says that where "in" only
# says the experiences happen inside the sport. "Through" is also the wording in
# the 2026-27 Executive Summary.
PROMISE = ("We&rsquo;re not just training swimmers. We&rsquo;re providing young people, "
           "families, and coaches with positive experiences they will carry long after "
           "they&rsquo;ve left the pool.")

MISSION = ("The mission of the Region of Waterloo Swim Club is to create experiences through "
           "competitive swimming that positively shape our swimmers, families, and coaches "
           "long after their time with the club has ended.")

FOUNDED = 1976


# Booking a new swimmer assessment. THE ONLY LINK. Confirmed August 2026.
#
# The eventId changes when a new registration event is created, so it lives here
# and nowhere else. Never hard-code it in a page script.
#
# Retired: /page/for-parents/team-registration?reg_id=115884, which the home page
# and About Us used under the names "New Swimmer Tryouts" and "Schedule a Swimmer
# Assessment Today". Two links and three names for the same thing. Both of those
# pages need updating to the link below.
URL_ASSESSMENT = f"{BASE}/page/system/teamreg-shopping?eventId=1761153"

URL_EQUIPMENT_LIST = f"{BASE}/page/for-swimmers/row-equipment-list"

URL_FOR_SWIMMERS = f"{BASE}/page/for-swimmers"

# The interactive calculator is hosted off-site because the CMS sanitizer strips <script>.
# Public repo under the ROW GitHub organization, served by GitHub Pages.
CALC_URL = "https://row-gm.github.io/row-swimming-math/"

# --- Not published yet: confirm before linking to any of these ---
URL_HUB_FAMILY = f"{HUB}/for-families"
URL_HOW_WE_PLAN_TRAINING_FAMILY = f"{HUB}/for-families/how-we-plan-training"

# ============================ Training zones ============================
# The five zones are the vocabulary all four layers are written in. They are not
# a layer themselves; How We Design Training owns the full explanation.
#
# DECISION, August 2026: the zone NUMBER is the reference, everywhere.
# "Zone 3" in prose and tables, "Z3" in set notation. This reverses the earlier
# "colour first, number second". The colour is kept as a descriptor and as the
# badge background, because it still tracks roughly what a swimmer looks like at
# that effort, but it is no longer how a zone is named. One handle, not two.
#
# Six became five when the old Red (aerobic build) and Blue (threshold) merged
# into one Red, at the Head Coach's direction.
#
# Hexes read off the live How We Design Training page, August 2026. Confirmed.
#
# Heart rate is BBMax: beats below the swimmer's own maximum, measured in water.
#
# Bands taken from Swimming Canada's Swim Training Zone Terminology, June 2024
# (Tom Vandenbogaerde, Performance Scientist Coach, CSI Pacific), which is the
# national standard and already uses BBMax. Their seven categories map onto our
# five without forcing:
#   Zone 1  <- A1                      80 to 60 BBMax
#   Zone 2  <- A2                      60 to 40 BBMax
#   Zone 3  <- A3 + Threshold          40 to 20 BBMax
#   Zone 4  <- Endurance-Intensive     20 to 0 BBMax
#   Zone 5  <- Explosive Efforts       not a heart rate measure
#
# Zone 3 landing on A3 plus Threshold is worth noting: that is exactly the old
# Red-plus-Blue merge, so the merge lines up with the national bands rather than
# cutting across them.
#
# The 10-second count is Swimming Canada's own field column. Counting for ten
# seconds and reading the number straight off the card means no multiplying on
# deck, which is where the errors come from.
#
# Why beats below max and not a percentage or a bpm chart: heart rate at
# threshold falls steeply through adolescence, so any fixed table written for
# adults sits wrong for a 12&U swimmer. Anchoring to the swimmer's own maximum
# removes the problem instead of correcting for it.
# (number, colour, short title, background, text colour, border, BBMax, beats in 10s)
ZONES = [
    (1, "White",  "Recovery",          "#FFFFFF", "#152225", "#DAD3C2",
     "80 to 60 below max", "20 to 24"),
    (2, "Pink",   "Aerobic Base",      "#E39BAE", "#152225", "#E39BAE",
     "60 to 40 below max", "24 to 26"),
    (3, "Red",    "Aerobic Threshold", "#D64545", "#FFFFFF", "#D64545",
     "40 to 20 below max", "26 to 30"),
    (4, "Purple", "Race Pace",         "#7A5AA8", "#FFFFFF", "#7A5AA8",
     "20 to 0 below max", "30 or more"),
    (5, "Green",  "Speed",             "#3FA35C", "#152225", "#3FA35C",
     "Not a heart rate measure", "&mdash;"),
]

# Age flags on the zone cards. Amber, deliberately not brand RED, because RED
# is already a zone colour.
FLAG_OK = "#2E8B4F"      # green check, "All ages"
FLAG_CARE = "#B8791A"    # amber warning, "Use with care"

ZONE_AGE = {1: "ok", 2: "ok", 3: "care", 4: "care", 5: "ok"}

ZONE = {num: (colour, title, bg, fg, br, hr, hr10)
        for num, colour, title, bg, fg, br, hr, hr10 in ZONES}


# BREAKING CHANGE, August 2026: was a 4-tuple where `title` held the question.
# The question is not the page title, so the layer map named four pages that do
# not exist in the site navigation. Now carries both.
# Rebuild every page that imports this.
# (number, page title, the question it answers, body, page key)
LAYERS = [
    (1, "How We Plan Training", "How we organize a season",
     "The six training phases and the five rules for combining them. Everything below is built "
     "on top of it.", "phases"),
    (2, "The Training Week", "How we organize a block",
     "The training week inside a phase. Session mix, hard and easy days, how load builds week to "
     "week, and where meets and testing land.", "week"),
    (3, "The Practice Session", "How we build a practice",
     "The session template, and one way to write a set on the board so every deck reads the same.",
     "session"),
    (4, "The Individual Swimmer", "How we make it fit the swimmer",
     "Same set, same energy system, different prescription. Interval, distance, target, stroke and "
     "equipment all move without changing what the set is training.", "individual"),
]

# The parent is not a layer and is not numbered. It is the page the four layers
# sit under, and it was missing from its own map, which is why the map showed
# four rows for a set of five pages.
# (page title, what it does, body, page key)
PARENT = ("How We Design Training", "What all four layers are built on",
          "Philosophy, the five zones, zones by phase, and age guidance. Everything below is "
          "written in its vocabulary.", "parent")

STATE = {
    "parent": ("Parent", URL_HOW_WE_DESIGN_TRAINING),
    "phases": ("Layer 1", URL_HOW_WE_PLAN_TRAINING),
    "week": ("Layer 2", URL_TRAINING_WEEK),
    "session": ("Layer 3", URL_PRACTICE_SESSION),
    "individual": ("Layer 4", URL_INDIVIDUAL),
}

# Which layer pages exist today. All four are built.
PUBLISHED = {"phases", "week", "session", "individual"}


def layer_state(key, current=None):
    """Return (href, status) for a layer row. status: current | published | progress."""
    _, href = STATE[key]
    if key == current:
        return None, "current"
    if key in PUBLISHED:
        return href, "published"
    return None, "progress"


# ============================ ROW groups and pathways ============================
# ===================== Pathways and groups, 2026-27 =====================
# Rebuilt August 2026 from the 2026-27 Program Structure Executive Summary.
#
# WHAT CHANGED, and why old names must not survive anywhere:
#   TOPS 1 / TOPS 2      ->  TOPS 3x / TOPS 2x   (named for sessions, not rank)
#   AGD1 / AGD2          ->  AGD 14&U / AGD 12&U (named for age band)
#   LTCS                 ->  ROW Swim Academy
#   RSA Age Group        ->  retired, absorbed into Regional and Recreation
#   RSA Competitive      ->  retired, same
#   new                  ->  Recreation pathway, REC-AG 14&U and REC-AG 18&U
#   new                  ->  SD, PD1, PD2, PD3 and ND carry their age band
#
# SIX pathways now, not three streams plus two pre-stream pathways. The summary
# says "the pathways are unchanged: Foundation, Junior, Recreation, Regional,
# Provincial and National", so one word covers all six. "Stream" and "track"
# are both retired.
# (pathway, group, short, sessions, hours a week)
PROGRAMS = [
    ("Foundation",  "ROW Swim Academy",              "RSA",          "3 class options",
     "Saturday, 40 minutes each"),
    ("Junior",      "TOPS 2x",                       "TOPS 2x",      "2",  "2.0"),
    ("Junior",      "TOPS 3x",                       "TOPS 3x",      "3",  "3.0"),
    ("Junior",      "Junior Development 2",          "JD2",          "3",  "4.0"),
    ("Junior",      "Junior Development 1",          "JD1",          "4",  "5.5"),
    ("Recreation",  "REC-AG 14&U",                   "REC-AG 14&U",  "3",  "3.5"),
    ("Recreation",  "REC-AG 18&U",                   "REC-AG 18&U",  "5",  "7.5"),
    ("Regional",    "Age Group Development 12&U",    "AGD 12&U",     "4",  "5.5"),
    ("Regional",    "Age Group Development 14&U",    "AGD 14&U",     "5",  "7.5"),
    ("Regional",    "Senior Development 18&U",       "SD 18&U",      "6",  "9.0"),
    ("Provincial",  "Provincial Development 3 12&U", "PD3 12&U",     "5",  "7.5"),
    ("Provincial",  "Provincial Development 2 14&U", "PD2 14&U",     "6",  "9.0"),
    ("Provincial",  "Provincial Development 1 18&U", "PD1 18&U",     "7",  "12.0"),
    ("National",    "National Development 18&U",     "ND 18&U",      "8",  "14.0"),
]

PATHWAYS = ["Foundation", "Junior", "Recreation", "Regional", "Provincial", "National"]


def pathway(name):
    return [g for g in PROGRAMS if g[0] == name]


# Which meet a pathway peaks for. Only the last three have one, and that is
# correct rather than a gap.
PATHWAY_PEAKS = [
    ("Foundation",  "ROW Swim Academy",
     "None. Learning to swim, and learning to like it."),
    ("Junior",      "TOPS 2x, TOPS 3x, JD2, JD1",
     "They race to learn and practise skills."),
    ("Recreation",  "REC-AG 14&U, REC-AG 18&U",
     "None. Technique, fitness and a group to be part of."),
    ("Regional",    "AGD 12&U, AGD 14&U, SD 18&U",
     "Western Regional Championships"),
    ("Provincial",  "PD3 12&U, PD2 14&U, PD1 18&U",
     "OAG short course, OSC long course"),
    ("National",    "ND 18&U",
     "Swimming Canada Trials and Nationals"),
]

# Week structure follows sessions per week, not age band.
LOAD_BANDS = [
    ("1 to 3", "RSA, TOPS 2x, TOPS 3x, JD2, REC-AG 14&U"),
    ("4 to 5", "JD1, AGD 12&U, AGD 14&U, PD3 12&U, REC-AG 18&U"),
    ("6",      "SD 18&U, PD2 14&U"),
    ("7 to 8", "PD1 18&U, ND 18&U"),
]

# Zones and phases follow the &Under band. Competitive groups only: the
# Recreation pathway is not built around peaking or zone percentages, and how
# far the framework applies to it is an open question for the coaching staff.
AGE_BANDS = [
    ("10&U", "TOPS 2x, TOPS 3x"),
    ("12&U", "JD2, JD1, AGD 12&U, PD3 12&U"),
    ("14&U", "AGD 14&U, PD2 14&U"),
    ("18&U", "SD 18&U, PD1 18&U, ND 18&U"),
]

# Program pages. Slug matches the nav label, per rule 0. Replaces the older
# scheme where eight were Olympic city codenames (stars, london, barcelona,
# beijing, sydney, la1, paris, seoul) and four were descriptive.
#
# Ten pages, fourteen groups: TOPS, Junior Development, Age Group Development
# and Recreation each cover two groups.
PROGRAMS_TREE = f"{BASE}/page/programs"

PROGRAM_SLUGS = {
    "RSA":         "row-swim-academy",
    "TOPS 2x":     "tops",
    "TOPS 3x":     "tops",
    "JD2":         "junior-development",
    "JD1":         "junior-development",
    "REC-AG 14&U": "recreation",
    "REC-AG 18&U": "recreation",
    "AGD 12&U":    "age-group-development",
    "AGD 14&U":    "age-group-development",
    "SD 18&U":     "senior-development",
    "PD3 12&U":    "provincial-development-3",
    "PD2 14&U":    "provincial-development-2",
    "PD1 18&U":    "provincial-development-1",
    "ND 18&U":     "national-development",
}


def program_url(short):
    """Page for a group, by its short name. Never hard-code one in a page script."""
    return f"{PROGRAMS_TREE}/{PROGRAM_SLUGS[short]}"


# ===================== Program pages, 2026-27 =====================
# One page per group. Recreation is the single exception: one page carrying both
# REC-AG options, at the club's direction.
#
# Schedules are from ROW_2026-27_Group_Schedules_12h_v26, the current version.
# Every page prints DRAFT, NOT YET FINAL above its schedule.
#
# Lead coaches are as published in the 2026-27 Executive Summary, in the same
# abbreviated form. TBC where the summary names no one.
# (day, time, pool, lanes)
SCHEDULES = {
    "ND 18&U": [("Mon", "4:00-6:00 pm", "WLU deep end", "3"),
                ("Tue", "6:00-7:30 am", "WLU deep end", "3"),
                ("Tue", "4:00-6:00 pm", "WLU deep end", "3"),
                ("Wed", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                ("Wed", "4:00-6:00 pm", "WLU deep end", "3"),
                ("Thu", "4:00-5:30 pm", "WLU deep end", "3"),
                ("Fri", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                ("Sat", "6:00-8:00 am", "WLU deep end", "3")],
    "PD1 18&U": [("Mon", "4:00-6:00 pm", "WLU deep end", "3"),
                 ("Tue", "6:00-7:30 am", "WLU deep end", "3"),
                 ("Wed", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                 ("Wed", "4:00-6:00 pm", "WLU deep end", "3"),
                 ("Thu", "4:00-5:30 pm", "WLU deep end", "3"),
                 ("Fri", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                 ("Sat", "6:00-8:00 am", "WLU deep end", "3")],
    "PD2 14&U": [("Mon", "6:00-7:30 pm", "WLU deep end", "3"),
                 ("Tue", "4:30-6:00 pm", "WLU deep end", "3"),
                 ("Wed", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                 ("Thu", "4:30-6:00 pm", "WLU shallow end", "3"),
                 ("Fri", "6:00-7:30 am &middot; 50 m", "WLU deep end", "2"),
                 ("Sat", "6:30-8:00 am", "WLU shallow end", "3")],
    "PD3 12&U": [("Mon", "6:00-7:30 pm", "WLU deep end", "3"),
                 ("Tue", "4:30-6:00 pm", "WLU shallow end", "3"),
                 ("Thu", "4:30-6:00 pm", "WLU shallow end", "3"),
                 ("Fri", "4:30-6:00 pm", "WLU shallow end", "3"),
                 ("Sat", "6:30-8:00 am", "WLU shallow end", "3")],
    "SD 18&U": [("Mon", "6:00-7:30 am", "WLU deep end", "6"),
                ("Tue", "6:00-7:30 pm", "WLU deep end", "6"),
                ("Wed", "4:30-6:00 pm", "WLU shallow end", "6"),
                ("Thu", "6:00-7:30 am", "WLU deep end", "6"),
                ("Fri", "4:30-6:00 pm", "WLU deep end", "6"),
                ("Sat", "6:00-7:30 am", "Cameron Heights", "6")],
    "AGD 14&U": [("Mon", "6:00-7:30 pm", "Cameron Heights", "6"),
                 ("Wed", "6:00-7:30 pm", "WLU deep end", "6"),
                 ("Thu", "6:00-7:30 pm", "WLU shallow end", "6"),
                 ("Fri", "6:00-7:30 pm", "WLU deep end", "6"),
                 ("Sat", "8:00-9:30 am", "WLU deep end", "6")],
    "AGD 12&U": [("Mon", "4:30-6:00 pm", "Cameron Heights", "6"),
                 ("Wed", "6:00-7:30 pm", "WLU shallow end", "6"),
                 ("Fri", "6:00-7:30 pm", "WLU shallow end", "6"),
                 ("Sat", "9:30-10:30 am", "WLU deep end", "6")],
    "JD1": [("Mon", "6:30-7:30 pm", "WLU shallow end", "3"),
            ("Tue", "4:30-6:00 pm", "WLU shallow end", "3"),
            ("Thu", "6:30-8:00 pm", "WLU deep end", "3"),
            ("Sat", "8:00-9:30 am", "WLU shallow end", "3")],
    "JD2": [("Mon", "6:30-7:30 pm", "WLU shallow end", "3"),
            ("Thu", "6:30-8:00 pm", "WLU deep end", "3"),
            ("Sat", "8:00-9:30 am", "WLU shallow end", "3")],
    "RSA": [("Sat", "7:30-10:00 am", "Cameron Heights", "6")],
}

# Group size, worked out from the lanes on each schedule and the swimmers per
# lane in THE RULES WE APPLIED in the Executive Summary:
#   ND 4 to a lane, PD1 and SD 5, PD2 PD3 JD1 JD2 6, both AGD 5.8, TOPS 5,
#   REC-AG 4 or fewer. In the 50 m pool ND 6, PD1 7.5, PD2 9.
#
# Most come out as a single number because the rule is a whole number and the
# lane count does not change. Ranges appear only where the rule itself gives one:
# AGD averages 5.8 a lane, so lanes run at 5 or 6, and the REC-AG groups are
# capped rather than targeted.
# (size, how it is worked out)
GROUP_SIZE = {
    "ND 18&U":     ("12",        "3 lanes at 4 a lane. In the 50 m pool, 2 lanes at 6."),
    "PD1 18&U":    ("15",        "3 lanes at 5 a lane. In the 50 m pool, 2 lanes at 7.5."),
    "PD2 14&U":    ("18",        "3 lanes at 6 a lane. In the 50 m pool, 2 lanes at 9."),
    "PD3 12&U":    ("18",        "3 lanes at 6 a lane."),
    "SD 18&U":     ("30",        "6 lanes at 5 a lane."),
    "AGD 14&U":    ("30 to 36",  "6 lanes averaging 5.8 a lane, so lanes run at 5 or 6."),
    "AGD 12&U":    ("30 to 36",  "6 lanes averaging 5.8 a lane, so lanes run at 5 or 6."),
    "JD1":         ("18",        "3 lanes at 6 a lane."),
    "JD2":         ("18",        "3 lanes at 6 a lane."),
    "TOPS 3x":     ("15 an option", "3 lanes at 5 a lane, with a coach for every lane. "
                                    "30 across both options."),
    "TOPS 2x":     ("15 an option", "3 lanes at 5 a lane, with a coach for every lane. "
                                    "45 across all three options."),
    "Recreation":  ("up to 24 and up to 32",
                    "REC-AG 14&U is 6 lanes at 4 or fewer. REC-AG 18&U runs 5 lanes on Monday "
                    "and Friday and 8 from Tuesday to Thursday, at 4 or fewer."),
    "RSA":         ("30 a class, 90 in total",
                    "6 lanes at about 5 a lane, with a coach for every lane, across three "
                    "Saturday classes."),
}

# Groups offered in more than one schedule option. label -> rows.
OPTIONS = {
    "TOPS 3x": [("Option 1", [("Mon", "4:30-5:30 pm", "WLU shallow end", "3"),
                              ("Tue", "6:00-7:00 pm", "WLU shallow end", "3"),
                              ("Thu", "5:30-6:30 pm", "WLU deep end", "3")]),
                ("Option 2", [("Mon", "5:30-6:30 pm", "WLU shallow end", "3"),
                              ("Wed", "7:00-8:00 pm", "Cameron Heights", "3"),
                              ("Fri", "7:00-8:00 pm", "Cameron Heights", "3")])],
    "TOPS 2x": [("Option 1", [("Mon", "5:30-6:30 pm", "WLU shallow end", "3"),
                              ("Wed", "7:00-8:00 pm", "Cameron Heights", "3")]),
                ("Option 2", [("Tue", "6:00-7:00 pm", "WLU shallow end", "3"),
                              ("Fri", "7:00-8:00 pm", "Cameron Heights", "3")]),
                ("Option 3", [("Mon", "4:30-5:30 pm", "WLU shallow end", "3"),
                              ("Thu", "5:30-6:30 pm", "WLU deep end", "3")])],
    "Recreation": [("REC-AG 14&U &middot; 3 sessions, 3.5 hours a week",
                    [("Mon", "7:30-9:00 pm", "Cameron Heights", "6"),
                     ("Wed", "8:00-9:00 pm", "Cameron Heights", "6"),
                     ("Fri", "8:00-9:00 pm", "Cameron Heights", "6")]),
                   ("REC-AG 18&U &middot; 5 sessions, 7.5 hours a week, "
                    "attend the mornings that suit you",
                    [("Mon", "6:00-7:30 am", "Rec Complex", "5"),
                     ("Tue", "6:00-7:30 am", "Rec Complex", "8"),
                     ("Wed", "6:00-7:30 am", "Rec Complex", "8"),
                     ("Thu", "6:00-7:30 am", "Rec Complex", "8"),
                     ("Fri", "6:00-7:30 am", "Rec Complex", "5")])],
}

# (slug, H1, pathway, schedule key, lead coach, sessions, hours, blurb)
PROGRAM_PAGES = [
 ("row-swim-academy", "ROW Swim Academy", "Foundation", "RSA", "Chloe H",
  "3 class options", "40 minutes each",
  "Where a swimmer starts. A FUNdamentals program for younger swimmers who want a taste of "
  "competitive swimming through a club. The aim is strong technique and water skills that carry "
  "into our junior programs. Saturday mornings at Cameron Heights, with beginner, intermediate "
  "and advanced levels running together in every class."),
 ("tops-2x", "TOPS 2x", "Junior", "TOPS 2x", "Kaitlyn M", "2", "2.0",
  "A first taste of training as a group, twice a week. Three schedule options so families can "
  "pick what suits them. Every option runs three lanes, five swimmers to a lane, with a coach "
  "for every lane."),
 ("tops-3x", "TOPS 3x", "Junior", "TOPS 3x", "Kaitlyn M", "3", "3.0",
  "The same program as TOPS 2x with an extra session a week. Two schedule options. Every option "
  "runs three lanes, five swimmers to a lane, with a coach for every lane."),
 ("junior-development-2", "Junior Development 2", "Junior", "JD2", "Kaitlyn M", "3", "4.0",
  "Stroke technique, starts and turns, and a first look at racing strategy. JD2 trains alongside "
  "JD1 on Monday, Thursday and Saturday with three lanes each, so a swimmer ready to move up does "
  "not have to change everything at once. Swimmers race at local and regional meets."),
 ("junior-development-1", "Junior Development 1", "Junior", "JD1", "Kaitlyn M", "4", "5.5",
  "The step up from JD2, with a fourth session a week. Stroke technique, starts and turns, and "
  "racing strategy. JD1 and JD2 train alongside each other on Monday, Thursday and Saturday. "
  "Swimmers race at local, regional and provincial meets."),
 ("recreation", "Recreation", "Recreation", "Recreation", "TBC", "3 or 5", "3.5 or 7.5",
  "For swimmers who want to keep swimming without the competitive commitment. Technique, fitness, "
  "and a group to belong to. Two options: REC-AG 14&U trains three evenings a week at Cameron "
  "Heights, and REC-AG 18&U has five available mornings at the Rec Complex with swimmers "
  "attending the ones that suit them."),
 ("age-group-development-12u", "Age Group Development 12&U", "Regional", "AGD 12&U", "TBC",
  "4", "5.5",
  "The first competitive group, for swimmers around the 12&U band. Refining technique and "
  "training skills to compete at the regional level. Evenings only, with no weekday mornings, and "
  "its own lead coach."),
 ("age-group-development-14u", "Age Group Development 14&U", "Regional", "AGD 14&U", "TBC",
  "5", "7.5",
  "The step up from AGD 12&U, with a fifth session a week. Refining technique and training skills "
  "to compete at the regional and provincial level. Evenings only, with no weekday mornings, and "
  "its own lead coach."),
 ("senior-development", "Senior Development", "Regional", "SD 18&U", "Tyson M", "6", "9.0",
  "Refining technique and training habits to compete at the regional and provincial level, with "
  "dryland alongside the swimming. SD trains Saturday mornings at Cameron Heights, and its "
  "swimmers coach the ROW Swim Academy immediately afterwards."),
 ("provincial-development-3", "Provincial Development 3", "Provincial", "PD3 12&U", "Isabelle D",
  "5", "7.5",
  "Stroke technique, starts and turns, and racing strategy, with the goal of competing at the "
  "provincial level. Five sessions a week with no weekday mornings."),
 ("provincial-development-2", "Provincial Development 2", "Provincial", "PD2 14&U", "Tyson M",
  "6", "9.0",
  "Building on PD3 with more time in the water and more racing. Six sessions a week, including "
  "two weekday mornings and 50 metre training twice a week."),
 ("provincial-development-1", "Provincial Development 1", "Provincial", "PD1 18&U", "Ron F",
  "7", "12.0",
  "Stroke skill mastery, goal setting and racing strategy, aiming at Provincial and Canadian Age "
  "Group Championships. Seven sessions a week with three weekday mornings, one double day, and "
  "50 metre training twice a week."),
 ("national-development", "National Development", "National", "ND 18&U", "Ron F", "8", "14.0",
  "The top of the pathway, for swimmers aiming at the provincial, national and international "
  "level. Eight sessions a week, three weekday mornings, two double days, and 50 metre training "
  "twice a week."),
]


# Retired slugs, kept only so a redirect list can be written from them.
RETIRED_PROGRAM_SLUGS = {
    "stars": "row-swim-academy", "london": "tops", "barcelona": "junior-development",
    "beijing": "junior-development", "paris": "age-group-development",
    "seoul": "senior-development",
    "sydney": None,   # RSA Age Group, retired with no direct successor
    "la1": None,      # RSA Competitive, retired with no direct successor
}


# --- Deprecated aliases -------------------------------------------------
# These names predate the current page titles: PHASES was Training Phases,
# HOW_WE_TRAIN was How We Train, SWIM_MATH was ROW Swimming Math. Every one is
# a retired name still in daily use, which is the same drift the page copy had.
# Kept so older build scripts still run. Delete once they are all rebuilt.
URL_PHASES_COACH = URL_HOW_WE_PLAN_TRAINING
URL_HOW_WE_TRAIN = URL_HOW_WE_DESIGN_TRAINING
URL_DEVELOP = URL_HOW_WE_DEVELOP_SWIMMERS
URL_SWIM_MATH = URL_GOAL_SETTING_TOOL
URL_PHASES_FAMILY = URL_HOW_WE_PLAN_TRAINING_FAMILY
