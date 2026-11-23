# Workflow — Import an Existing CV

**Trigger:** the user already has a CV (PDF/DOCX/text) and wants its content turned into structured entries.

An old CV is a **claim**, not proof. It is also often out of date or inflated. Import carefully.

## Steps

1. **Extract the text** (see `workflows/add-entry.md` "Reading files"). Verify special characters.
2. **Split into entries** using the templates: identity → `profile/personal.md`; education → `profile/education.md`; jobs and organizations → `profile/experience.md`; projects → `info/PROJECT/`; research → `info/RESEARCH/`; skills → `info/SKILL/`; certificates → `info/CERTIFICATE/`.
3. **Compare with what the user has already told you** (chat, existing entries). List every conflict: different dates, titles, employers, degree names, numbers.
4. **Do not merge conflicting claims.** Put them in an "Unconfirmed items from the earlier CV" section in `profile/experience.md` marked *do not use until confirmed*, and ask the user once, listing all of them.
5. **Respect what the user rejects.** If the user dislikes a description, keep their new wording and do not copy the old claims into the entry (record them as excluded or not approved if the user says they are true).
6. **Record the source** of every imported entry (`source: <file name>`).
7. **After the user answers**, update the entries: confirmed → normal; excluded → marked excluded; not approved → marked not approved.

## Common conflicts to look for

- Employment gaps and overlapping dates
- Titles that sound more formal than the real arrangement
- Businesses that are aspirations, not operating (e.g. "Founder" of a planned company)
- Metrics without a definition or date
- Degree names translated differently (e.g. an Indonesian M.Kom written as "M.Sc.")
- Skills with no project or certificate behind them
