# cursor.directory — Listing draft

> **STATUS: DRAFT — DO NOT SUBMIT.** This copy is ready to paste into the
> cursor.directory submission form when the time comes. Nothing here has been
> submitted.

**Submit at:** https://cursor.directory/mcp/new (or /plugins/new — the site's
bot check may require opening it in a real browser). Fill in the fields with
the values below.

---

## Name

```
Unloopr
```

## One-line description

```
Break the loop. Unloopr teaches you what your AI-generated code got wrong — in plain words.
```

## Long description

```
Unloopr is a code coach for vibe coders — the people building apps with AI who
want to actually understand their code.

Add it to Cursor once, and your agent gets a coach on call. Before every
commit, it checks your staged diffs: security holes, leaked keys, broken
deploys, and the quiet bugs AI loves to write. Every finding comes in plain
words — what's wrong, why it matters, how to fix it — so you learn the pattern
and stop making the same mistake.

4 tools:
- unloopr_agent_guidance — coaching advice before you start a task
- unloopr_agent_check — scan a diff for problems
- unloopr_agent_outcome — report your decision so the coach learns what you care about
- unloopr_scan_report — the plain-language version, shareable with humans

Pair it with the .cursor/rules file (in the docs) and Cursor's agent runs the
check automatically before every commit.

Hosted MCP, Streamable HTTP. Your own private token keeps your code yours —
never shared, never used for training. Free tier: 3 fixes per scan.
```

## Install config JSON

```json
{
  "mcpServers": {
    "unloopr": {
      "url": "https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>",
      "headers": {
        "Authorization": "Bearer <token>"
      }
    }
  }
}
```

Replace `<token>` with your Unloopr token (get one at unloopr.com).

## Tags

```
code-review, ai-coding, code-coach, vibe-coding, mcp, security, developer-tools
```

## Category

Developer Tools / Code Quality

## Links

- Homepage: https://unloopr.com
- Support: https://github.com/jabbertones-cloud/unloopr_support
- Docs: 60-second setup + .cursor/rules companion in the support repo
