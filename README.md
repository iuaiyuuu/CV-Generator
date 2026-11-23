# CV Creator

**English** · [Bahasa Indonesia](README.id.md)

An AI-driven CV generator built from **Markdown rules**, not code. You keep your own data in folders; the AI reads the rules and writes a CV **tailored to each job description** — truthfully.

Works with any AI coding agent that reads `AGENTS.md` (Claude Code, Codex, Cursor, Copilot, …).

## How it works

```
profile/                info/                   jobs/<job>.md
who you are             your proof              what the employer wants
     │                       │                       │
     └───────────────────────┼───────────────────────┘
                             ▼
                    rules/ + workflows/
                             │
                             ▼
              output/<date>_<company>_<role>/
                ├─ cv.md              tailored CV
                └─ match-report.md    fit, gaps, advice
```

## Quick start

1. **Clone** this repo.
2. **Fill your data** (private, git-ignored). **The easiest way: just tell your AI.** Describe your projects, your story, and your skills in your own words, in any language and any order. The AI asks a few short follow-up questions and writes the entries for you using the templates (`workflows/interview.md`). For example:

   > I want to tell you about my projects, my story, and my skills. Interview me and write the entries into this repo.

   Nothing is saved until you confirm, and anything you did not say is marked `[TODO]`, never guessed. Prefer to write the files yourself? Copy the templates:
   - `profile/` — copy each `*.template.md` to a real file (`personal.md`, `education.md`, `experience.md`).
   - `info/CERTIFICATE`, `info/SKILL`, `info/PROJECT`, `info/RESEARCH` — drop your files in, then ask the AI to convert them to entries (`workflows/add-entry.md`).
   - `info/PROJECT/<name>.md` — one file per project (copy `project.template.md`). Tell each project in this order: **title → problem → solution → your part → stack → results**. For instance: title *Sales Dashboard*; problem "the cooperative's managers guessed which products sold well"; solution "a dashboard of revenue by category and month, built from cleaned sales data"; your part "solo: cleaned the data, wrote the queries, built and deployed it". See [`info/PROJECT/README.md`](info/PROJECT/README.md).
   - `profile/story.md` — **your story and personality** (copy `story.template.md`). Write what pulls you, how you work, and what you want next, the way you would tell a friend. Each trait needs one real example; a trait without an example is not used. For instance:

     ```
     I'm the kind of person who gets curious when something doesn't add up, and I really
     like solving problems because every problem is a small mystery.
     For example, my dashboard project was already graded, but the totals still didn't match
     the paper records. I kept hunting for duplicates until they matched, then sent the
     corrected numbers to the managers. They used it in their monthly meeting.
     (proof: info/PROJECT/sales-dashboard.md)
     ```

     The AI turns this into the **reason and direction** of your summary, never into bare words like "hardworking". See the full fictional example in [`examples/sample-user/profile/story.md`](examples/sample-user/profile/story.md).
3. **Add a job**: paste the **full** job description **either into the chat with your AI** (it saves it to `jobs/<company>_<role>.md` for you) **or into that file yourself** (use `jobs/job.template.md`). A link or job title alone is not enough: the AI can only tailor to text it can read. For a program or fellowship, include the deadline and eligibility lines too.
4. **Ask your AI agent**, for example:
   > Generate a CV for `jobs/acme_data-analyst.md` using `workflows/generate-cv.md`.
5. Review `output/…/cv.md` and `match-report.md`. Answer any `[TODO]` questions.
6. Export to PDF: `pip install reportlab`, then `python tools/md2pdf.py output/<run>/cv.md` (see [`tools/README.md`](tools/README.md)).

Want to see the result first? Open [`examples/sample-user/`](examples/sample-user/): fictional data, one job, the generated CV, its PDF, and the match report.

## What the rules enforce

| Rule | Guarantee |
|---|---|
| [01 Truthfulness](rules/01-truthfulness.md) | No invented facts, numbers, or skills. Gaps are flagged, not hidden. |
| [02 Job tailoring](rules/02-job-tailoring.md) | The AI analyzes the job description, matches it to your evidence, and adapts summary, skills, order, and wording. |
| [03 Writing style](rules/03-writing-style.md) | Strong, specific bullets; no buzzwords; consistent language and length. |
| [04 ATS formatting](rules/04-ats-formatting.md) | Single-column, standard headings, parser-friendly. |
| [05 Privacy](rules/05-privacy.md) | Personal data never committed; sensitive fields omitted by default. |

## Repo layout

```
AGENTS.md          entry point for AI agents (CLAUDE.md points to it)
rules/             hard rules the AI must follow
workflows/         step-by-step procedures
templates/         CV layout, match report
tools/             helper scripts (md2pdf.py)
examples/          fictional sample user, job, CV, and PDF
profile/           YOUR identity (private)
info/              YOUR evidence: CERTIFICATE, SKILL, PROJECT, RESEARCH (private)
jobs/              job descriptions (private)
output/            generated CVs and reports (private)
```

## Privacy

`profile/`, `info/`, `jobs/`, and `output/` are git-ignored; only READMEs and `*.template.md` are tracked. Before pushing a fork, run `git status` and confirm none of your personal files are staged. Never use `git add -f` on those folders: it bypasses the protection and uploads your personal data.

## Contributing

Improvements to rules, workflows, templates, and examples are welcome — especially:

- Region-specific conventions (CV norms differ by country)
- Role-specific tailoring guides (e.g. `rules/roles/software-engineer.md`)
- Translations of the rules
- New workflows (cover letter, LinkedIn summary, interview prep)

Never include real personal data in a contribution. Use fictional data in `examples/`.

## License

[MIT](LICENSE). The license covers the rules, workflows, templates, and tools in this repo. Your own CV data in `profile/`, `info/`, `jobs/`, and `output/` stays yours and is never part of the repo.
