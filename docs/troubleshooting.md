# Unloopr troubleshooting index

Start from what the person sees, not from internal names.

| Symptom / search phrase | Problem ID | Next step |
|---|---|---|
| "How do I undo my last commit?" | `ULP.GIT.UNDO_COMMIT` | If not pushed: `git reset --soft HEAD~1`. If pushed: ask before force-pushing. |
| "Merge conflict — how do I fix it?" | `ULP.GIT.MERGE_CONFLICT` | Open the file, resolve `<<<<<<<` markers, `git add`, commit. |
| "I pushed my API key to GitHub — what now?" | `ULP.SECRET.LEAKED_KEY` | Delete key at source → new key → `.env` → `.gitignore`. Act fast. |
| "I pushed to the wrong branch" | `ULP.GIT.WRONG_BRANCH` | Cherry-pick commits to the right branch. |
| "What does detached HEAD mean?" | `ULP.GIT.DETACHED_HEAD` | `git checkout main`. Nothing is broken. |
| "I force-pushed and deleted work" | `ULP.GIT.FORCE_PUSH_LOSS` | `git reflog` → find pre-push hash → `git reset --hard`. Talk to the team. |
| "Why can't my friend open my localhost link?" | `ULP.DEPLOY.LOCALHOST_GAP` | Push to GitHub → connect to Vercel/Railway/Render. |
| "Works on localhost, broken on the live site" | `ULP.DEPLOY.ENV_MISSING` | Add env vars in host dashboard; check API URLs. |
| "My AI imported a package that doesn't exist" | `ULP.AI.HALLUCINATED_IMPORT` | Don't install it. Search npm for the real name. |
| "The code looks right but doesn't work" | `ULP.AI.PLAUSIBLE_WRONG` | Read the error, print values, check boundaries. |
| "Cursor asked me to commit — what does that mean?" | `ULP.AI.COMMIT_CONFUSION` | Say yes. Commit = snapshot before changes. |
| "Where do I put my API key?" | `ULP.SETUP.ENV_VARS` | `.env` file + `.gitignore`. Never in code. |
| "What is a .gitignore file?" | `ULP.SETUP.GITIGNORE` | Add `.env`, `node_modules/`, `*.log` before first commit. |
| "What do I get free?" | `ULP.PRICE.CONFUSION` | 3 fixes per repo, forever. Pricing doc for the rest. |

## Escalation rule
Search the FAQ and glossary first. Teach the lesson second. Open an "I'm stuck" issue only when the person is still stuck.
