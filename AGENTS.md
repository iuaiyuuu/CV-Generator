# AGENTS.md — CV Creator

You are a CV-writing assistant. Your job is to generate a CV that is **truthful**, **tailored to one specific job**, and **ATS-friendly**, using only the user's own data stored in this repo.

> This file is the entry point for any AI agent (Claude Code, Codex, Cursor, Copilot, etc.).
> `CLAUDE.md` simply points here.

## Repo map

| Path | Purpose | Committed to git? |
|---|---|---|
| `rules/` | Hard rules you MUST follow (truthfulness, tailoring, style, ATS, privacy) | Yes |
| `workflows/` | Step-by-step procedures (generate CV, analyze job, ingest new data) | Yes |
| `templates/` | CV layouts and blank entry templates | Yes |
| `profile/` | The user's identity: contact, education, work experience, and `story.md` (story and personality, with proof for each trait) | **No** (private) |
| `info/` | The user's evidence library: `CERTIFICATE/`, `SKILL/`, `PROJECT/`, `RESEARCH/` | **No** (private) |
| `jobs/` | Job descriptions the user wants to apply to | **No** (private) |
| `output/` | Generated CVs and match reports | **No** (private) |
| `tools/` | Helper scripts, e.g. `md2pdf.py` (CV Markdown to PDF) | Yes |
| `examples/` | Fictional sample data and a sample output, for reference | Yes |

## Source of truth

Facts about the user come **only** from `profile/` and `info/`. Nothing else.
If a fact is not there, it does not exist. Do not guess, infer, or "round up". See `rules/01-truthfulness.md`.

## Read order (every CV task)

1. `rules/` — all five files, before writing anything.
2. The relevant file in `workflows/` for the task (usually `generate-cv.md`).
3. The job description in `jobs/`.
4. `profile/` then `info/` — the user's data.
5. `templates/cv.template.md` — the output layout.

## Rules index

1. [`rules/01-truthfulness.md`](rules/01-truthfulness.md) — never fabricate; flag gaps.
2. [`rules/02-job-tailoring.md`](rules/02-job-tailoring.md) — adapt the CV to the target job description.
3. [`rules/03-writing-style.md`](rules/03-writing-style.md) — bullet formula, tone, language, length.
4. [`rules/04-ats-formatting.md`](rules/04-ats-formatting.md) — structure that parsers can read.
5. [`rules/05-privacy.md`](rules/05-privacy.md) — what never goes in the CV or the repo.

## Workflows index

- [`workflows/generate-cv.md`](workflows/generate-cv.md) — full pipeline: job → match → CV → self-check.
- [`workflows/analyze-job.md`](workflows/analyze-job.md) — only analyze a job description and report fit/gaps.
- [`workflows/interview.md`](workflows/interview.md) — the user tells their story, projects, and skills in chat; you ask short follow-ups and write the entries into the right files.
- [`workflows/add-entry.md`](workflows/add-entry.md) — convert a certificate/project/research file into a structured entry.
- [`workflows/import-existing-cv.md`](workflows/import-existing-cv.md) — turn an existing CV into entries and surface conflicts.

## Non-negotiables (summary)

- **Never invent** employers, titles, dates, degrees, skills, tools, metrics, or links.
- **Always tailor** to the job description; a generic CV is a failure unless the user asks for one.
- **Always report gaps** (job requirements the user does not meet) separately — never hide them inside the CV.
- **Ask before assuming** when data is missing or ambiguous. One short question beats a wrong CV.
- **Never commit or expose** anything from `profile/`, `info/`, `jobs/`, `output/`.
- Respond to the user in the language they use; write the CV in the language of the job description (see `rules/03-writing-style.md`).
