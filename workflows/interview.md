# Workflow — Interview: "Just tell me about yourself"

**Trigger:** the user wants to tell their story in chat instead of filling templates ("I want to tell you about my project", "interview me", "here is my story"), or the repo has no data yet.

**Goal:** the user talks freely, in any language and in any order. You ask short follow-up questions, then **write the entries into the right files using the repo's templates**. The user never has to open a template.

## Principles

1. **Let them talk first.** Start with one open question and let the answer run. Do not hand them a form.
2. **Never invent.** Write only what the user said. If something is missing, write `[TODO: ...]` or ask. Never fill gaps with plausible facts.
3. **Ask little, in one batch.** After they talk, ask only what is missing, at most 5 questions per message, short and concrete. Ask for the facts a CV needs: role, scope, tools, real numbers, dates.
4. **Mirror their language** in chat. Write the entries in English unless the user prefers otherwise (the AI translates their words faithfully; keep original quotes where useful).
5. **Show before you save.** After writing, show a short summary of each entry and ask them to confirm or correct, especially dates, numbers, and titles.
6. **Respect what they hold back.** If the user wants part of a project private (e.g. a technology) or rejects a claim, record it in the entry's "Not to claim" section and obey it in every CV.
7. **Separate story from proof.** A trait ("I finish what I start") is only usable with one real example and a proof file. Ask for the example; if there is no proof yet, mark it unverified.
8. **No sensitive identifiers.** Never ask for ID numbers, passwords, or similar (see `rules/05-privacy.md`).

## Where each thing goes

| The user talks about | Write to | Template |
|---|---|---|
| Name, contact, links, languages, target roles | `profile/personal.md` | `profile/personal.template.md` |
| Schools, degrees, thesis | `profile/education.md` | `profile/education.template.md` |
| Jobs, internships, organizations | `profile/experience.md` | `profile/experience.template.md` |
| Personality, motivation, how they work, what they want next | `profile/story.md` | `profile/story.template.md` |
| A project (problem, solution, their part) | `info/PROJECT/<slug>.md` | `info/PROJECT/project.template.md` |
| A thesis, paper, publication | `info/RESEARCH/<slug>.md` | `info/RESEARCH/research.template.md` |
| Skills and tools | `info/SKILL/<slug>.md` | `info/SKILL/skill.template.md` |
| Certificates (files) | `info/CERTIFICATE/` | use `workflows/add-entry.md` |

## Steps

### 1. Open with one question per topic

Pick the topic the user brings up. If they have no preference, go in this order: projects → story → skills → experience and education.

| Topic | Opening question |
|---|---|
| Project | "Tell me about a project you are proud of. What was the problem, what did you build, and what was your part?" |
| Story | "What kind of problems pull you in, and why? Tell me about a time you were stuck or something went wrong." If the user is unsure how to start, offer a sentence starter: "I'm the kind of person who ... when ..., and I really like ... because ..." |
| Skills | "What can you actually do with your best tools? Where did you use them?" |
| Experience | "Where have you worked or volunteered, when, and what did you do day to day?" |

### 2. Listen, then restate in 2–3 lines

Reflect back what you understood ("So the problem was X, you built Y, and you did Z alone. Right?"). This catches misunderstandings before anything is written.

### 3. Ask only what is missing

Use the checklist for the topic. Ask all gaps in one message.

- **Project:** problem (who, why it mattered) · solution (what it does now) · the user's own part (solo or team) · tech stack actually used · real numbers (volume, users, speed) with an "as of" date · dates · anything they do not want named.
- **Story:** one real example per trait (situation, what they did, how they know it worked) · a failure or mistake and what they did · what they want next and why · what they do not want to claim.
- **Skill:** what they can do with it · a project, job, or certificate that proves it · honest level (used in work, used in a project, certified, only learning).
- **Experience:** title or descriptor, organization, dates, kind of arrangement (employee, freelance, internship, volunteer) · what they did · real results.

### 4. Write the entries

Copy the matching template, fill it from what the user said, and mark every unknown as `[TODO: ...]`. Record the source: `source: told by the user in chat on <date>`.

For `profile/story.md`, **keep the user's own voice**: first person, natural sentences, their wording (translated faithfully if needed), with the proof file in brackets after each story. Do not turn it into bullet points or polish it into marketing language.

### 5. Show a short summary and ask to confirm

One or two lines per entry, plus the list of `[TODO]` items. Ask: "Is this correct? Anything I should not mention?"

### 6. Claim check

Flag, without pressure:
- claims with no proof file or number (offer: "a link, a file, or a number would make this stronger");
- words like "expert" or "best" without evidence (see `rules/01-truthfulness.md`);
- numbers with no definition or date;
- details that contradict something already saved (see `workflows/import-existing-cv.md` for conflicts).

### 7. Next topic

Ask whether to continue with another project or topic. Stop when the user wants to stop; unfinished entries stay with `[TODO]`.

## Example (fictional)

> **User:** I made a dashboard for my campus cooperative. They kept sales in spreadsheets and just guessed what to restock. I cleaned about 12,000 rows, put them in SQLite, and built a Streamlit dashboard. I did it alone. I showed it to the managers and they started using it every month.
>
> **AI:** Got it: the managers guessed what to restock; you alone cleaned about 12,000 rows, used SQLite, built a Streamlit dashboard, and presented it. A few things so I get it right: when did you do it, and for how long? What was wrong with the data (duplicates, missing values)? Did you find anything in the numbers? Is there a link to the repo or demo? Anything you do not want me to mention?
>
> **User:** Sep to Dec 2024. Duplicates and missing prices. Three product categories made most of the revenue. Repo is github.com/janedoe-example/sales-dashboard. Don't call it production software, it's a student project.
>
> **AI:** (writes `info/PROJECT/sales-dashboard.md` with Problem, Solution, My part, Stack, Results, and "Not to claim: not production software", then shows the summary and asks to confirm.)

The result is the file in [`examples/sample-user/info/PROJECT/sales-dashboard.md`](../examples/sample-user/info/PROJECT/sales-dashboard.md).

## What not to do

- Do not ask all the template fields one by one like a form.
- Do not rewrite the user's words into stronger claims ("led" instead of "helped", "expert" instead of "used").
- Do not save something the user has not confirmed.
- Do not skip the `[TODO]` markers to make an entry look complete.
