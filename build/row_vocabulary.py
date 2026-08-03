"""ROW controlled vocabulary — one word per idea, and a checker that enforces it.

The framework's whole value is that a swimmer moving from 10&U to 18&U hears one
consistent story. That only holds if every page uses the same word for the same
thing. This file is the list, and the check that catches drift before it ships.

Run it over any built fragment:

    python3 row_vocabulary.py /mnt/user-data/outputs/row_<page>_embed.html

It strips the markup first and checks only the visible copy, so CSS keywords
(color:, center) are never flagged. Two levels:

    FIX    a retired or off-vocabulary word. Always wrong.
    CHECK  legitimate in some contexts. A person decides.
"""

import html as _html
import re
import sys

FIX = "FIX"
CHECK = "CHECK"


# (preferred, [patterns], why, level, times allowed)
RULES = [
    # --- one word per idea -------------------------------------------------
    ("volume",
     [r"high metres", r"metres drop", r"total metres", r"total work",
      r"training stress", r"mileage", r"yardage"],
     "Volume is the word. Four synonyms for it appeared on one page.", FIX, 0),

    ("intensity",
     [r"harder work", r"work rate"],
     "Intensity is the word.", FIX, 0),

    # "Quality" is out. It was doing three different jobs across the five pages,
    # which is how it spread:
    #   the dial            "volume drops, quality holds"     -> intensity
    #   a type of session   "never two quality days"          -> hard session / hard day
    #   an attribute        "the one quality that cannot be   -> reword
    #                        rushed later"
    # "Hard" is not a new word: Layer 2 already says "hard and easy days" and
    # Layer 1 says "after every hard block".
    ("intensity (the dial) / hard session (the type)",
     [r"\bqualit(?:y|ies)\b"],
     "Intensity is the dial on a session. A hard session or a hard day is the "
     "type. Neither is 'quality'.", FIX, 0),

    ("Peaking",
     [r"\btapers?\b", r"\btapered\b", r"\btapering\b"],
     "Peaking is the phase name. One gloss is allowed, in the Peaking row.",
     FIX, 1),

    ("peak meet",
     [r"designated peak meet", r"target meet", r"named meet", r"championship meet"],
     "Peak meet is the term.", FIX, 0),

    ("race through",
     [r"low.priority meet", r"minor meet", r"\bB meet\b", r"lesser meet"],
     "A meet that is not a peak is one we race through.", FIX, 0),

    ("practice session",
     [r"\bworkouts?\b"],
     "Layer 3 is The Practice Session. Workout names an activity, not a thing.",
     FIX, 0),

    # "Senior" is only wrong when it means the age band. Senior Development is a
    # group, and senior coaches, senior officials and senior leadership are all
    # ordinary English. A rule that flags those gets ignored.
    ("18&U",
     [r"\bseniors?\b(?!\s+(?:Development|coach|official|position|leadership|"
      r"staff|management))"],
     "18&U is the age band. Senior Development, senior coach and senior official "
     "are all fine. A senior swimmer is not: that is an 18&U swimmer, or a\n     named group.", CHECK, 0),

    ("block / cycle",
     [r"\bmesocycle\b", r"\bmacrocycle\b", r"\bmicrocycle\b"],
     "A block is one run of a phase. A cycle ends in Transition.", FIX, 0),

    # DECISION, August 2026: pathway is the word. The 2026-27 Executive Summary
    # says "the pathways are unchanged: Foundation, Junior, Recreation,
    # Regional, Provincial and National", so all six are pathways.
    # "Stream" and "Track" were both in use for the same idea, 28 times across
    # five live pages, and Programs Overview alone used four labels:
    # Junior Development Stream, Junior Comp Stream, Development Track,
    # Provincial Track.
    # "Track" only counts as a pathway label when it follows a pathway name.
    # "Track height, not just times" is the verb and is fine.
    ("pathway",
     [r"\bstreams?\b",
      r"\b(?:Development|Provincial|Regional|National|Comp|Competitive|Senior|Junior)\s+Track\b",
      r"\bTracks\b"],
     "Pathway is the word for all six. Stream and Track are both retired.",
     FIX, 0),

    ("the assessment link in layers_common.py",
     [r"team-registration\?reg_id", r"New Swimmer Tryouts",
      r"Schedule a Swimmer Assessment"],
     "One assessment link, one name. Use URL_ASSESSMENT from layers_common.py "
     "and call it booking an assessment.", FIX, 0),

    # Never send a family to a coach mid-session. A coach on deck is coaching.
    ("before or after practice",
     [r"(?:ask|talk to|speak to|catch)[^.]{0,40}\bon deck\b",
      r"\bon deck\b[^.]{0,25}(?:if you have|with any question)"],
     "Point families at before or after a practice, never at a coach on deck.",
     FIX, 0),

    # The club's promise, settled August 2026. Use PROMISE and MISSION from
    # layers_common.py rather than retyping either one.
    ("PROMISE and MISSION in layers_common.py",
     [r"will cherish long after", r"experiences in competitive swimming"],
     "Carry, not cherish. Through, not in. Both sentences live in "
     "layers_common.py so they cannot drift again.", FIX, 0),

    # DECISION, August 2026: group names carry a number, not a session count or
    # an age band. TOPS 3x became TOPS 1 and TOPS 2x became TOPS 2, because the
    # lower number is the higher level, matching JD1/JD2 and PD1/2/3. AGD 14&U
    # became AGD 1 and AGD 12&U became AGD 2. The two Recreation groups are named
    # for when they train: REC AM in the mornings, REC PM in the evenings.
    ("the group name in layers_common.py",
     [r"TOPS ?[23]x", r"AGD ?1[24]&U", r"REC-AG",
      r"\b(?:SD|PD[123]|ND) ?1[248]&U\b",
      r"(?:Senior|Provincial|National) Development ?[123]? ?1[248]&U"],
     "A group name is a name. No age band in it: SD, PD1, PD2, PD3, ND, and the "
     "same for the long forms. Age ranges belong in the detail on the page.",
     FIX, 0),

    # --- retired page and product names ------------------------------------
    ("How We Design Training", [r"How We Train\b"],
     "Retired title. Collided with the hub.", FIX, 0),
    ("How We Plan Training", [r"Training Phases"],
     "Retired title.", FIX, 0),
    ("Coaching at ROW", [r"How ROW Coaches"],
     "Retired title.", FIX, 0),
    ("Goal Setting Tool", [r"ROW Swimming Math", r"swim math", r"swimming math"],
     "Rejected working title. The repo keeps the old name; the product does not.",
     FIX, 0),
    ("The Practice Session", [r"Workout Design"], "Retired title.", FIX, 0),
    ("The Individual Swimmer", [r"Individuali[sz]ing Training"],
     "Retired title, and it reopened the -ising spelling question.", FIX, 0),
    ("", [r"Coaching Application", r"\bApplication\b"],
     "On a swim club site this reads as a job posting.", CHECK, 0),

    # --- zones -------------------------------------------------------------
    ("Zone 3",
     [r"(?<!Aerobic )\bthreshold\b", r"aerobic build", r"\bBlue zone\b"],
     "Blue merged into Red. Bare 'threshold' puts a retired zone name back.",
     CHECK, 0),

    # DECISION, August 2026: the zone number is the only reference.
    #   Zone 3   in prose and tables
    #   Z3       in set notation and on a lane card
    # The colour survives in one place only, the Descriptor column on How We
    # Design Training. Used anywhere else it is a second name for the same thing,
    # which is what this file exists to stop.
    ("Zone 3 in prose, Z3 on a board",
     [r"\b(?:White|Pink|Red|Purple|Green)\s+(?:sets?|work|days?|zone|touch|swim|metres)\b",
      r"\b(?:top|bottom|end)\s+of\s+(?:White|Pink|Red|Purple|Green)\b",
      r"\b(?:in|into|at)\s+(?:White|Pink|Red|Purple|Green)\b",
      r"\b(?:WHITE|PINK|RED|PURPLE|GREEN)\b"],
     "The zone number is the reference. The colour is a descriptor and belongs "
     "only in the descriptor column on How We Design Training.", FIX, 0),

    ("the zone number", [r"\bPk\b", r"\bPu\b", r"\bW\s*/\s*Pk"],
     "Pk, Pu and W are not zone names.", FIX, 0),

    # --- Canadian English (decisions record, section 10) --------------------
    ("-ize",
     [r"\borganis", r"\bindividualis", r"\bspecialis(?:e|ed|es|ing|ation)\b", r"\brecognis", r"\bemphasis(?:e|ing|ed)\b"],
     "-ize and -ization, not -ise.", FIX, 0),
    ("-our / -re",
     [r"\bcolors?\b", r"\bbehaviors?\b", r"\bfavor", r"\bmeters?\b", r"\bcenters?\b"],
     "colour, behaviour, favour, metre, centre. CSS keywords are code and are "
     "stripped before this check runs.", FIX, 0),
    ("specialty", [r"specialit(?:y|ies)"], "specialty / specialties.", FIX, 0),
    ("program", [r"\bprogramme"], "program, not programme.", FIX, 0),
    ("towards", [r"\btoward\b"], "towards, not toward.", FIX, 0),
    ("practice (noun) / practise (verb)",
     [r"\bpractic(?:e|ing)\b(?=\s+(?:the|your|it|at))"],
     "Practise is the verb. 'Practise the target pace', not 'practice'.",
     CHECK, 0),

    # Audience wording is not a plain vocabulary rule: BUILDING and EASING are
    # correct on a family page and wrong on a coach page. See check_audience(),
    # which works in both directions.
]


