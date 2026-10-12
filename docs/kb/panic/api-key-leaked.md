# I accidentally committed my API key — what now?

**Act fast. This is the one panic on this page where speed matters.** Bots scan GitHub for leaked keys within seconds.

**Asked by 89,727+ people on GitHub. Here's exactly what to do.**

## Do this right now (5 minutes)

1. **Go revoke the key.** Open the service the key belongs to (OpenAI, Stripe, AWS, whatever) and delete/regenerate it. The old key stops working. This is the most important step — do it first, before reading further.

2. **Remove it from your code.** Replace the key in your files with a placeholder:
   ```js
   const apiKey = process.env.MY_API_KEY; // not the real key
   ```

3. **Add a `.gitignore` file** (if you don't have one) and put your secrets file in it:
   ```
   .env
   ```
   Then put the real key in a `.env` file that never gets committed.

4. **Remove the key from Git history.** The key is still in your old commits. If the repo is yours and nobody else uses it:
   ```bash
   git filter-repo --strip-blobs-bigger-than 1K
   ```
   Or use [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) — it's built for exactly this.

   If other people use this repo, tell them what happened. They need to pull fresh after you force-push the cleaned history.

## Why this happened

Your AI wrote the key directly into the code. That's normal — the AI doesn't know any better. **You** need to move keys into a `.env` file and keep that file out of Git. That's the whole lesson.

## The rule to remember

- Keys go in `.env`. `.env` goes in `.gitignore`. `.gitignore` means "Git, don't upload this."
- If a key ever touches GitHub, assume it's public and revoke it.

## No shame

89,000+ people did this. The AI put it there, you pushed it, bots found it. It happens to everyone once. Now you know the `.env` rule and it won't happen twice.

---

## Never panic about this again

Unloopr's secret scanner catches leaked keys in your code before they ship — not after the bots find them.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
