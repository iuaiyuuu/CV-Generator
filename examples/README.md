# examples/

**Everything here is fictional.** Any resemblance to a real person is a coincidence. Never put real personal data in this folder.

## sample-user/

A complete run of the workflow for a fictional user, in the same folder layout you would use yourself:

| File | What it shows |
|---|---|
| [`profile/`](sample-user/profile/) | A filled-in identity: personal, education, experience, and [`story.md`](sample-user/profile/story.md) (story and personality, each trait with one real example) |
| [`info/PROJECT/sales-dashboard.md`](sample-user/info/PROJECT/sales-dashboard.md) | One evidence entry, with real numbers and honest gaps |
| [`jobs/acme_junior-data-analyst.md`](sample-user/jobs/acme_junior-data-analyst.md) | The job description the CV is written for |
| [`output/2025-01-15_acme_junior-data-analyst/cv.md`](sample-user/output/2025-01-15_acme_junior-data-analyst/cv.md) | The tailored CV (Markdown) |
| [`output/2025-01-15_acme_junior-data-analyst/Jane-Doe_CV_Junior-Data-Analyst.pdf`](sample-user/output/2025-01-15_acme_junior-data-analyst/Jane-Doe_CV_Junior-Data-Analyst.pdf) | The PDF made with `tools/md2pdf.py` |
| [`output/2025-01-15_acme_junior-data-analyst/match-report.md`](sample-user/output/2025-01-15_acme_junior-data-analyst/match-report.md) | Fit, evidence table, gaps, honest advice |

## What to notice

- The summary is written from the job's top requirements; it would not fit another job.
- Docker and cloud are **not** on the CV: no evidence, and the job does not need them.
- A skill the user is only learning sits on its own line, apart from proven skills.
- The match report names a real gap (SQL) and gives a realistic suggestion instead of hiding it.
