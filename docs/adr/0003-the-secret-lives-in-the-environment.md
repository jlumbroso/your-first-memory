# ADR-0003: The connection string is a secret, and secrets live in the environment

- Status: accepted
- Date: 2026-09-24
- Deciders: Lapidary 5

## Context

`DATABASE_URL` contains a password. It has to reach the server somehow,
and this repo is public.

## Decision

The connection string exists in exactly two places: Neon's dashboard
(where it's issued) and Render's environment variables (where you paste
it). Never in code, never in git, never in a README example with your
real values. `render.yaml` declares the variable with `sync: false`,
which makes Render *ask you* for the value at deploy time instead of
reading it from the repo.

## The road not taken, and why

**Hardcoding it "just for now"** is how real credentials end up in real
git histories — and a git history is a memory that never forgets (that's
the whole reason we like it). The five seconds saved are repaid by a
credential rotation the day the repo goes public.

**A `.env` file committed with a placeholder** invites the classic
accident: fill in the real value, `git add .`, done. We keep the variable
out of the repo entirely.

## Consequences

- Missing `DATABASE_URL` is treated as *unfinished setup, not a crash*:
  the server starts fine and the tools answer with a pointer to
  COURSE-STEPS step 2. You can deploy first and wire the database second.
- If a connection string ever does leak: no panic, no history rewriting.
  Neon's dashboard resets the password in one click; paste the new one
  into Render. Exposure is a rotation, not a crisis.
