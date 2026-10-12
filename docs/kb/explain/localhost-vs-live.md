# Why does it work on localhost but not on the live site?

**The universal vibe-coder heartbreak.** It works on your computer. You put it online. It breaks. Here's why.

## The plain-English version

`localhost` is **your own computer talking to itself**. When you open `http://localhost:3000`, you're looking at a program running on your machine, for your eyes only.

A live site is a **different computer** (a server) running your program for everyone. Moving from one to the other introduces a dozen things that can go wrong.

## The usual suspects

1. **Environment variables.** Your `.env` file has your API keys and settings — but it doesn't get uploaded (that's the point of `.gitignore`). The live server needs those values set separately, in its own dashboard.

2. **Hardcoded localhost URLs.** Your code says `fetch("http://localhost:3000/api")`. On the live server, there is no localhost:3000. Use relative URLs (`/api`) instead.

3. **Missing build step.** Your computer runs the code directly. The server needs it **built** first (`npm run build`). If the deploy didn't build, it serves nothing.

4. **Ports.** Localhost has a port (`:3000`). Live sites usually don't show one — the server handles that. Don't put port numbers in your live URLs.

5. **Case sensitivity.** Your Mac doesn't care if a file is `Image.png` or `image.png`. The Linux server does. If an image or import is missing live, check the exact filename.

## The rule to remember

Localhost = your computer. Live = someone else's computer. Anything your computer provides for free (env files, ports, case-insensitivity) has to be set up again on the server.

## No shame

"Why does my friend can't open my website http://localhost:3000??" — real question, from a real person. Localhost is your computer's private address. Nobody else can open it. That's the whole point.
