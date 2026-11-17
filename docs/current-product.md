# What Unloopr does today

_Website, suite and protected-route verification: November 17, 2026. MCP discovery observations below date to November 10 unless stated. This is a product-status reference, not a promise of future features._

## What is Unloopr?

Unloopr is a code coach for people building apps with AI tools. It checks selected code for known errors and security mistakes, such as unsupported imports or secret-shaped values, and returns findings with explanations. A scan can legitimately return no findings. Unloopr is advisory: you must review and test changes before shipping.

## What else is in the engineering suite?

See [the seven-role suite map](suite.md) for **Unloopr**, **Handroll Rehab** (local read-only candidate detection), **Lego Builder** (research-first donor selection and source-provenance checks), **Overwrite Guard** (opt-in local/CI regression replay), **AgentGit** (agent work and evidence controls), **StateLayer** (internal release-state preview) and **Sweepr** (safe reclaim through `agentgit reclaim`). Only the free Unloopr scanner is public self-service today. The other engineering tools are **not** a bundled public service, one-click repair flow or seven separate paid products.

## User consent for promotional or testimonial tools

A November 17 code update merged safeguards requiring explicit user initiation for promotional and testimonial MCP operations. A routine scan, support question or GitHub App connection must not be treated as consent to generate, send, or publish sales material. The source update has not been independently verified on the deployed MCP service in this support review; the website's free-scan and checkout status remains separately documented below.

## Can I scan a GitHub repository for free?

Yes, **public repositories** can be submitted at https://unloopr.com/scan using a `https://github.com/owner/repo` URL. No GitHub account or credit card is needed for this website route. The website currently advertises **up to three public repository scans per day**. It shows a limited set of findings, not an unlimited audit.

A live probe of an explicitly public sample repository on November 10 returned HTTP 200, `files_scanned: 15`, and zero findings. This proves the route processed that sample; it does not prove full coverage of every language or repository.

## Can I paste code without GitHub?

The homepage has a free snippet-scanning form. It processes submitted code to produce findings; redact secrets before submitting. Website rate limits may apply. Don't post confidential source in a public issue.

## Can I connect an AI coding agent?

The authenticated MCP endpoint is `https://mcp.unloopr.com/mcp`. Use a supported MCP client with the advertised OAuth flow. On November 10, unauthenticated MCP initialize requests returned HTTP 401 as expected. The authorization metadata advertised the existing issuer `https://unloopr-mcp.smatdesigns.workers.dev`; the branded hostname does not replace that issuer. A GET request's 404 is not evidence that authenticated MCP POST is broken.

The hosted service advertises failure-mode guidance, diff checks, reporting, feedback/outcomes, and related coaching utilities. Tool availability can depend on authentication and entitlements.

## Does Unloopr edit my repository?

A free scan reports findings and possible fixes; it does not authorize automatic writes to your repository. GitHub App connection is separate and requires selecting permissions. Do not assume continuous monitoring, one-tap repair, or automatically opened fix branches until that specific flow has been demonstrated.

## Is payment available?

Not yet verified for customer use. On November 17, both `/billing/start?plan=founder` and `/billing/start?plan=pro` returned HTTP 503. The site advertises Founder at $9/month and Pro at $19/month, but the checkout and paid entitlements must be independently verified before the site can accept subscriptions. Free scanning does not require a card.

## Is Unloopr in the ChatGPT app directory?

Public listing and review completion have not been verified. The MCP endpoint is not itself evidence of a published ChatGPT directory app. Refer to https://unloopr.com/support for the confirmed connection instructions when available.

## What languages does Unloopr support?

The website presents a range of common stacks, including Python, JavaScript/TypeScript, Go, Swift, Rust, Java, C/C++, C#, PHP, Kotlin, Ruby, and Dart. Detection depends on the rule and input. An absence of findings is not a guarantee of correctness.

## Where can I get help?

Use https://unloopr.com/support for account and private inquiries, or https://github.com/jabbertones-cloud/unloopr_support/issues for sanitized, non-sensitive technical reports. Search existing issues first. Never submit exposed keys, private code or personally identifiable information in a public issue.

## Status evidence and boundaries

- November 17 live web checks: `/`, `/suite`, `/scan`, `/support`, `/llms.txt` and `/sitemap.xml` returned HTTP 200. The revised website serves exact-main source `a11974cb61e0cd23a6e85745ba05b4a017d2fad2` through Worker version `12798e66-480d-4ad1-a019-a4245e8014a3` at 100% production traffic. The older November 10 sample GitHub scan processed 15 files and returned zero findings; it was not re-run as part of the November 17 website release.
- Live paid routes: Founder and Pro checkout returned 503, fail-closed.
- Historical November 10 MCP check: `https://mcp.unloopr.com/mcp` returned a 401 auth challenge to unauthenticated JSON-RPC POST; OAuth metadata advertised the existing issuer. No fresh authenticated MCP test is claimed from the November 17 website release.
- Release proof: [merged PR #180](https://github.com/jabbertones-cloud/unloopr/pull/180), exact-main source commit and Cloudflare Worker version listed above. Outstanding work and separate OpenAI reviews must not be presented as released merely because the site deployed.

Do not convert planned functions or local tests into live claims. This document is written for humans, support agents, and search systems alike.

