# Rule 02 — Job Tailoring

Every CV is written for **one** job description. Before writing, the AI must read the job description (JD) in `jobs/` and adapt the CV to it — within the limits of `01-truthfulness.md`.

If no JD is given, ask for one. Only produce a generic CV if the user explicitly asks.

## Step 1 — Analyze the JD

Extract and write down (in the match report, not the CV):

| Item | What to capture |
|---|---|
| Role & seniority | Title, level (intern / junior / mid / senior / lead), years asked |
| **Must-have** requirements | Anything marked required, "must", "minimum", or repeated several times |
| **Nice-to-have** | "Plus", "preferred", "bonus" |
| Hard skills / tools | Languages, frameworks, platforms, methods, certifications |
| Soft skills / behaviors | Collaboration, ownership, communication, etc. — as the JD words them |
| Domain / industry | Fintech, health, security, data, etc. |
| Responsibilities | What the person will actually do day to day |
| Company signals | Mission, values, tech stack, size, culture hints |
| Language & region | Language the JD is written in; country-specific CV conventions |
| Keywords | Exact terms the JD uses (e.g. "CI/CD" vs "continuous integration") |

## Step 2 — Match against the user's data

Build a match table: each must-have / nice-to-have → the user's **evidence** (file + entry) → strength.

| Strength | Meaning |
|---|---|
| Strong | Direct, recent, demonstrated in a project/role/certificate |
| Partial | Related or older experience, or only certified/studied |
| Gap | No evidence |

## Step 3 — Select and rank content

- **Include** entries that support must-haves first, then nice-to-haves.
- **Cut or shrink** entries irrelevant to this JD, even if impressive. Relevance beats completeness.
- **Order** sections and bullets so the strongest match to the JD is seen first (top third of page 1).
- Within each entry, order bullets by relevance to the JD, not chronology.
- Certificates: list only those relevant to the JD, unless there are few. Group the rest on one line or omit.
- Projects/research: pick the 2–4 closest to the JD's domain and stack.

## Step 4 — Rewrite for the JD

- **Summary**: write it **after** the match table, from the top two must-haves (or research areas) and the user's evidence for them, following `03-writing-style.md` "Summary section" (identity + proof for must-have 1, evidence for must-have 2 in the job's terms, direction in the job's domain). It must pass the swap test and the link test. Rewrite it for every job.
- **Terminology**: if the user's recorded fact and the JD's term mean the same thing, use the JD's term (e.g. record says "automated deployment", JD says "CI/CD" → use "CI/CD" only if the recorded work genuinely is CI/CD).
- **Skills section**: put JD-relevant skills first, in the JD's wording. Drop skills irrelevant to the role if the list is long.
- **Bullets**: emphasize the outcome and technology the JD cares about. Same facts, different emphasis.
- **Keywords**: each important JD keyword should appear naturally **where the evidence supports it**. Do not stuff, repeat, or hide keywords.

## Step 5 — Gap handling

For every Gap or Partial must-have:

1. **Never** add it to the CV as a claim.
2. List it in the match report with a short, honest suggestion: adjacent evidence to highlight, something to learn, or a cover-letter angle.
3. If the gap is a hard blocker (e.g. required license, required years), tell the user plainly before they apply.

## Step 6 — Fit verdict

End the match report with a short verdict: **strong / moderate / weak fit**, the top 3 selling points, and the top 3 risks. Be candid — the user benefits more from honesty than from flattery.

## Non-standard postings

Fellowships, residencies, grants, scholarships, and internship programs often have no requirement list. Treat the text as a job description anyway:

- Turn the **"who we are looking for"** statements into must-haves, and the **listed research or work areas** into nice-to-haves.
- Check **seniority fit** first (e.g. "professor, technical founder, or staff-level engineer"). If the user is below it, say so plainly in the verdict and suggest a better-matched route if the posting names one (e.g. a fellows program).
- Note logistics that affect eligibility: location, duration, remote allowance, deadline.
- For research programs, include Research right after the Summary and use the student/research section order in `04-ats-formatting.md`.

## Approved and excluded facts

The user may mark true facts as **excluded** (e.g. an unclear metric) or **not approved** (true but not wanted on the CV), or ask to keep part of a project private (e.g. an undisclosed stack). Such markers live in the entry itself. Obey them in every CV; never reintroduce an excluded fact because it would match the job.

## Don't

- Don't reuse a previous tailored CV without re-running Steps 1–4.
- Don't tailor by fabricating a company-specific story the user never told you.
- Don't mention the company's name in the CV body (only in file names and the cover letter) unless the user asks.
