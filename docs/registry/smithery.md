# Smithery.ai — Listing draft

> **STATUS: DRAFT — DO NOT SUBMIT.** This copy is ready to paste into the
> Smithery publish form when the time comes. Nothing here has been submitted.

**Submit at:** https://smithery.ai/new — sign in with GitHub, enter the server
URL below, and fill in the fields. Unloopr is a hosted remote server
(Streamable HTTP, token in path), so use the **URL-based publish** flow, not
the stdio/npm flow.

---

## Qualified name

```
jabbertones-cloud/unloopr
```

## Display name

```
Unloopr — Break the loop.
```

## Server URL

```
https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>
```

Transport: **Streamable HTTP**. Auth: per-user token in the path. When a user
installs from the listing, they enter **their own Unloopr token** — the listing
itself must never contain a real token.

## Config schema (for the publish form — asks users for their token at install)

```json
{
  "type": "object",
  "properties": {
    "token": {
      "type": "string",
      "title": "Unloopr token (get yours at unloopr.com)"
    }
  },
  "required": ["token"]
}
```

## Short description (one-liner)

```
Break the loop. Unloopr teaches you what your AI-generated code got wrong — in plain words.
```

## Long description

```
Unloopr is a code coach for vibe coders — the people building apps with AI who
want to actually understand their code.

Connect it to your editor and it checks the code your AI writes before you
commit it. It finds real problems — security holes, leaked keys, broken
deploys — and explains each one in plain words: what's wrong, why it matters,
and how to fix it so you learn the pattern.

4 tools:
- unloopr_agent_guidance — coaching advice before you start a task
- unloopr_agent_check — scan a diff for problems
- unloopr_agent_outcome — report your decision so the coach learns what you care about
- unloopr_scan_report — the plain-language version, shareable with humans

Your own private token keeps your code yours. Code is never shared or used for
training. Free tier: 3 fixes per scan. Paid: Founder $9/mo, locked forever for
the first 500.
```

(Write the long description with search in mind: repeat the key words —
code coach, vibe coding, code review, AI-generated code, MCP, security — so
people find it.)

## Categories

```
developer-tools, code-review, ai-coding
```

## Tags

```
code-coach, vibe-coding, mcp, security, ai-coding, code-review, developer-tools
```

## Homepage

```
https://unloopr.com
```

## Repository / Support

```
https://github.com/jabbertones-cloud/unloopr_support
```

(Note: the unloopr_support repo does not exist yet — create it before
submitting, or point this at the live support URL at submit time.)

## Install config JSON (shown to users after install)

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
