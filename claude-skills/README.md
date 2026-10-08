# claude-skills/ — skills for your Claude Code

Session-6 material: **new-skill**, the guided skill-creation skill.

Install (pick one):

**Have your Claude do it** — paste to Claude Code:
> Install the skill from https://github.com/jlumbroso/your-first-memory/tree/main/claude-skills/new-skill into my .claude/skills/

**Or one command from your project root:**
```
mkdir -p .claude/skills/new-skill && curl -fsSL https://raw.githubusercontent.com/jlumbroso/your-first-memory/main/claude-skills/new-skill/SKILL.md -o .claude/skills/new-skill/SKILL.md
```

Then start a NEW Claude Code session (skills load at start) and say
"create a skill for my server" — or /new-skill.
