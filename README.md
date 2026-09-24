# your-first-memory

**A memory for a model that has none.** Sibling of
[`your-first-instrument`](https://github.com/jlumbroso/test-time-mcp-exercise):
last week your model got a sense of time; tonight it gets a record that
survives the end of the conversation.

One table. Two tools (`record_quote`, `list_quotes`). A database that
outlives the server, the deploy, and the chat window.

- **In class**: follow [COURSE-STEPS.md](COURSE-STEPS.md).
- **Every design choice, with the road not taken**: [docs/adr/](docs/adr/) —
  four real decisions, none decorative. When you change the code and face
  a choice of your own, add ADR-0005.
- **Stack**: FastMCP (`mcp[cli] >=1.2,<2` — pinned, see render.yaml) +
  `psycopg` + [Neon](https://neon.tech) free-tier Postgres + Render
  free-tier compute. The secret (`DATABASE_URL`) lives only in the
  environment (ADR-0003).

*CAM · CIS 7000-008 · Penn · Fall 2026 — session 5 (2026-09-24).*
