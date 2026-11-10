# Unloopr troubleshooting index

Start from what the person sees, not from internal names.

| Symptom / search phrase | Problem ID | Next step |
|---|---|---|
| "How do I undo my last commit?" | `ULP.GIT.UNDO_COMMIT` | If not pushed: `git reset --soft HEAD~1`. If pushed: ask before force-pushing. |
| "Merge conflict — how do I fix it?" | `ULP.GIT.MERGE_CONFLICT` | Open the file, resolve `<<<<<<<` markers, `git add`, commit. |
| "I pushed my API key to GitHub — what now?" | `ULP.SECRET.LEAKED_KEY` | Delete key at source → new key → `.env` → `.gitignore`. Act fast. |
| "I pushed to the wrong branch" | `ULP.GIT.WRONG_BRANCH` | Cherry-pick commits to the right branch. |
| "What does detached HEAD mean?" | `ULP.GIT.DETACHED_HEAD` | `git checkout main`. Nothing is broken. |
| "I force-pushed and deleted work" | `ULP.GIT.FORCE_PUSH_LOSS` | `git reflog` → find pre-push hash → `git reset --hard`. Talk to the team. |
| "Why can't my friend open my localhost link?" | `ULP.DEPLOY.LOCALHOST_GAP` | Push to GitHub → connect to Vercel/Railway/Render. |
| "Works on localhost, broken on the live site" | `ULP.DEPLOY.ENV_MISSING` | Add env vars in host dashboard; check API URLs. |
| "My AI imported a package that doesn't exist" | `ULP.AI.HALLUCINATED_IMPORT` | Don't install it. Search npm for the real name. |
| "The code looks right but doesn't work" | `ULP.AI.PLAUSIBLE_WRONG` | Read the error, print values, check boundaries. |
| "Cursor asked me to commit — what does that mean?" | `ULP.AI.COMMIT_CONFUSION` | Say yes. Commit = snapshot before changes. |
| "Where do I put my API key?" | `ULP.SETUP.ENV_VARS` | `.env` file + `.gitignore`. Never in code. |
| "What is a .gitignore file?" | `ULP.SETUP.GITIGNORE` | Add `.env`, `node_modules/`, `*.log` before first commit. |
| "What do I get free?" | `ULP.PRICE.CONFUSION` | Public website: up to 3 repo scans per day; paid checkout is closed. See pricing/status. |

## Escalation rule
Search the FAQ and glossary first. Coach them through it second. Open an "I'm stuck" issue only when the person is still stuck.

## Connection and billing checks (November 10, 2026)

| Symptom | What it means | Safe next step |
|---|---|---|
| Browser GET to `/mcp` returns 404 | A browser request is not an authenticated MCP POST | Use an OAuth-capable MCP client and [the editor setup](ide-setup.md) |
| MCP initialize returns 401 | No accepted Bearer token was supplied | Complete OAuth; never paste a token in a public issue |
| Paid checkout returns HTTP 503 | Checkout is intentionally unavailable | Continue with [free scanning](https://unloopr.com/scan); read [plan status](pricing.md) |
| A public scan returns zero findings | None of the covered rules matched the scanned material | Review output scope; do not assume zero defects |
| Can't find Unloopr in ChatGPT directory | Public publication is not independently verified | Do not infer listing from the MCP address; see [current status](current-product.md) |
