# How do I undo my last commit?

Don't panic. Your code is not gone. Here's how to take back your last commit.

**Asked by 119,160+ people on GitHub. You are not the first, and this is easy to fix.**

## The quick answer

If you just committed and haven't pushed yet:

```bash
git reset --soft HEAD~1
```

This undoes the commit but **keeps all your changes**. Your files are exactly as they were. Nothing is lost.

## What just happened

- `git reset --soft HEAD~1` moves the "you committed" marker back one step.
- Your changes stay in place, waiting to be committed again.
- Nothing is deleted. Nothing is uploaded. You're safe.

## If you already pushed

If the commit is already on GitHub, undoing is trickier — because other people may have it. Don't rewrite history on a shared branch. Instead, make a **new commit that undoes the old one**:

```bash
git revert HEAD
```

This creates a fresh commit that reverses what the last one did. Safe for shared branches.

## The rule to remember

- **Not pushed yet?** `git reset --soft HEAD~1` — safe, nothing lost.
- **Already pushed?** `git revert HEAD` — safe for everyone.

## No shame

Everyone does this. The command has "reset" in the name and it sounds scary, but `--soft` means "be gentle." Your work is still there.
