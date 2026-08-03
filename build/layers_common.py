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