BLOCK_END = re.compile(
    r"</(?:div|p|h[1-6]|td|th|li|tr|caption|blockquote|pre)>|<br\s*/?>", re.I)


# ---------------------------------------------------------------------------
# Audience guard
#
# Some lines are true, useful, and correct on a coach page, and land badly on a
# family page. The decisions record (section 8) names the failure mode: principle
# 6 originally read "Long-term development beats this season", which sets this
# season against the future and reads badly to a family paying for this season.
#
# Second confirmed instance, August 2026: principle 7, "Every year they need us
# less". On a coach page it is the goal. To a family paying fees it reads as a
# plan to sell them less coaching.
#
# Checked only when a build declares audience="family".
# (pattern, why it must not cross over)
# The reverse of COACH_ONLY: family wording that has strayed onto a coach page.
# BUILDING and EASING are correct on a family page and wrong on a coach one, so
# this cannot be a plain vocabulary rule. It depends on who the page is for.
# DECISION, August 2026: families and coaches use ONE vocabulary. The earlier
# rule gave families BUILDING, EASING and STARTING in place of LOAD, UNLOAD and
# ENTRY. Dropped, because a swimmer comes home saying the group is in
# Accumulation and a parent reading a different word for it is worse off.
FAMILY_ONLY = [
    (r"Available now|Coming soon",
     "Family wording for build status. Coach pages use Live, In draft and Planned."),
]


