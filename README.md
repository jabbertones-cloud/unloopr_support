# Unloopr Support

**Break the loop.** [Unloopr](https://unloopr.com/) is a code coach for people building with AI. It checks submitted code and selected public GitHub repositories for known failure patterns, then explains findings and possible next steps in plain English. The user reviews and applies changes.

[Scan a public GitHub repo](https://unloopr.com/scan) · [Get support](https://unloopr.com/support) · [Search help issues](https://github.com/jabbertones-cloud/unloopr_support/issues) · [Report a bug](https://github.com/jabbertones-cloud/unloopr_support/issues/new/choose)

## The engineering suite

[Explore the complete suite](docs/suite.md) or [view its live website](https://unloopr.com/suite): Unloopr, Overwrite Guard, AgentGit, Sweepr, StateLayer and Handroll Rehab. Overwrite Guard is an opt-in local/CI behavior-replay gate, not the free website scanner. Sweepr is part of AgentGit; StateLayer and Handroll Rehab remain internal/local.

## Start with what works today

- **Public repository scan:** Paste a public `github.com/owner/repo` URL at [unloopr.com/scan](https://unloopr.com/scan). No account is required. The website currently limits public repo scans to three per day. Reports may return fewer than three findings, including zero.
- **Paste a code snippet:** Use the free code-scan form on [unloopr.com](https://unloopr.com/). Do not submit live credentials or confidential code.
- **GitHub App connection:** [Connect the Unloopr GitHub App](https://github.com/apps/unloopr-code-coach/installations/new) and choose repositories. Grant only the permissions you intend to grant; installing the app is not proof of automatic fixes.
- **MCP for AI coding agents:** The authenticated MCP service is at [mcp.unloopr.com/mcp](https://mcp.unloopr.com/mcp). It offers code-checking, guidance, reports and outcome tools. The existing OAuth authorization-server issuer is `https://unloopr-mcp.smatdesigns.workers.dev`; clients must follow its discovery response. A browser GET is not a connection test: the MCP endpoint is an authenticated HTTP protocol endpoint.

## Availability, not promises

- Free web scans are available now. The website's three-scans-per-day limit is separate from hosted MCP coaching-loop entitlements and from the number of findings shown.
- Founder ($9/month) and Pro ($19/month) are advertised plans, **not open checkout** as of November 10, 2026. Both purchase URLs currently return HTTP 503 intentionally. Do not enter payment details or assume an active subscription.
- A ChatGPT directory listing or completed OpenAI review has **not been verified**. Do not tell people to find or install an app in the directory until its publication is confirmed.
- Public repo scans provide findings and guidance. Do not promise one-tap repair, live push monitoring, private repo scanning, or automatic pull requests without a demonstrated product flow.

[Current verified capabilities and status](docs/current-product.md) · [Getting started](docs/getting-started.md) · [Connect your editor](docs/ide-setup.md) · [Pricing and checkout status](docs/pricing.md) · [Security and privacy](docs/security.md) · [FAQ](docs/faq/faq.md) · [Troubleshooting](docs/troubleshooting.md)

## Report a problem safely

Search [existing issues](https://github.com/jabbertones-cloud/unloopr_support/issues) first. To report a bug, describe what you expected, what happened, the product surface, and non-sensitive reproduction steps. **Do not post tokens, API keys, private source, customer data, or raw secret-scanner output.** For billing, accounts, or private information, use [Unloopr private support](https://unloopr.com/support). For vulnerabilities, follow [SECURITY.md](SECURITY.md).

AI agents using an authorized GitHub connection may search issues and prepare sanitized reports. See [AGENTS.md](AGENTS.md) and [AGENT-GITHUB-ISSUES.md](AGENT-GITHUB-ISSUES.md). They must not publish a report without the user's authorization.

_Last product availability check: 2026-11-10. The linked live service and repository can change independently._
