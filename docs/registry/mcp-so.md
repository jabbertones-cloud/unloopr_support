# mcp.so — Listing draft

> **STATUS: DRAFT — DO NOT SUBMIT.** This copy is ready to paste into the
> mcp.so submission form when the time comes. Nothing here has been submitted.

**Submit at:** mcp.so → Submit button, or https://mcp.so/submit (form-based,
manual submission — mcp.so blocks automated posts).

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

Connect it to your editor (Cursor, VS Code, Claude, ChatGPT) and it checks the
code your AI writes before you commit it. It finds real problems — security
holes, leaked keys, broken deploys — and explains each one in plain words:
what's wrong, why it matters, and how to fix it so you learn the pattern.

4 tools:
- unloopr_agent_guidance — coaching advice before you start a task
- unloopr_agent_check — scan a diff for problems
- unloopr_agent_outcome — report your decision so the coach learns what you care about
- unloopr_scan_report — the plain-language version, shareable with humans

Hosted MCP, Streamable HTTP. Your own private token keeps your code yours.
Free tier: 3 fixes per scan. Paid: Founder $9/mo, locked forever for the first 500.
```

## Connect URL

```
https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>
```

Replace `<token>` with your Unloopr token. Auth: token in path (paste the full
URL, no extra auth step needed).

## Server config (paste into the "config" field)

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

## Tags

```
code-review, ai-coding, code-coach, vibe-coding, mcp, security, developer-tools
```

## Category

Developer Tools / Code Quality

## Links

- Homepage: https://unloopr.com
- Support: https://github.com/jabbertones-cloud/unloopr_support
