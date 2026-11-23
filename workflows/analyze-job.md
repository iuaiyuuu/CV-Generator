# Workflow — Analyze a Job (no CV yet)

**Trigger:** the user wants to know if a job fits, or what to improve, before generating a CV.

**Output:** `output/<YYYY-MM-DD>_<company>_<role>/match-report.md` only.

## Steps

1. Read `rules/01-truthfulness.md` and `rules/02-job-tailoring.md`.
2. Get the full job description text (save to `jobs/`; ask the user if only a link/title is given).
3. Load the user's `profile/` and `info/`.
4. Run `rules/02` Steps 1, 2, 5, 6: analyze, match, handle gaps, give a verdict.
5. Write the report using `templates/match-report.template.md`.
6. In chat, give a short summary: verdict, top 3 strengths, top 3 gaps, and whether to proceed to `generate-cv.md`.

## Quality bar

- Be candid. A "weak fit" verdict with clear reasons is more useful than an inflated one.
- Gap suggestions must be realistic (what the user can learn or highlight), not a way to bluff.
