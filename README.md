# ROW website content

Pages for rowswimming.ca, which runs on SportsEngine Motion.

| Folder | What is in it |
|---|---|
| `originals/` | The 56 live pages as they were in August 2026, before any changes. The backup. |
| `pages/` | Rebuilt pages, ready to paste into the CMS. |
| `build/` | The Python that generates them, plus the shared stylesheet. |

## Pasting a page into the site

Two fields, not one:

1. `build/row_stylesheet.css` goes into the page's **custom CSS** field. The same
   stylesheet on every page; it never changes per page.
2. The matching file from `pages/` goes into the **content editor**, via the
   Source button.

## Changing a page

Edit the build script, not the page. A page edited in the CMS loses its change
the next time it is built, and the site starts drifting apart again.

    cd build
    python3 build_<page>.py
    python3 row_vocabulary.py ../pages/row_<page>_embed.html
    python3 row_style_check.py ../pages/row_<page>_embed.html

The two checks catch wording that has drifted from the club's agreed terms, and
styling that has drifted from the template.

## Not in this repo

`ROW_Coaching_Framework_Decisions.md` holds internal material and lives in Claude
project files instead.
