# Unloopr problem ontology — seed

These are routing identifiers. Customer language → stable ID → plain-words concept → public first step.

| Problem ID | Customer language | Plain-words concept | Public first step |
|---|---|---|---|
| `ULP.GIT.UNDO_COMMIT` | "how do I undo my last commit?" | A commit is a saved snapshot; undoing removes the snapshot, not your work | Check whether they pushed yet — unpushed is safe, pushed needs care |
| `ULP.GIT.MERGE_CONFLICT` | "merge conflict — how do I fix it?" | Two people changed the same lines; git can't pick, you pick | Open the file, find `<<<<<<<` markers, keep what you want |
| `ULP.SECRET.LEAKED_KEY` | "I pushed my API key to GitHub" | Bots scan GitHub for keys in seconds; the key is burned | Delete the key at the source, make a new one, `.env` + `.gitignore` |
| `ULP.GIT.WRONG_BRANCH` | "I pushed to the wrong branch" | Commits are safe, just on the wrong branch | Cherry-pick commits to the right branch |
| `ULP.GIT.DETACHED_HEAD` | "what does detached HEAD mean?" | Looking at a commit without being on a branch | `git checkout main` to get back; nothing is broken |
| `ULP.GIT.FORCE_PUSH_LOSS` | "I force-pushed and deleted work" | Rewriting shared history can orphan commits | `git reflog` to find lost commits; talk to the team |
| `ULP.DEPLOY.LOCALHOST_GAP` | "why can't my friend open my localhost link?" | localhost is your own computer; nobody else can reach it | Push to GitHub, connect to a host (Vercel/Railway) |
| `ULP.DEPLOY.ENV_MISSING` | "works on localhost, broken live" | The live site is missing your `.env` values | Add environment variables in the host dashboard |
| `ULP.AI.HALLUCINATED_IMPORT` | "my AI imported a package that doesn't exist" | ~1 in 5 AI-suggested packages aren't real | Search npm for the real name; don't install the fake one |
| `ULP.AI.PLAUSIBLE_WRONG` | "the code looks right but doesn't work" | AI code can look correct and be wrong | Read the error, print values, check the boundaries |
| `ULP.AI.COMMIT_CONFUSION` | "Cursor asked me to commit — what does that mean?" | Commit = save a snapshot before changes | Say yes — it's protecting you |
| `ULP.SETUP.ENV_VARS` | "where do I put my API key?" | Keys live in `.env`, never in code | Create `.env`, add to `.gitignore`, read via environment |
| `ULP.SETUP.GITIGNORE` | "what is a .gitignore file?" | Tells git which files to never track | Add `.env`, `node_modules/`, `*.log` before first commit |
| `ULP.PRICE.CONFUSION` | "what do I get free / what does Pro cost?" | Free = 3 fixes per repo; Founder $9; Pro $19 | Point to pricing doc; no surprise bills, ever |
