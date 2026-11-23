# Rule 01 — Truthfulness

A CV is a factual document. A tailored CV is the same facts, selected and phrased for a reader — never different facts.

## MUST

- Use only facts found in `profile/` and `info/`.
- Keep employers, job titles, institutions, degrees, dates, and credential names **exactly** as recorded.
- Keep numbers exactly as recorded. Do not round up, convert ranges to their upper bound, or add "+".
- Keep the user's real level of involvement. "Contributed to", "assisted", "led", "owned" are not interchangeable — use the one recorded.
- Mention a skill/tool only if it appears in a recorded entry (project, certificate, experience, or `info/SKILL/`).
- Include a certificate only if it is recorded with issuer and date (or marked `date: unknown`).

## MUST NOT

- Invent metrics ("improved performance by 40%") when no figure is recorded.
- Add job-description keywords the user has no evidence for, just to pass a keyword filter.
- Upgrade scope: a class project is not "production", a course is not "experience", a team result is not a personal result.
- Fill gaps in employment dates to hide a break.
- Copy phrases from the job description into the CV as claims about the user.

## When data is missing

1. **Do not guess.** Leave a visible placeholder: `[TODO: add <what is missing>]`.
2. Ask the user one concise question listing everything missing at once.
3. If the user cannot provide it, omit that detail — do not substitute a plausible value.

## Informal work and missing titles

Many people work without a contract or an official title (freelance, verbal agreements, remote part-time). That is legitimate experience. Handle it honestly:

- Do not invent a formal title. Use a plain **descriptor** of the real work and arrangement, e.g. "Freelance Full-Stack Developer (Remote)", and record in `profile/` that it is a descriptor.
- Do not upgrade the arrangement: freelance/part-time/verbal-agreement work is never written as "Full-time" or "Employee".
- Dates, employer name, and the work done must still be real. Ask whether the employer can confirm them if a background check is likely.
- Never put compensation in the CV.

## Publication and thesis status

Use the exact status, and update it when it changes:

- Written the way the user's records say: `In preparation` · `Submitted` · `Under revision` · `Accepted (to appear Month YYYY)` · `Published` · for theses `Experiments complete, awaiting defense` or `Defended`.
- Never promote a status ("accepted" → "published", "awaiting defense" → "master's degree"). A paper accepted but not yet issued is "Accepted", with the planned month only if the user confirmed it.
- State the user's author position only as recorded (first author, sole author, co-author).

## Self-described expertise

"Expert" is a claim that needs evidence. If the user calls themselves an expert but the data shows only informal or limited evidence, write the specific capability ("PC hardware assembly and troubleshooting") instead of the word "expert", and tell the user what evidence would justify it.

## Skill honesty levels

When listing skills, use only levels supported by evidence:

| Level | Evidence required |
|---|---|
| Used in a project / role | A recorded entry that names the skill |
| Certified | A recorded certificate covering the skill |
| Familiar / learning | Course or self-study recorded, no project |

Put "familiar/learning" items in a clearly separate line or omit them. Never mix them with proven skills.

## Final check (run before delivering)

For every line in the CV, be able to answer: **"Which file in `profile/` or `info/` proves this?"**
If you cannot point to a file, remove or rewrite the line.
