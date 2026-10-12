# My AI built an app — how do I put it on GitHub?

Your AI made the app. Now you want it safe on GitHub. Here's the whole thing, no jargon.

## Step by step

**1. Make a GitHub account** at [github.com](https://github.com) if you don't have one. It's free.

**2. Create a new repository.** Click the **+** in the top-right → **New repository**. Give it a name. Keep it **private** if you're not ready to share. Click **Create repository**.

**3. In your project folder, run these commands** (in the terminal — the black window where you type commands):

```bash
git init
git add .
git commit -m "my app"
git branch -M main
git remote add origin https://github.com/YOUR-NAME/YOUR-REPO-NAME.git
git push -u origin main
```

Replace `YOUR-NAME` and `YOUR-REPO-NAME` with yours. GitHub shows you these exact commands on the new repo page — you can copy them from there.

**4. Done.** Refresh the GitHub page. Your code is there.

## What just happened

- `git init` — turned your folder into a Git project.
- `git add .` — picked up all your files.
- `git commit` — saved them as a snapshot.
- `git push` — uploaded the snapshot to GitHub.

## Before you push: check for secrets

If your app uses API keys, **don't push yet**. Read [Where do I put my API key?](../explain/where-api-key-goes.md) first. Keys in your code + GitHub = bots steal them in seconds.

## See also

- [How do I put my app online?](put-app-online.md) — the next step after GitHub
- [What is a commit?](../explain/what-is-commit.md)
