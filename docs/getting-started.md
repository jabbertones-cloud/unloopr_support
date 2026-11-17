# Getting started with Unloopr

_Updated for the November 17, 2026 website release. The authenticated MCP connection details below were last independently checked on November 10._

## Scan a public GitHub repository

1. Open [unloopr.com/scan](https://unloopr.com/scan).
2. Paste a public repository URL, for example `https://github.com/githubtraining/hellogitworld`.
3. Run the free scan and read the returned findings. If there are none, it means no covered rules were triggered in that run, not that the repository is guaranteed bug-free.
4. Open a finding to understand what may be wrong, why it matters, and what to verify after a change.

The public website scan does **not** need a GitHub login or payment card. It currently allows up to three public repo scans per day and can return fewer than three findings. Private repository scans are **not** offered through this URL.

## Scan pasted code

On [Unloopr's homepage](https://unloopr.com/), choose **Paste your broken code**, pick a language if needed, then scan. Remove passwords, access tokens, customer information, and confidential code first. You are responsible for reviewing and testing any suggested fix.

## Connect GitHub or an AI agent

You can [install the GitHub App](https://github.com/apps/unloopr-code-coach/installations/new) and select repositories. Review permissions before authorizing. The installation is not the same as an automatic code-fix service.

An MCP-capable coding client may connect using `https://mcp.unloopr.com/mcp` and OAuth discovery. The authorization issuer remains the existing workers.dev endpoint. A plain browser GET to `/mcp` is not an MCP client connection test.

Unloopr's publication in the ChatGPT directory has **not been independently confirmed**. Do not assume it can be found in the app directory until its listing is verified.

## Explore the other engineering roles\n\nThe [seven-role engineering suite](suite.md) explains when to use Handroll Rehab, Lego Builder, Overwrite Guard, AgentGit, StateLayer and Sweepr. These are **not included as hosted features** simply because the website lists them. Only the free Unloopr scanner is public self-service today.\n\n## Plans and help

Free web scans work without checkout. [Founder and Pro checkout is not open yet](pricing.md). If a connection or scan fails, see [troubleshooting](troubleshooting.md) or [private support](https://unloopr.com/support). For technical reports without secrets, use the [public issue form](https://github.com/jabbertones-cloud/unloopr_support/issues/new/choose).
