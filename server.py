"""your-first-memory — a memory for a model that has none.

Last week's instrument gave your model a sense of time. But ask it
"what did we say last Tuesday?" and it can only guess: nothing survives
the end of a conversation. This server is the smallest honest fix —
a table, two tools, and suddenly there is a *record*. The pattern
generalizes to anything worth keeping. See docs/adr/ for every choice
made here — each one records a real decision with the road not taken.
"""
import os
from mcp.server.fastmcp import FastMCP

import psycopg

DATABASE_URL = os.environ.get("DATABASE_URL")

mcp = FastMCP(
    "your-first-memory",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)),
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS quotes (
    id          SERIAL PRIMARY KEY,
    quote       TEXT NOT NULL,
    who         TEXT,                          -- optional: unattributed quotes are allowed (ADR-0004)
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
"""


def db():
    """One connection per tool call (ADR-0002): Neon's free tier suspends
    when idle, and a fresh connection wakes it transparently. A held pool
    would die during the nap and greet you with a stale-connection error."""
    if not DATABASE_URL:
        raise RuntimeError(
            "DATABASE_URL is not set. Not an error in the code — a feature "
            "waiting for setup: create a free database at neon.tech, copy the "
            "connection string, and set it as an environment variable "
            "(COURSE-STEPS.md, step 2)."
        )
    conn = psycopg.connect(DATABASE_URL)
    with conn.cursor() as cur:
        cur.execute(SCHEMA)
    conn.commit()
    return conn


@mcp.tool()
def record_quote(quote: str, who: str = "") -> str:
    """Save a quote worth keeping. `who` is optional — a quote you can't
    place is still worth remembering."""
    with db() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO quotes (quote, who) VALUES (%s, %s) RETURNING id, recorded_at",
            (quote, who or None),
        )
        qid, ts = cur.fetchone()
        conn.commit()
    return f"Recorded as quote #{qid} at {ts.isoformat()}."


@mcp.tool()
def list_quotes() -> str:
    """Every quote in the memory, oldest first."""
    with db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, quote, who, recorded_at FROM quotes ORDER BY id")
        rows = cur.fetchall()
    if not rows:
        return "The memory is empty. Record something worth keeping."
    lines = []
    for qid, quote, who, ts in rows:
        attribution = f" — {who}" if who else ""
        lines.append(f'#{qid} ({ts:%Y-%m-%d %H:%M}): "{quote}"{attribution}')
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
