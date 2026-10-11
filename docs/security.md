# Security & privacy

> Last updated: 2026-10-11

---

## The short version

Unloopr reads your code to teach you. It never shares your code with anyone, never uses it to train models, and deletes what it doesn't need. If you delete your account, your data goes with it.

---

## What Unloopr reads

- **Your repo's code and history** — the files and the git history (commits, diffs). The history is how the tutor learns which bugs you're likely to hit: it studies how bugs were fixed across thousands of repos, then looks for the same shapes in yours.
- **Your GitHub identity** — just enough to connect the repo (username, repo list). Read-only OAuth scope.

## What Unloopr never does

- **Never shares your code** with anyone — not other users, not partners, not advertisers.
- **Never trains models on your code.** Your code teaches *you*, not our models.
- **Never writes to your repo** unless you explicitly approve a fix (Pro one-tap apply). The default product is read-only.
- **Never sells data.** There is no data business. The product is the business.

## Secrets in your code

If Unloopr finds an API key or secret in your source, it tells *you* — privately, in your report. It does not log the secret value, does not include it in lessons shown to others, and does not store it beyond your report's lifetime.

If you've already pushed a key to GitHub: [act fast — here's what to do](faq/faq.md#i-pushed-my-api-key-to-github--what-now).

## Data retention

- **Scan reports** are kept while your account is active so you can revisit lessons.
- **Deleted repos** drop their reports within 30 days.
- **Deleted accounts** drop everything within 30 days. Email support to confirm deletion.

## The agent version (MCP)

The `unloopr_agent` MCP follows the same rules, plus anti-extraction protections: it answers questions about *your* code only, never dumps its rule catalog, and rate-limits queries to prevent systematic harvesting. Details: [MCP anti-extraction standard](../../mcp-anti-extraction-standard.md).

---

## Questions

**Can Unloopr see my private repos?**
Only the ones you connect, only with read-only access you grant. Revoke access anytime in GitHub Settings → Applications.

**Does Unloopr store my code?**
It caches scan inputs long enough to generate your report, then drops raw file contents. What persists is the *findings* (your lessons), not your source.

**Who do I contact about privacy?**
Open an issue with the **Privacy** label, or email the address in your account settings. We answer within 2 business days.

---

## Related articles

- [Getting started](getting-started.md)
- [Pricing](pricing.md)
- [FAQ](faq/faq.md)
