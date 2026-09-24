# your-first-memory — the steps, in class order

*Sibling of `your-first-instrument` (last week). Same shape: read it,
deploy it, make it yours. New tonight: the server keeps state, and the
state lives somewhere that outlives both the server and the chat.*

## 1. Read the server (3 minutes, really)

`server.py`, top to bottom. It is shorter than this file. Notice:
- the schema (8 lines) — the only data design in the repo
- the two tools — record and list, nothing else (docs/adr/0004 says why)
- what happens when `DATABASE_URL` is missing (a pointer, not a crash)

## 2. Get your database (neon.tech)

1. https://neon.tech → Sign up (GitHub works; free tier, no card).
2. Create a project — name it anything ("my-memory" is fine).
3. Copy the **connection string** (starts `postgresql://…`). That string
   is a password: it goes ONE place (step 3), never in code or chat.

## 3. Deploy (render.com — same as last week)

1. Fork this repo (or use the template button).
2. Render → New → Blueprint → your fork.
3. When Render asks for `DATABASE_URL`, paste your Neon string.
4. Deploy. Your MCP URL is `https://<your-service>.onrender.com/mcp`.

## 4. Connect your Claude, and test the claim

Add the connector (Settings → Connectors → same flow as last week), then:
- *"Record this: …"* — something said tonight that you want to keep.
- *"What quotes do I have?"*
- Now the real test: **start a brand-new conversation** and ask again.
  Last week's instrument couldn't do that. This one can. That difference
  is the whole lesson.

## 5. Make it yours

`quotes` is a placeholder for *whatever you would actually keep*:
moods, catches-of-your-own-reasoning, decisions, gems. Rename the table,
the columns, the tools — the model adapts to your tool names instantly.
When you make a real design choice (add delete? soft or hard? — see
ADR-0004), write your own ADR-0005 in docs/adr/. That's not homework
theater: it's the difference between code you have and decisions you own.
