# Rule 03 — Writing Style

## Language

- Write the CV in the **language of the job description**. If the JD is bilingual or unclear, ask the user.
- Reply to the user in the language they are using in chat.
- Don't mix languages inside one CV, except for proper nouns, tool names, and official credential titles.

## Bullet formula

Each bullet = **Action verb + what you did + how / with what + result (only if recorded)**.

> Built a REST API with FastAPI and PostgreSQL that serves 3 internal dashboards. *(result only if recorded)*

Rules:

- Start with a strong past-tense verb (present tense for the current role). Vary verbs; don't start two adjacent bullets with the same word.
- One idea per bullet. 1–2 lines max (about 25 words).
- Name the concrete tool, method, or scope ("with Docker and GitHub Actions"), not vague nouns ("various technologies").
- Include a number **only** when it is recorded in the user's data. No number is better than an invented one.
- Bullets per entry: 2–4 for the most relevant, 1–2 for older or less relevant.

## Numbers that change

Metrics that keep growing (users, visits, records) must carry an "as of" month: "37,874 recorded visits as of Nov 2026". Always say **what** is counted. Never merge figures that measure different things into one claim.

## Tone

- Professional, specific, plain. No first-person pronouns ("I", "my"); no full-sentence storytelling.
- Avoid empty buzzwords: *passionate, hardworking, team player, results-driven, dynamic, go-getter, synergy, think outside the box.* Show with evidence instead.
- Avoid unexplained abbreviations unless the JD itself uses them.
- No humor, emojis, or decorative symbols.

## Summary section

The summary is the most job-specific part of the CV. It must be **written from the job description**, not from the user's general story.

- 3–4 sentences, **40–80 words** (3–5 lines). Longer only if each added phrase passes the link test. Three parts in this order:
  1. **Identity + proof:** who the user is (their preferred headline if set) with the single strongest piece of evidence that answers the job's **top must-have**.
  2. **Second match:** a second piece of evidence answering the **next must-have or research/work area** in the job description, using the job's own terms (only where the evidence supports it).
  3. **Direction:** what the user wants to work on in **this** role's domain, in the job's words (not "seeking new challenges"). If the job asks for motivation, add the user's own **reason** (their words from `profile/story.md`), not only a goal.
- Show traits through evidence, never as bare adjectives ("curious", "committed", "passionate"). A trait phrase is allowed only when the same sentence carries the proof.
- Name the role type or domain from the job description (e.g. "empirical AI research", "junior data analysis"). Never name the company.
- Numbers only if recorded, with their "as of" date.
- **Swap test:** if the summary could be pasted unchanged into a CV for a different job, rewrite it.
- **Link test:** every phrase should map to (a) a requirement in the job description and (b) an entry in `profile/` or `info/`. A phrase with only one of the two is deleted or reworded.
- Rewritten for every job (see `02-job-tailoring.md`). No claims that are not backed by an entry.

Weak: "Independent researcher and developer who is passionate about technology and looking for new challenges."
Better (for a research-program posting): "Independent researcher with a master's thesis that tests a theory-only algorithm against brute-force optima, and the sole developer of a live system with built-in evidence checks. Aiming to apply this verification habit to empirical AI research on scalable oversight."

## Tense and formatting consistency

- Past tense for finished work, present for current.
- Dates: one format throughout (`MMM YYYY – MMM YYYY`, e.g. `Jan 2024 – Aug 2024`; `Present` for ongoing).
- Consistent punctuation: either end all bullets with a period or none.
- Spell out technology names correctly (`JavaScript`, `PostgreSQL`, `GitHub`, `Node.js`).

## Length

| Situation | Target |
|---|---|
| Student / fresh graduate / < 5 years experience | 1 page |
| 5–10 years | 1–2 pages |
| 10+ years or academic CV | 2 pages (academic may be longer, only if the user asks) |

If content overflows, cut by relevance (see `02-job-tailoring.md`) — never by shrinking fonts below 10 pt or margins below 1.5 cm.

## Before/after examples

| Weak | Better |
|---|---|
| Responsible for making a website | Built a responsive company-profile website with React and Tailwind CSS |
| Worked with data | Cleaned and analyzed 12k-row sales dataset in Python (pandas) to find top-selling categories *(only if the size/result is recorded)* |
| Hardworking and passionate team player | *(delete — replace with evidence in bullets)* |
