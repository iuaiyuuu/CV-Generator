# Workflow — Generate a CV

**Trigger:** the user asks for a CV for a specific job ("buatkan CV untuk lowongan ini", "make a CV for this role").

**Inputs:** a job description (pasted text, a file in `jobs/`, or a URL), plus the user's `profile/` and `info/`.
**Outputs:** in `output/<YYYY-MM-DD>_<company>_<role>/`:
- `cv.md` — the tailored CV
- `match-report.md` — fit, evidence table, gaps, suggestions

## Steps

### 1. Load rules
Read all files in `rules/`. They override any habit or default.

### 2. Get the job description
- If pasted in chat, save it to `jobs/<company>_<role>.md` using `jobs/job.template.md`.
- If only a URL/title is given, try to read the page. If it cannot be read (login wall, blocked, empty), ask the user to paste the full text into the chat. Don't guess requirements.

### 2b. Pre-checks on the posting (before any writing)

- **Date and deadline:** compare the deadline with today's date. If it has passed, tell the user first, then continue only if they still want the CV.
- **Posting type:** is it a normal job posting, or something else (fellowship, residency, grant, scholarship, internship program)? Non-standard postings follow `rules/02-job-tailoring.md` "Non-standard postings".
- **Seniority fit:** compare the level the posting asks for (stated title, "established", "staff-level", years) with the user's real level. If the user is clearly below it, say so in the match report; never close the gap with wording.

### 3. Load the user's data
- Read every file in `profile/` (personal, education, experience, and `story.md`). Use `story.md` for the **reason and direction** of the Summary and for choosing what to emphasize; never copy its trait adjectives into the CV, and use a story only if it has a proof file.
- Read `info/SKILL/`, `info/PROJECT/`, `info/RESEARCH/`, `info/CERTIFICATE/`.
- For certificates that exist only as PDF/image with no structured entry, run `workflows/add-entry.md` first (or ask the user to confirm extracted details).

### 4. Check for blockers
If essential data is missing (name, contact, at least one of education/experience/projects), ask **one** consolidated question, or offer to run `workflows/interview.md` so the user can simply tell you. Don't continue with invented data.

### 5. Analyze and match
Follow `rules/02-job-tailoring.md` Steps 1–3. Produce the match table (must-have → evidence → strength).

### 6. Draft the CV
- Use `templates/cv.template.md` as the layout.
- Apply `rules/02` Step 4 (rewrite), `rules/03` (style), `rules/04` (ATS).
- Choose the section order that best presents the strongest evidence for this JD.

### 7. Self-check (mandatory)
Run each check; fix issues before delivering.

- [ ] **Truth:** every line traces to a file in `profile/` or `info/` (rule 01)
- [ ] **No invented numbers or skills**
- [ ] **Tailoring:** summary, skills order, and bullets reflect this JD; all must-haves with evidence are visible
- [ ] **Summary:** passes the swap test and the link test (`rules/03` "Summary section"); written from the top must-haves
- [ ] **Layout:** standard headings only ("Organizations", not "Leadership"); every entry follows the entry shape; header block in the fixed order (`rules/04` "Layout contract")
- [ ] **Gaps not claimed:** nothing in the CV claims a Gap requirement
- [ ] **Style:** bullet formula, no buzzwords, consistent dates and tense (rule 03)
- [ ] **ATS:** single column, standard headings (rule 04)
- [ ] **Length:** within target
- [ ] **Privacy:** no omitted-by-default fields (rule 05)
- [ ] **Placeholders:** any remaining `[TODO: ...]` is listed to the user

### 8. Write the match report
Use `templates/match-report.template.md`. Include verdict, evidence table, gaps with honest suggestions, and the list of `[TODO]` items.

### 9. Deliver
Reply with: path to the output folder, a 3-line summary of how the CV was tailored, the top gaps, and any questions. Do not paste the entire CV in chat unless asked.

If the user requests PDF/DOCX, convert from `cv.md` without altering content and confirm the text is selectable.
