# Workflow — Add or Convert an Entry

**Trigger:** the user adds raw material (certificate PDF/image, project description, paper, notes) and wants it stored as a structured entry the AI can use.

> No file to convert? If the user would rather just talk, use `workflows/interview.md`.

## Where entries go

| Material | Folder | Template |
|---|---|---|
| Certificate / badge / course completion | `info/CERTIFICATE/` | `certificate.template.md` |
| Skill group / tool proficiency | `info/SKILL/` | `skill.template.md` |
| Project (personal, academic, freelance, open source) | `info/PROJECT/` | `project.template.md` |
| Research / thesis / paper / publication | `info/RESEARCH/` | `research.template.md` |
| Identity, education, work experience | `profile/` | `*.template.md` in `profile/` |

## Steps

1. **Read the source file** (PDF, image, notes). Extract only the fields in the template (see `rules/05-privacy.md`).
2. **Create a new `.md` entry** next to the source, named `<slug>.md` (lowercase, hyphens), copying the matching template.
3. **Fill fields from the source only.** If a field is not visible in the source, write `unknown` — do not infer.
4. **Show the user the entry** and ask them to confirm or correct, especially dates, credential IDs, and results.
5. **Record evidence:** set `source:` to the original file name so every claim stays traceable.
6. **Ask for the facts a CV needs but the file does not contain.** For a project, make sure the entry answers, in this order: **problem** (who had it, why it mattered), **solution** (what was built), **my part** (what the user personally did, solo or team), **tech stack**, and **results** (real numbers with an "as of" date). Ask only for what is missing, all in one message.

## Reading files

- Images (JPG/PNG): open them directly and read the text.
- PDFs: if the PDF viewer fails (e.g. `pdftoppm` is missing), extract text with `pdftotext -layout file.pdf -`. For long links that wrap across lines, also run it without `-layout`. Check special characters (e.g. `×`) by encoding (`-enc UTF-8`) before trusting them.
- Public profiles (Credly, Google Skills, GitHub, portfolio): read the page text and record the source URL and the date read.
- Pages that need a login (e.g. LinkedIn): do not sign in for the user; ask them to paste the text.

## Notes

- Keep the original files (PDF/JPG) where they are; the `.md` entry is the AI-readable layer.
- One entry = one item. Don't merge several certificates into one file.
- Never add facts the user did not confirm.
