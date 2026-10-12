# What is the difference between git commit and git push?

Short version: **commit = save on your computer. Push = upload to GitHub.**

## Commit

`git commit` saves a snapshot of your changes **on your own computer**. Nobody else can see it. It's like saving a document — it's on your hard drive, not on the internet.

## Push

`git push` **uploads** your commits to GitHub (or wherever your remote is). Now it's backed up online and other people can see it. It's like emailing the saved document to someone.

## The mnemonic everyone uses

**add → stage, commit → save, push → upload.**

1. `git add` — pick which changes to include (put them in the box).
2. `git commit` — save the box on your computer.
3. `git push` — upload the box to GitHub.

## The common confusion

"I committed but my code isn't on GitHub!" That's because **commit doesn't upload anything**. You still need to push. This trips up everyone coming from tools where "save" means "save to the cloud."

## Can you push without committing?

No. Push uploads **commits**. No commits, nothing to upload. The order is always: add → commit → push.
