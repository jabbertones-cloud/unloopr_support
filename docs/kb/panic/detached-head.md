# What does "detached HEAD" mean?

**Nothing is broken. Your code is fine.** "Detached HEAD" sounds terrifying. It's not.

## The plain-English version

Think of a branch as a bookmark in a book. Normally, your bookmark moves forward as you read (commit).

"Detached HEAD" means **your bookmark fell out**. You're still on the same page. You can still read. But if you write new pages (commits) now, they won't be attached to any bookmark — and you could lose track of them.

## How you got here

You probably checked out a specific commit, a tag, or a pull request — instead of a branch. That's all. Git is just warning you: "Hey, you're not on a branch right now."

## The fix

Get back on a branch:

```bash
git checkout <your-branch-name>
```

That's it. Bookmark back in the book.

If you made commits while detached and want to keep them:

```bash
git checkout -b new-branch-name
```

This creates a new branch exactly where you are, saving those commits.

## The rule to remember

Detached HEAD = "you're not on a branch." Get back on one with `git checkout`, and everything is normal again.

## No shame

The name is awful. It sounds like something snapped off. It's just Git being dramatic about a missing bookmark.

---

## Never panic about this again

Unloopr explains your repo in plain words — what state it's in, what that means, what to do next.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
