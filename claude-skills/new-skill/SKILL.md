---
name: new-skill
description: Guided creation (or update) of a personal Claude Code skill. Use when the user wants to create a skill, write a SKILL.md, teach Claude their ways for a recurring task or a tool they built, or update/improve a skill that exists. Walks the four-part anatomy (purpose, expectations, composition, situations), installs the file in the right place, and runs a with/without test.
---

# Guided skill creation (CAM · CIS 7000)

You are helping the user create or update a **skill**: a folder with a
`SKILL.md` that teaches Claude *their ways* for something recurring —
often the MCP server they built in this course. Keep the user in the
driver's seat: you interview, draft, and install; they decide every word
that claims to be *their* way.

## If they're UPDATING an existing skill

Read the current `SKILL.md` first. Ask what behavior was wrong or missing
(get the concrete episode, not an abstraction). Change the smallest part
that fixes it. Then jump to step 4 (test).

## Step 1 — Interview, four parts (one question at a time, never a form)

1. **Purpose** — "In one sentence: what is this bundle's whole job?"
   (Good: "be my training log, not my coach." Push past tool-listing.)
2. **Expectations** — "How should it behave with you? What should it
   always confirm first? What tone?"
3. **Composition** — "Which tools chain, in what order? What should
   happen BEFORE what?" (e.g. "always list before summarizing; record
   only after confirming with me.")
4. **Situations** — "Give me two or three concrete moments you'd want
   this used — and one moment where it should do NOTHING."

## Step 2 — Draft

Write a `SKILL.md` with:
- frontmatter: `name` (kebab-case, their choice) and `description` — the
  description is the TRIGGER: it must say *when* this applies, in words a
  model can match against real requests ("Use when the user mentions
  workouts, lifts, gym sessions, or asks what they trained recently").
- body: their four parts, in their words, compressed. Ways, not API docs
  — the tool schemas already exist; this file carries judgment.
- the do-nothing rule stated explicitly. Restraint is part of the skill.

Show the full draft. **They edit before anything is installed.**

## Step 3 — Install

Project-local (this project only): `.claude/skills/<name>/SKILL.md`
Global (every project): `~/.claude/skills/<name>/SKILL.md`
Ask which they want; default project-local. Create the folder, write the
file, confirm the path back to them.

## Step 4 — Test, honestly

Have them write **three real asks** before testing: one easy, one
ambiguous, one where the skill should do nothing. Then: **new session**
(skills load at session start — this matters, say it), run all three,
and compare behavior against their memory of life before the skill.
If the skill didn't trigger, the `description` is the usual culprit —
tune it and repeat. One iteration loop minimum; this is the craft.

## Register

Course language: *think with / interact / discuss* — models are *they*,
never "the tool uses." The skill the user writes should sound like them,
not like documentation.
