# ADR-0002: Plain SQL via psycopg; one connection per tool call

- Status: accepted
- Date: 2026-09-24
- Deciders: Lapidary 5

## Context

Two stacking choices: how to talk to Postgres (raw SQL vs an ORM like
SQLAlchemy), and when to connect (a pooled connection held for the
process vs a fresh one per call).

## Decision

Raw SQL through `psycopg`, and a new connection inside every tool call.

## The road not taken, and why

**An ORM** would add a models file, a session object, and a migration
story — machinery that buries the only genuinely interesting artifact in
this repo: the eight-line schema. You should be able to read `server.py`
top to bottom in three minutes and account for every line. (The
`your-first-instrument` README made that promise; this repo keeps it.)

**A connection pool** is the "right" answer for a busy service and the
wrong one here. Neon's free tier *suspends* the database when idle —
that's how it's free — and a pooled connection held across the nap dies,
so your first question after lunch would be answered with a stale-socket
traceback. A fresh connection wakes the database transparently. Cost: a
few hundred milliseconds per call, invisible next to the model's own
thinking time.

## Consequences

- `CREATE TABLE IF NOT EXISTS` runs on every connection: idempotent,
  and it means there is no separate "setup" step to forget.
- If this ever serves real traffic, revisit both halves of this ADR —
  and notice that you'd be revisiting them for a *reason you can name*,
  which is what an ADR is for.
