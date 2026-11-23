# Rule 04 — ATS-Friendly Formatting and Layout

Applicant Tracking Systems (ATS) parse the CV into fields. If the structure is unusual, parts of the CV get lost. A human reader also needs a regular, predictable layout. Keep it plain **and consistent**.

## Structure

- **Single column.** No tables for layout, no text boxes, no multi-column sections, no sidebars.
- **No** icons, images, skill-bar charts, rating stars, or graphics in place of text. (A profile photo only if the target country/employer expects it and the user asks.)
- Contact info in the document body, **not** in a header/footer.
- Use **only** these standard section headings, spelled exactly like this (shown in ALL CAPS in PDF/DOCX exports):

  `Summary` · `Research` · `Experience` · `Projects` · `Education` · `Skills` · `Certifications` · `Organizations` · `Publications` · `Awards` · `Languages`

- **`Organizations`** is the heading for memberships and roles in student, community, and professional organizations, including leadership roles (chairman, division head, committee). Do **not** use "Leadership", "Activities", "Extracurricular" or other variants.
- Standard bullets (`-` in Markdown, `•` in exports). No custom symbols.

## Section order (default)

Sections are grouped as **who you are → what you did → what you can do**: identity and credentials first, then work and activities, then the skills summary at the end.

For **students, fresh graduates, people with an ongoing degree, and research or academic applications**:

1. Header (name, headline, contact)
2. Summary
3. Research *(only if there is a thesis or paper; include it for research programs)*
4. Education
5. Experience
6. Organizations
7. Projects
8. Skills
9. Certifications

For **experienced professionals** (about 5+ years of relevant work), Education moves below Experience:

Header → Summary → Experience → Projects → Research *(if any)* → Education → Skills → Certifications → Organizations

Papers and theses: with one paper plus a thesis, list both as entries under **Research** (peer-reviewed or accepted work first). With two or more papers, use a separate **Publications** section placed right after Research. Always show the status and the author position on the entry's second line.

Rules for the order:

- **Education always comes before Organizations and Projects** for the student/research order; never put Education below Projects there.
- **Organizations** sits right after Experience (they are the same kind of content: roles you held), not at the very bottom, in the student/research order.
- **Skills and Certifications** close the CV in both orders.
- Within these orders you may move **one** section up when it best proves the job's must-haves (see `02-job-tailoring.md`), but do not otherwise reshuffle. Ask the user when unsure which order fits.

## Layout contract (the CV must look regular)

Every CV follows the same shapes. Do not invent a new shape for one section.

### Header block (always this order, nothing else)

```
# Full Name
**Headline**                       <- optional, the user's own wording
Focus A · Focus B · Focus C        <- optional, max 3
City, Country | email | phone
linkedin... | github... | portfolio
```

Contact order is fixed: location, email, phone, then links (LinkedIn, GitHub, portfolio). Two lines maximum.

### Entry shape (used by Experience, Research, Projects, Education, Organizations)

```
### Title — Organization              <- line 1: what + where
Mon YYYY – Mon YYYY | Location | link  <- line 2 (one line): dates first, then optional details
- bullet
- bullet
```

- Line 1 is always `Title — Organization`. Line 2 always starts with the dates; if there are no dates (e.g. an undated project), line 2 starts with the link or is omitted. Never put dates inside line 1 or inside a bullet.
- Line 2 holds **all** metadata (location, link, GPA, supervisor, status). No metadata in separate loose lines.
- Bullets only describe the work. Education coursework or honors may be one bullet.
- Every entry in every section uses this same shape.

### Short list sections

- **Skills:** one line per category: `**Category:** item, item, item`. Same category labels style across CVs; no sub-bullets.
- **Certifications:** one line each: `Name — Issuer, Mon YYYY`. Group minor ones on a single `Also:` line.
- **Organizations:** use the entry shape if you have bullets; otherwise a single line `Role — Organization, YYYY – YYYY`. Do not mix both in one section.

### Spacing and typography (PDF/DOCX)

- Page A4 (or Letter for US). Margins 1.5–2 cm, the same on all sides.
- Body 10–11 pt, one font family (Arial, Calibri, Helvetica). Name 16–20 pt, section headings 11–12 pt bold ALL CAPS with a thin rule under, entry title 10–11 pt bold.
- Dates on line 2 may be right-aligned in exports **only** if the text stays selectable and in reading order. If unsure, keep them left-aligned.
- One consistent gap before each section heading, one smaller consistent gap before each entry. No blank lines inside an entry.
- Never leave a section heading or an entry title as the last line of a page: keep it with its first bullet.
- Do not mix bullet characters, dash types, or date formats within one CV.

## Text

- Real text, not images of text.
- Spell out acronyms once if the JD uses the long form: "Continuous Integration/Continuous Deployment (CI/CD)".
- Links: show the readable URL (`github.com/user/repo`), not just "click here".

## File output

- Primary output: Markdown (`cv.md`) in `output/<date>_<company>_<role>/`.
- When the user asks for PDF, run `python tools/md2pdf.py <cv.md>` (see `tools/README.md`). Convert **without changing content**, then open the pages to verify the layout contract: selectable text, no orphan headings, page count within target. For DOCX, apply the same contract with your own tooling.
- File name: `<Full-Name>_CV_<Role>.pdf` (e.g. `Jane-Doe_CV_Data-Analyst.pdf`). No spaces or special characters.

## Check before delivering

- [ ] Single column, no tables/graphics
- [ ] Only the standard headings above; "Organizations", not "Leadership"
- [ ] Section order matches the student/research or the experienced order (Education above Projects; Organizations right after Experience; Skills and Certifications last)
- [ ] Every entry follows the entry shape (title line, then dates/meta line)
- [ ] Header block in the fixed order
- [ ] Consistent date format, bullets, dash types
- [ ] No orphan headings at the bottom of a page
- [ ] Fits target page length
