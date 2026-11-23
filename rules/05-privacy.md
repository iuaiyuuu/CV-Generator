# Rule 05 — Privacy

This repo is **public**. People clone it and put their own data in `profile/` and `info/`. Those folders are git-ignored, and the AI must keep it that way.

## In the repo

- **Never** stage, commit, or push anything from `profile/`, `info/`, `jobs/`, or `output/` (except their `README.md` and `*.template.md` files).
- **Never** edit `.gitignore` to loosen those rules.
- Before any `git add` / commit, check `git status` and make sure no personal file is staged. If one is, stop and tell the user.
- Examples in `examples/` must use **fictional** data only. Never copy a real user's data into an example.
- Don't paste a user's personal data into issues, PR descriptions, or commit messages.

## In the CV

Include only what helps the application. By default **omit**:

- National ID numbers (NIK, SSN, passport), tax numbers
- Full home address (city/country is enough)
- Date of birth, age, marital status, religion, ethnicity, number of children
- Photo — unless the user asks or the country/employer norm requires it
- Salary history or expectations — unless the JD requires it
- References' details — use "References available on request" only if the user wants it
- Social profiles that are unprofessional or irrelevant

Always allowed (if the user provides them): name, professional email, phone, city/country, LinkedIn, GitHub, portfolio.

If a JD or local convention explicitly requires an omitted field (e.g. some regions expect a photo or date of birth), **ask the user** before including it.

## In conversation

- Treat everything in `profile/` and `info/` as private. Don't send it to external services, tools, or URLs unless the user explicitly asks.
- When reading certificates (PDF/image), extract only the fields needed for the CV (name of credential, issuer, date, credential ID/URL). Don't copy unrelated personal data from the document.
- Redact or skip data about third parties (supervisors, colleagues) unless needed and the user approves.
