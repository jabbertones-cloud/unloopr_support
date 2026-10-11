# FAQ — Things people actually ask

## How do I undo my last commit?

Don't panic. If you haven't pushed yet:

```
git reset --soft HEAD~1
```

Your changes stay. The commit goes away. If you already pushed, ask us before you force-push — that's how work gets deleted.

## I pushed my API key to GitHub — what now?

Act fast. Bots scan GitHub for keys in seconds.

1. Delete the key where you made it (Stripe dashboard, OpenAI settings, etc.)
2. Make a new key
3. Put the new key in a `.env` file — never in your code
4. Add `.env` to your `.gitignore`

The old key is burned. Don't reuse it.

## Merge conflict — how do I fix it?

A merge conflict means two people changed the same lines. Git can't pick. You pick.

1. Open the file — look for `<<<<<<<` markers
2. Keep the lines you want, delete the markers
3. Save, then `git add` the file and commit

It feels scary the first time. It's normal. Everyone gets these.

## How do I put my app online?

Your app runs on `localhost` — that's your own computer. Nobody else can reach it.

To put it online ("deploy"), you need a host. Easiest paths:
- **Vercel / Netlify** — connect your GitHub repo, they handle the rest
- **Railway / Render** — for apps with a backend

Push your code to GitHub first. Then connect the repo to the host.

## Why does it work on localhost but not on the live site?

Common causes, in order:

1. **Environment variables** — your `.env` file didn't get uploaded. Add them in your host's dashboard.
2. **API URLs** — your code calls `http://localhost:3000/api`. Change it to your live URL.
3. **Build vs dev** — some things only break in the production build. Check your host's build logs.

## Cursor asked me to commit — what does that mean?

"Commit" means "save a snapshot of my code." Cursor wants to save your progress before it changes things — so you can undo if something breaks. Say yes. It's protecting you.

## What does this error mean?

Copy the error message and search it in our [glossary](https://unloopr.com/terms). If it's not there, open an issue — we'll explain it and add it.

## I force-pushed and deleted work — can I get it back?

Don't panic. Maybe.

**If it was your own repo and you have the commits locally:** your work still exists in your local git history. `git reflog` shows every move your repo ever made — find the commit hash from before the force-push, then `git reset --hard <hash>` to go back to it.

**If it was a shared repo and teammates pulled the rewritten history:** talk to your team first. Everyone needs to re-sync, and force-pushing shared branches is how trust gets broken. The work isn't necessarily gone — but the cleanup is social, not just technical.

**Prevention:** never force-push a branch someone else uses. If git rejects your push, that's git protecting you — read *why* before overriding it.

## What is a .gitignore file?

A `.gitignore` file tells git which files to never track. Secrets, build output, dependencies — the stuff that should never end up in a repo.

Create a file called `.gitignore` in your repo root. Each line is a pattern:

```
.env
node_modules/
*.log
```

**The one rule:** put `.env` in there before your first commit. 89,000+ leaked API keys on GitHub started as "I'll add it later."

## Where do I put my API key?

Not in your code. Ever.

1. Create a file called `.env` in your project folder (same folder as your code, not inside a subfolder).
2. Put your key there: `STRIPE_KEY=sk_live_abc123`
3. In your code, read it from the environment: `process.env.STRIPE_KEY` (Node) or `os.environ["STRIPE_KEY"]` (Python).
4. Add `.env` to your `.gitignore` so it never gets committed.

Your host (Vercel, Railway, etc.) has a dashboard section for environment variables — add the same keys there for the live site. Your `.env` file stays on your computer only.

## I pushed to the wrong branch — what now?

Don't panic. Your code isn't lost — it's just on the wrong branch.

1. **Don't touch the wrong branch yet.** Your commits are safe there.
2. Switch to the right branch: `git checkout correct-branch`
3. Bring your commits over: `git cherry-pick <commit-hash>` for each commit (find hashes with `git log` on the wrong branch).
4. Once the right branch has everything, you can clean up the wrong one.

**If you haven't pushed yet**, it's even easier — just rename your local branch: `git branch -m wrong-name right-name`.

## What does "detached HEAD" mean?

It means you're looking at a commit, but you're not on any branch. Like reading a page with no bookmark — you can read, but if you make changes, git won't remember where to keep them.

**You didn't break anything.** To get back: `git checkout main` (or whatever your branch is called).

**If you made changes while detached** and want to keep them: `git checkout -b my-new-branch` — that gives your work a branch to live on.

## Why is my push rejected?

Git rejected your push because the remote has changes you don't have locally. It's protecting you from overwriting someone else's work.

1. Pull first: `git pull`
2. If there are conflicts, fix them ([how to fix a merge conflict](#merge-conflict--how-do-i-fix-it))
3. Push again.

**Don't** reach for `--force` to make the error go away. That's how work gets deleted.

## My AI imported a package that doesn't exist — what now?

This happens more than you'd think — about 1 in 5 AI-suggested packages aren't real. (Attackers even register the fake names to steal data. It's called slopsquatting.)

1. **Don't install it.** If `npm install` fails with "not found," that's actually good news — it means the package doesn't exist rather than being malicious.
2. Search [npmjs.com](https://www.npmjs.com) for the real package name — it's usually one letter off from what the AI wrote.
3. Replace the import with the correct name.
4. Tell your AI what the right package is so it doesn't do it again.

Unloopr flags these automatically — hallucinated imports are the first thing the harness checks.

## The code looks right but doesn't work — what do I do?

This is the hardest kind of bug, and the most common with AI-generated code. It *looks* right. It passes a quick glance. But it's wrong.

1. **Read the error, not the code.** The error message tells you what's actually happening. Copy it and search our [glossary](https://unloopr.com/terms).
2. **Check your assumptions.** Print values with `console.log` (or `print`). The variable you think holds a user probably holds `undefined`.
3. **Check the boundaries.** Most "looks right" bugs live at edges: empty lists, missing files, network failures, wrong types.
4. **Ask Unloopr.** Scan the repo — the tutor has seen this bug shape before and will explain it in plain words.

The lesson: "looks right" is not a test. Running it is.

---

*More terms: [unloopr.com/terms](https://unloopr.com/terms) — 105 explained in plain words.*