COACH_ONLY = [
    (r"need us (?:a little )?less", "Reads to a family as a plan to sell less coaching."),
    (r"working ourselves out of a job", "Same failure mode, older wording."),
    (r"your call as lead coach", "Addresses the coach, not the family."),
    (r"\bprescrib", "The coach version says what to prescribe. The family version "
                    "says what you will see."),
    (r"tell families", "Instruction to a coach about families, printed for families."),
    (r"\bIn draft\b",
     "Build status is for the coach hub, not for families."),
]


def check_audience(markup, audience):
    """Flag wording that has crossed between audiences, in either direction.

    Some words are not right or wrong on their own, only right or wrong for who
    is reading. BUILDING belongs on a family page and not on a coach one.
    "Every year they need us less" is the reverse. So this cannot be a plain
    vocabulary rule; the build has to say who the page is for.
    """
    rules = {"family": COACH_ONLY, "coach": FAMILY_ONLY}.get(audience)
    if not rules:
        return []
    text = visible_text(markup)
    out = []
    for pat, why in rules:
        # Same convention as the vocabulary rules: a capital in the pattern
        # means match case. The family badges are all-caps, so BUILDING is
        # caught while "Building the engine" in ordinary prose is not.
        flags = 0 if re.search(r"[A-Z]", pat) else re.IGNORECASE
        hits = re.findall(pat, text, flags=flags)
        if hits:
            out.append((FIX, f"wording that does not belong on a {audience} page",
                        ", ".join(sorted({str(h) for h in hits})), len(hits), why))
    return out


def visible_text(markup):
    """Strip tags and entities so only the copy a reader sees is checked.

    Block ends become a marker first, so a rule cannot match across two
    unrelated cells or paragraphs. Without this, a table cell ending "a
    practice" followed by one starting "The session template" read as the
    phrase "practice the", which is a spelling rule, and reported a fault
    that was not on the page.
    """
    text = BLOCK_END.sub(" \u00b6 ", markup)
    text = re.sub(r"<[^>]+>", " ", text)
    text = _html.unescape(text)
    return re.sub(r"\s+", " ", text)


def check(markup, name=""):
    """Return a list of (level, preferred, found, count, why)."""
    text = visible_text(markup)
    findings = []
    for preferred, patterns, why, level, allowed in RULES:
        hits = []
        for pat in patterns:
            # A pattern written with a capital is a proper noun: match case.
            flags = 0 if re.search(r'[A-Z]', pat) else re.IGNORECASE
            hits += re.findall(pat, text, flags=flags)
        if len(hits) > allowed:
            seen = sorted({h if isinstance(h, str) else h[0] for h in hits})
            findings.append((level, preferred, ", ".join(seen), len(hits), why))
    return findings


def report(path):
    markup = open(path, encoding="utf-8").read()
    findings = check(markup, path)
    print(f"\n{path}")
    if not findings:
        print("  clean")
        return 0
    for level in (FIX, CHECK):
        rows = [f for f in findings if f[0] == level]
        if not rows:
            continue
        print(f"  {level}")
        for _, preferred, found, count, why in rows:
            use = f" -> use {preferred}" if preferred else ""
            print(f"    {found}  x{count}{use}")
            print(f"        {why}")
    return len([f for f in findings if f[0] == FIX])


if __name__ == "__main__":
    paths = sys.argv[1:]
    if not paths:
        print(__doc__)
        sys.exit(0)
    sys.exit(min(sum(report(p) for p in paths), 1))
