# Add Unloopr to your editor in 60 seconds

> Last updated: 2026-10-11

Unloopr lives inside your editor now. It checks the code your AI writes, before you commit it. One setup, then it rides along with you.

---

## What you need first

Your **Unloopr token**. It looks like a long jumble of letters and numbers. It is yours alone — like your house key. Never share it, never paste it in a public chat, never post a screenshot of it.

Every URL below says `<token>`. **Replace `<token>` with your token.** If you do not have a token yet, get one at [unloopr.com](https://unloopr.com).

---

## One-click badge (Cursor)

Put this badge in your repo's README. One click, and it opens Cursor with Unloopr ready to add:

```markdown
[![Add Unloopr to Cursor](https://img.shields.io/badge/Add%20to-Cursor-blue)](cursor://anysphere.cursor-deeplink/mcp/install?name=unloopr&config=BASE64_JSON_CONFIG)
```

How to make it work: take this JSON, replace `<token>`, base64-encode the whole thing, and paste the result where it says `BASE64_JSON_CONFIG`:

```json
{"mcpServers":{"unloopr":{"url":"https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>"}}}
```

(Tip: on a Mac, `echo -n '<the-json>' | base64` does the encoding for you.)

---

## Option 1: Cursor (manual)

1. Open Cursor. Go to **Settings → Tools & Integrations → MCP**.
2. Click **New MCP Server**. A file called `mcp.json` opens.
3. Paste this in. Replace `<token>` with your token:

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

4. Save the file. Restart Cursor. You should see **unloopr** in the MCP list with 4 tools.

**Not showing up?** Check two things: did you save the file, and is the URL pasted with your real token (no `<` or `>` left in it)?

---

## Option 2: VS Code

VS Code speaks MCP out of the box now. No extension needed.

1. Open the command palette (`Cmd+Shift+P` on Mac, `Ctrl+Shift+P` on Windows).
2. Type **MCP** and pick **MCP: Add Server**.
3. Choose **HTTP**. Paste this URL, with your token:

```
https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>
```

4. Give it the name **unloopr**. Done.

**Keep your token out of the file (smart move).** VS Code lets you use an `inputs` block so your token is not saved as plain text. Add this to your `mcp.json`:

```json
{
  "servers": {
    "unloopr": {
      "type": "http",
      "url": "https://unloopr-mcp.smatdesigns.workers.dev/mcp/${input:unloopr-token}"
    }
  },
  "inputs": [
    {
      "id": "unloopr-token",
      "type": "promptString",
      "description": "Your Unloopr token (get one at unloopr.com)",
      "password": true
    }
  ]
}
```

VS Code will ask for your token when it connects, and it keeps it in a safe spot — not in the file. Also check the in-app **MCP gallery** in VS Code: new servers appear there as they get published, and you may be able to add Unloopr straight from the gallery without editing any JSON.

---

## Option 3: Claude

1. Go to **claude.ai → Settings → Connectors**.
2. Click **Add custom connector** (or similar wording — Claude renames this button now and then).
3. Paste your full URL, with your token:

```
https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>
```

4. Save. Claude will now offer Unloopr's 4 tools in your chats.

**Not connecting?** Make sure you pasted the whole URL, token included. If Claude asks for auth, the token in the URL already is your auth.

---

## Option 4: ChatGPT

1. Open ChatGPT. Turn on **Developer Mode** (in your ChatGPT settings).
2. Go to **Connectors → Create**.
3. For authentication, pick **None** — your token is already in the URL.
4. Paste this, with your token:

```
https://unloopr-mcp.smatdesigns.workers.dev/mcp/<token>
```

5. Save. ChatGPT can now call Unloopr's 4 tools.

> **Heads-up:** ChatGPT renames menus fast. If "Developer Mode" or "Connectors" looks different in your app, search ChatGPT's settings for "MCP" or "connectors" and follow the current flow. The part that never changes: paste the URL with your token.

---

## What you get: 4 tools

Once it is connected, your editor's AI can use:

- **unloopr_agent_guidance** — advice for the task at hand. "What should I watch out for?"
- **unloopr_agent_check** — paste a diff, get the problems found. Runs before you commit.
- **unloopr_agent_outcome** — tells Unloopr what you decided, so it learns what matters to you.
- **unloopr_scan_report** — the plain-words version of a scan. Share this one with humans.

---

## Prefer a directory listing?

If your tool finds MCP servers through a public directory instead of a manual URL, this endpoint exists for that:

```
POST https://unloopr-mcp.smatdesigns.workers.dev/mcp
```

It is the public OAuth directory endpoint. Your own personal connection still uses the `/mcp/<token>` URL above.

---

## Troubleshooting

**"Invalid token" / 401 errors**
Your token is wrong or has a typo. Copy it fresh from unloopr.com. Make sure there are no spaces at the start or end.

**Connected but no tools show up**
Restart the editor after saving the config. Cursor and VS Code only read the config when they start.

**It works in one editor but not another**
Each editor keeps its own config. You added it to Cursor? That does not add it to VS Code too. Repeat the steps for each editor you use.

**Still stuck?**
Open an **"I'm stuck"** issue and tell us which editor you are using and what you see. Paste the editor name and the error message — but **never paste your token**.

---

## Related articles

- [Getting started](getting-started.md) — your first scan in 5 minutes
- [FAQ](faq/faq.md) — panic questions, answered
- [Cursor rules for your repo](cursor-rules.md) — make Cursor's agent use Unloopr on every commit
- [Troubleshooting](troubleshooting.md) — when something breaks
