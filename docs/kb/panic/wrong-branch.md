# I pushed to the wrong branch — what now?

Don't panic. The code is not lost. It's just in the wrong place. Here's how to move it.

## The fix

**Step 1: Go to the branch you pushed to by accident.**

```bash
git checkout <wrong-branch>
```

**Step 2: Undo the push there.**

```bash
git reset --hard HEAD~1
git push --force-with-lease
```

This removes your commit from the wrong branch. (`--force-with-lease` is the safe version of force-push — it stops if someone else pushed since.)

**Step 3: Go to the right branch and put the commit there.**

```bash
git checkout <right-branch>
git cherry-pick <the commit>
git push
```

Done. The commit now lives on the correct branch.

## If the wrong branch is shared with other people

Skip the force-push. Instead, use `git revert` on the wrong branch (which makes a clean "undo" commit), then `git cherry-pick` onto the right branch. No history rewriting, no one else affected.

## The rule to remember

Commits can be moved. `cherry-pick` copies a commit onto whatever branch you're on. Nothing is ever truly stuck on the wrong branch.

## No shame

Branches have confusing names. Everyone pushes to the wrong one eventually. The fix takes two minutes.
