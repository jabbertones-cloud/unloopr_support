# Where do I put my API key?

**Not in your code.** That's the whole answer. Here's the how.

## The rule

API keys go in a **`.env` file**. Your code reads from it. Git ignores it. The key never touches GitHub.

## Step by step

**1. Create a file called `.env`** in your project folder:

```
MY_API_KEY=sk-abc123your-real-key-here
```

**2. Make sure Git ignores it.** Create (or open) a file called `.gitignore` and add:

```
.env
```

**3. Read the key in your code** instead of pasting it:

```js
// Don't do this:
const apiKey = "sk-abc123your-real-key-here";

// Do this:
const apiKey = process.env.MY_API_KEY;
```

**4. When you deploy**, add the same key in your hosting dashboard (Vercel, Netlify, Cloudflare — they all have an "Environment Variables" section). The `.env` file stays on your computer; the server gets its own copy through the dashboard.

## What is an environment variable?

It's just a named value your program can read — like a sticky note the computer keeps for your app. `process.env.MY_API_KEY` means "read the sticky note called MY_API_KEY." The sticky note lives outside your code, so it never gets uploaded to GitHub.

## Why this matters

If a key is in your code and you push to GitHub, bots find it in seconds and use it. You'll get a surprise bill. The `.env` + `.gitignore` habit prevents this completely.

## See also

- [I accidentally committed my API key — what now?](../panic/api-key-leaked.md) — if it's too late for prevention

---

## Never panic about this again

Unloopr's secret scanner finds keys sitting in the wrong place and shows you exactly where they belong.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
