# tools/

Small helper scripts. They only lay out or check what you already wrote; they never invent content.

## md2pdf.py — Markdown CV to PDF

Turns `output/<run>/cv.md` into an ATS-friendly PDF that follows the layout contract in [`rules/04-ats-formatting.md`](../rules/04-ats-formatting.md): single column, selectable text, consistent entry shape, no orphan headings, dates that never split across lines.

```powershell
pip install reportlab
python tools/md2pdf.py output/2026-01-15_acme_data-analyst/cv.md
```

- Output: a `.pdf` next to the input, or give a second argument for the path.
- Add `--letter` for US Letter paper (default is A4).
- Name the final file `<Full-Name>_CV_<Role>.pdf` (see rule 04).

The AI agent should run this when you ask for a PDF, then check the result: open the pages and confirm there is no heading stranded at the bottom of a page and the page count fits the target.

Supported Markdown: `# Name`, `## Section`, `### Entry title`, `- bullet`, plain lines, `**bold**`, and `<!-- comments -->`. Fonts are Helvetica (a standard PDF font, so text stays selectable and ATS-readable). Characters outside Latin-1, such as Chinese or Arabic, are not supported by this basic converter.
