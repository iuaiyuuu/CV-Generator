# info/

Your **evidence library**: the proof behind every claim on your CV. **Private — git-ignored.** Only README and `*.template.md` files are tracked.

| Folder | What goes in | Template |
|---|---|---|
| `CERTIFICATE/` | Certificates, badges, course completions (PDF/JPG) + one `.md` entry per item | `certificate.template.md` |
| `SKILL/` | Skill groups with level and evidence | `skill.template.md` |
| `PROJECT/` | Personal, academic, freelance, open-source projects | `project.template.md` |
| `RESEARCH/` | Thesis, papers, publications, lab work | `research.template.md` |

## How it works

1. Drop raw files (PDF, image, notes) into the matching folder.
2. Ask the AI to run `workflows/add-entry.md` — it creates a structured `.md` entry per item and asks you to confirm.
3. When you request a CV, the AI reads these entries and selects the ones that match the job.

Original files stay as proof; the `.md` entries are what the AI reads best.
