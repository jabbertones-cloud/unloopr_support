# CORS error — blocked

**Your code is probably fine.** CORS errors are the browser's security rules getting in the way, not a bug in what you built.

**Seen in 96,859+ GitHub issues. One of the most common errors vibe coders hit when their app talks to an API.**

## The plain-English version

Your website (running at one address) tried to ask another website (at a different address) for data. The browser said: "Nope. That other site didn't say you're allowed to ask."

This is called CORS — Cross-Origin Resource Sharing. It's a **browser security rule**, not a code bug.

## The fix

**The fix goes on the server, not your website.** The server needs to send back a header that says "yes, that website is allowed to ask me":

```
Access-Control-Allow-Origin: *
```

(or your site's address instead of `*`)

**If you control the API:** add that header to the server's responses. Every framework has a CORS plugin or middleware — search "[your framework] enable CORS."

**If you don't control the API:** you can't fix it from your website. Options:
- Ask the API owner to allow your site.
- Route requests through your own server (a proxy) instead of calling the API directly from the browser.

## The rule to remember

CORS = the browser blocking your site from talking to another site. Fix it on the **server side** by allowing your site's address.

## No shame

CORS confuses senior developers too. It's a security feature with an error message that reads like your code is broken. It's not.

---

## Never panic about this again

Unloopr matches your code against bug patterns mined from thousands of real fixes — and explains each one simply.

**[Unloopr](https://unloopr.com)** is a code coach for your GitHub repos. Connect a repo and get your 3 biggest fixes in plain words — what's wrong, why it matters, how to fix it.

- **Free forever:** 3 fixes per repo. No credit card.
- **Read-only:** Unloopr looks at your code. It never changes it.
- **5 minutes:** connect at [unloopr.com](https://unloopr.com), pick a repo, read your fixes.
