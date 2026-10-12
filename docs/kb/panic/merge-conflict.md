# Merge conflict — how do I fix it?

Don't panic. A merge conflict means Git found two changes to the same lines and doesn't know which one you want. **Your code is not broken. Nothing is destroyed.**

**Asked by 1,787,101+ people on GitHub. This is the most-asked question in the history of Git.**

## What you're seeing

Lines like this in your file:

```
<<<<<<< HEAD
your version of the code
=======
their version of the code
>>>>>>> branch-name
```

This is Git saying: "You both changed this spot. Pick one — or combine them."

## The fix, step by step

1. **Open the file** with the conflict markers.
2. **Read both versions.** The top part (after `<<<<<<< HEAD`) is yours. The bottom part (before `>>>>>>>`) is theirs.
3. **Delete the markers** (`<<<<<<<`, `=======`, `>>>>>>>`) and keep the code you want. You can keep yours, theirs, or mix both.
4. **Save the file.**
5. Tell Git you're done:
   ```bash
   git add <the file>
   git commit
   ```

That's it. The conflict is resolved.

## The escape hatch

If it's a mess and you want to start over:

```bash
git merge --abort
```

This cancels the merge completely. Everything goes back to how it was before you tried. No harm done.

## The rule to remember

A merge conflict is a **question**, not an error. Git is asking you to choose. Pick the code you want, delete the markers, commit.

## No shame

1.7 million people asked this. Merge conflicts scare everyone the first ten times. After that, they're just Tuesday.
