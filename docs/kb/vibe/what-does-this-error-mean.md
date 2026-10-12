# What does this error mean?

**You don't need to understand the whole error.** You need three things: what broke, where, and what to try. Here's how to read any error message.

## The 30-second method

Error messages look scary, but they follow a pattern. Look for:

**1. The error type (the first line).** This is the category:
- `TypeError` — you tried to do something with a value that can't do it (like reading a property of `undefined`).
- `ReferenceError` — you used a name that doesn't exist (typo, or forgot to import).
- `SyntaxError` — the code itself is malformed (missing bracket, bad punctuation).
- `404` — the thing you're asking for doesn't exist (wrong URL).
- `CORS` — the browser blocked the request ([what's CORS?](../panic/cors-error.md)).

**2. The file and line number.** It'll say something like `app.js:42`. That's where to look. Open that file, go to that line.

**3. The message in plain words.** Ignore the codes. Read the sentence: "Cannot read properties of undefined (reading 'name')" means "you tried to read `.name` from something that doesn't exist."

## What to do next

1. **Read the first line only.** The rest is usually noise.
2. **Go to the file and line.** Look at what's there.
3. **Ask:** "What's `undefined` (or missing, or wrong) on this line?"
4. **Paste the first line into Unloopr** (or your AI) and ask: "Explain this in plain English and tell me how to fix it."

## The most common one

```
TypeError: Cannot read properties of undefined
```

Translation: "Your code expected something to exist, and it didn't." Usually a variable that's empty, a missing API response, or a typo. Check the line — find what's empty.

## The rule to remember

Errors are **directions**, not verdicts. The first line tells you the category. The file:line tells you where. That's enough to start.

## No shame

"What does this error mean?" is the most human question in programming. Everyone asks it. The skill isn't knowing — it's knowing how to read.

---

## Never panic about this again

Unloopr translates scary errors into plain English — what broke, why it matters, and the exact fix.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
