"""ROW stylesheet check — every class a page uses must exist in the stylesheet.

The shared stylesheet lives in one field and the page lives in another. Nothing
warns you when they disagree: a class that is not defined simply renders as
nothing, and the page looks almost right. That is how row-stage-head and
row-stage-lead sat unstyled on three published pages without anyone noticing.

Run it over the build scripts, the built pages, or both:

    python3 row_css_check.py row_stylesheet.css build_*.py ../pages/*.html

Two levels:

    FIX     a class is used and the stylesheet does not define it. The page
            will render unstyled in that spot. Always wrong.
    CHECK   a class is defined and nothing uses it. Usually harmless, sometimes
            a rename that left the old rule behind. A person decides.

Exit code is 1 if anything is at FIX, so it can gate a build.
"""

import re
import sys

FIX = "FIX"
CHECK = "CHECK"

# Only ROW's own classes. Anything the CMS or SportsEngine supplies is not ours
# to define and must not be reported.
OURS = re.compile(r"^row-")

# class="..." in HTML, and class=\"...\" inside a Python f-string.
USE = re.compile(r'class=\\?["\']([^"\'\\]+)')

# A rule head in the stylesheet: .row-thing, including inside a media query.
DEFINE = re.compile(r"\.(row-[a-z0-9-]+)")


def classes_used(paths):
    """Return {class: {file, ...}} for every ROW class referenced."""
    found = {}
    for path in paths:
        text = open(path, encoding="utf-8").read()
        for group in USE.findall(text):
            for name in group.split():
                if OURS.match(name):
                    found.setdefault(name, set()).add(path.split("/")[-1])
    return found


def classes_defined(stylesheet):
    text = open(stylesheet, encoding="utf-8").read()
    # Strip comments first. The header explains the row-stage bug by name, and
    # without this the checker reads that explanation as a definition.
    text = re.sub(r"/\*.*?\*/", " ", text, flags=re.S)
    return set(DEFINE.findall(text))


def report(stylesheet, paths):
    defined = classes_defined(stylesheet)
    used = classes_used(paths)

    missing = sorted(set(used) - defined)
    unused = sorted(defined - set(used))

    print(f"\n{stylesheet}  ({len(defined)} classes defined, "
          f"{len(used)} referenced across {len(paths)} file(s))")

    if not missing and not unused:
        print("  clean")
        return 0

    if missing:
        print(f"  {FIX}")
        for name in missing:
            where = sorted(used[name])
            shown = ", ".join(where[:3])
            more = f" and {len(where) - 3} more" if len(where) > 3 else ""
            print(f"    {name}  used in {len(where)} file(s): {shown}{more}")
            print("        Not in the stylesheet. Renders unstyled.")

    if unused:
        print(f"  {CHECK}")
        for name in unused:
            print(f"    {name}")
            print("        Defined and never used. Check it is not a rename "
                  "that left the old rule behind.")

    return len(missing)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(0)
    sys.exit(1 if report(args[0], args[1:]) else 0)
