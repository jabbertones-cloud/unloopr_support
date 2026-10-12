# Make Cursor's agent use Unloopr on every commit

> Last updated: 2026-10-11

This is a rules file for Cursor. It teaches Cursor's agent to check code with Unloopr before it commits. Copy the block at the bottom into a file named `.cursor/rules` in your repo, and Cursor follows it on its own.

---

## How to install it

1. In your repo, make a folder called `.cursor` if you do not have one.
2. Inside it, make a file called `rules` (no file extension).
3. Paste the whole block below into it.
4. Done. Next time the agent works on your code, it will run Unloopr checks.

This file is for the **agent**, not for you. It is written in agent-speak on purpose — Cursor's agent follows instructions like these best.

---

## The rules file (copy everything below this line)

```markdown
# Unloopr — code coach rules for this repo

You are writing code with a human who is learning. Unloopr is their code coach.
It scans diffs and teaches patterns, in plain words. Use it. Never invent scan
results — only report what the tools actually returned.

## The tools (already connected via MCP)

- unloopr_agent_guidance(task, top) — get advice before starting a task.
- unloopr_agent_check(diff, path, manifest_modules, first_party_modules, language, user_key, repo_url) — check a diff for problems. The tools take diffs, not workspace context: always pass the actual diff text.
- unloopr_agent_outcome(decision_id, outcome, family_id, note) — report what the human decided, so the coach learns.
- unloopr_scan_report(diff, tier, format, ...) — the plain-language version of a scan, for humans.

## Before every commit

1. Run unloopr_agent_check on the staged and uncommitted diffs. If there are no
   changes, skip it.
2. Surface the findings inline, in plain words, in the chat. Say what is wrong,
   why it matters, and what to change. Do not just list rule names.
3. If a finding is serious (security, data loss, broken deploy), stop and ask
   the human before committing. For small stuff, fix it and say what you fixed.
4. After the human decides (fix it, accept the risk, or ignore it), call
   unloopr_agent_outcome with the decision_id from the check, the outcome
   ("fixed", "accepted", or "ignored"), and a one-line note.

## When the human asks "what's wrong with my code"

Use unloopr_scan_report. It speaks plain language. Share its output directly —
do not reword it into jargon.

## When starting a risky task

Call unloopr_agent_guidance first with the task name. Apply what it says.

## Ground rules

- The coach sees diffs, not your whole workspace. Give it the diff.
- A green test suite is not proof the bug is gone. A green Unloopr check is a
  signal, not proof either. Say what you observed, not what you proved.
- Never shame the human for a bug. They are learning. Teach the pattern, not
  just the fix.
```

---

## What this gets you

- The agent checks your diffs with Unloopr **before** committing — no more "oops" commits.
- Findings show up inline, in words you can read.
- Every decision you make (fix it or accept it) trains Unloopr to care about what **you** care about.

---

## Related articles

- [Add Unloopr to your editor](ide-setup.md) — the 60-second setup
- [Getting started](getting-started.md) — your first scan in 5 minutes
