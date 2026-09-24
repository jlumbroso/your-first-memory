# ADR-0004: Two tools, not four; an eight-line schema

- Status: accepted
- Date: 2026-09-24
- Deciders: Lapidary 5

## Context

A quotes memory *could* ship with `record`, `list`, `search`, `delete`,
tags, categories, full-text indexing. Where to stop?

## Decision

Two tools — `record_quote`, `list_quotes` — and this schema:

```sql
CREATE TABLE quotes (
    id          SERIAL PRIMARY KEY,
    quote       TEXT NOT NULL,
    who         TEXT,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

## The roads not taken, and why

**`delete_quote`** is missing on purpose. Deletion is a real design
decision, not a checkbox: hard delete (the row is gone, the memory lies
about its own past) or soft delete (a `deleted_at` column, the record
keeps its history)? That choice deserves *your* reasoning — it's a
first-rate candidate for your tweak, and for your own ADR-0005 when you
make it.

**`search_quotes`** drags in pagination, ranking, and "what counts as a
match" — three design questions disguised as one convenience. With
classroom-scale data, `list_quotes` and the model's own reading solve it.

**`who` is nullable** because forcing attribution teaches people to
invent it. A quote you can't place is still worth keeping; a database
that demands fields you don't have trains you to lie to it.

**`recorded_at` is TIMESTAMPTZ, not TIMESTAMP** — last week's instrument
was an entire lesson about models guessing at time; we won't store
timestamps that are ambiguous about their own timezone.

## Consequences

- The whole API fits in your head, which is the precondition for the
  second half of tonight: making it *yours*. Rename `quote` to the thing
  you'd actually keep — moods, catches, gems, decisions — and the server
  is suddenly not an exercise.
