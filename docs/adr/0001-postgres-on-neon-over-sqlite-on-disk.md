# ADR-0001: Postgres on Neon, not SQLite on the server's disk

- Status: accepted
- Date: 2026-09-24
- Deciders: Lapidary 5 (build), Jérémie Lumbroso (the Neon direction was his)

## Context

The server needs somewhere to keep quotes. The obvious cheap answer is
SQLite: one file, zero accounts, `import sqlite3` and done. We almost
did that.

## Decision

An external Postgres database on Neon's free tier, reached through a
`DATABASE_URL` environment variable.

## The road not taken, and why

**SQLite on Render's free tier is a trap that teaches the wrong lesson.**
Render's free instances have an *ephemeral* filesystem: every deploy —
including the redeploy you trigger by tweaking `server.py`, which is the
whole second half of tonight — replaces the disk. Your quotes would
survive exactly until the first time you improved the code that stores
them. A memory that dies when you touch it is not a memory.

The deeper reason: this course's arc is *state that outlives the
conversation*. Putting the state inside the compute would rebuild, at the
architecture level, the exact fragility we're escaping at the
conversation level.

## Consequences

- Students create one more free account (no card). The signup is part of
  the lesson, not overhead: your data now has an address that isn't your
  laptop and isn't your chat window.
- A secret now exists (the connection string). It lives in an environment
  variable, never in code — see ADR-0003.
- The database survives the server. Delete the Render service entirely;
  your quotes are still there. That asymmetry is the point of the night.
