#!/usr/bin/env python3
"""Convert a CV written in Markdown into an ATS-friendly PDF.

Follows rules/04-ats-formatting.md ("Layout contract"):
- single column, real selectable text, one font family
- headings in ALL CAPS with a thin rule, entry title bold, then a meta line, then bullets
- a section heading is always kept together with its first entry (no orphan headings)
- dates such as "Jan 2026" or "2024 - 2025" never break across lines

Usage:
    python tools/md2pdf.py path/to/cv.md [path/to/output.pdf]

If the output path is omitted, the PDF is written next to the input file.
Requires: pip install reportlab
The converter does not change the content; it only lays out the Markdown it is given.
Supported Markdown: "# Name", "## Section", "### Entry title", "- bullet", plain lines,
**bold** inline, and <!-- comments --> (ignored).
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, LETTER
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate
except ImportError:
    sys.exit("reportlab is required: pip install reportlab")

FONT, BOLD = "Helvetica", "Helvetica-Bold"   # standard fonts: no embedding needed, always selectable
BODY = 10
LEAD = 12.6
GAP_SECTION = 9    # space before each section heading
GAP_ENTRY = 5      # space before each entry title
GAP_BULLET = 1.2
NBSP = " "


def make_styles():
    return {
        "name": ParagraphStyle("name", fontName=BOLD, fontSize=19, leading=23, spaceAfter=2),
        "head": ParagraphStyle("head", fontName=BOLD, fontSize=BODY + 0.5, leading=LEAD),
        "hdr": ParagraphStyle("hdr", fontName=FONT, fontSize=BODY, leading=LEAD),
        "para": ParagraphStyle("para", fontName=FONT, fontSize=BODY, leading=LEAD),
        "h2": ParagraphStyle("h2", fontName=BOLD, fontSize=11.5, leading=14, spaceBefore=GAP_SECTION, spaceAfter=1),
        "h3": ParagraphStyle("h3", fontName=BOLD, fontSize=BODY, leading=LEAD, spaceBefore=GAP_ENTRY),
        "meta": ParagraphStyle("meta", fontName=FONT, fontSize=BODY, leading=LEAD, spaceAfter=1.5),
        "bul": ParagraphStyle("bul", fontName=FONT, fontSize=BODY, leading=LEAD, leftIndent=11,
                              bulletIndent=1.5, spaceAfter=GAP_BULLET),
    }


def keep_dates_together(text):
    text = re.sub(r"\b([A-Z][a-z]{2}) (\d{4})\b", lambda m: m.group(1) + NBSP + m.group(2), text)
    text = re.sub(r"(\d{4}|Present) – (\d{4}|Present|Expected)",
                  lambda m: m.group(1) + NBSP + "–" + NBSP + m.group(2), text)
    text = re.sub(r"– (\d{4})\b", lambda m: "–" + NBSP + m.group(1), text)
    return text


def inline(text):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escape(keep_dates_together(text)))


def parse(path):
    items, in_comment = [], False
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if "<!--" in line and "-->" not in line:
            in_comment = True
            continue
        if in_comment:
            in_comment = "-->" not in line
            continue
        if not line.strip() or line.strip().startswith("<!--"):
            continue
        if line.startswith("# "):
            items.append(("name", line[2:]))
        elif line.startswith("## "):
            items.append(("h2", line[3:]))
        elif line.startswith("### "):
            items.append(("h3", line[4:]))
        elif line.startswith("- "):
            items.append(("bul", line[2:]))
        else:
            items.append(("text", line.strip()))
    return items


def build(items, st):
    story, i = [], 0

    def bullet(t):
        return Paragraph(inline(t), st["bul"], bulletText="•")

    def entry_group(i):
        """h3 + optional meta line + first bullet, kept together. Returns (flowables, next_i)."""
        group = [Paragraph(inline(items[i][1]), st["h3"])]
        i += 1
        if i < len(items) and items[i][0] == "text":
            group.append(Paragraph(inline(items[i][1]), st["meta"]))
            i += 1
        if i < len(items) and items[i][0] == "bul":
            group.append(bullet(items[i][1]))
            i += 1
        return group, i

    while i < len(items):
        kind, text = items[i]
        if kind == "name":
            story.append(Paragraph(inline(text), st["name"]))
            i += 1
            # header lines (headline, focus areas, contact): bold only where the Markdown says **bold**
            while i < len(items) and items[i][0] == "text":
                story.append(Paragraph(inline(items[i][1]), st["hdr"]))
                i += 1
        elif kind == "h2":
            group = [Paragraph(inline(text).upper(), st["h2"]),
                     HRFlowable(width="100%", thickness=0.6, color=colors.black, spaceBefore=0, spaceAfter=3)]
            i += 1
            if i < len(items):
                k2, t2 = items[i]
                if k2 == "text":
                    group.append(Paragraph(inline(t2), st["para"]))
                    i += 1
                elif k2 == "bul":
                    group.append(bullet(t2))
                    i += 1
                elif k2 == "h3":
                    sub, i = entry_group(i)
                    group.extend(sub)
            story.append(KeepTogether(group))
        elif kind == "h3":
            group, i = entry_group(i)
            story.append(KeepTogether(group))
        elif kind == "bul":
            story.append(bullet(text))
            i += 1
        else:
            story.append(Paragraph(inline(text), st["para"]))
            i += 1
    return story


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        sys.exit(__doc__)
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    items = parse(src)
    name = next((t for k, t in items if k == "name"), "CV")
    page = LETTER if "--letter" in sys.argv else A4
    doc = SimpleDocTemplate(
        str(dst), pagesize=page,
        leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm,
        title=f"{name} - CV", author=name,
    )
    doc.build(build(items, make_styles()))
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
