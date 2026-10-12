# What is a commit?

A commit is a **save point** for your code.

## The plain-English version

Imagine writing a document. Every so often you hit save. A commit is that save — but smarter. It remembers exactly what changed, when, and lets you go back to any save point later.

Each commit has:
- **What changed** — the actual code differences.
- **A message** — a short note you write, like "fix login button."
- **A timestamp** — when you saved.

## The three steps

```bash
git add .          # pick your changes (put them in the box)
git commit -m "what I did"   # save the box with a label
```

That's a commit. It's on your computer. Nobody else sees it until you push.

## Why commits matter

- **Undo.** Broke something? Go back to the last commit that worked.
- **History.** See what changed and when — and why (that's what the message is for).
- **Sharing.** Push sends your commits to GitHub so others can see them.

## See also

- [What is the difference between git commit and git push?](commit-vs-push.md)
- [How do I undo my last commit?](../panic/undo-last-commit.md)

---

## Never panic about this again

Connect your repo and Unloopr will show you what your commits actually contain — in words you'll understand.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
