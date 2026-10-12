# How do I put my app online?

**The deploy gap.** Your app works on your computer. Here's how the world sees it.

## The plain-English version

"Putting it online" means: **rent a computer that's always on, put your code there, and give it an address** (a URL). Hosting services do all three for you.

## The easiest path (5 minutes)

**If your app is a website** (HTML, or a framework like Next.js, React, Vite):

1. **Push your code to GitHub** — [how?](ai-app-to-github.md)
2. Go to [vercel.com](https://vercel.com) or [netlify.com](https://netlify.com). Sign up with GitHub (one click).
3. Click **"Add New Project"** → pick your repo → click **Deploy**.
4. Wait a minute. You get a URL like `your-app.vercel.app`. **You're live.**

That's it. No servers, no config, no terminal magic. They read your code and figure out the rest.

## The checklist (if it doesn't work)

- **API keys?** Add them in the hosting dashboard under "Environment Variables." ([Where do I put my API key?](../explain/where-api-key-goes.md))
- **Build failing?** Make sure `npm run build` works on your computer first.
- **Blank page?** Check the deploy logs — they tell you what went wrong.

## What about backends and databases?

If your app needs a server or database (not just a website), it's one step harder:
- **Vercel/Netlify** handle simple backends (serverless functions) automatically.
- **Railway** or **Render** handle full servers and databases — connect your GitHub repo, same idea.

## The rule to remember

You don't manage servers anymore. Push to GitHub → connect to a host → deploy. The host is the computer that's always on.

## See also

- [Why does it work on localhost but not on the live site?](../explain/localhost-vs-live.md) — when it's live but broken
- [My AI built an app — how do I put it on GitHub?](ai-app-to-github.md) — step zero

---

## Never panic about this again

About to put your app online? Unloopr scans it first — 3 fixes free, so you ship with confidence.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
