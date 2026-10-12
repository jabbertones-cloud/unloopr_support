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
