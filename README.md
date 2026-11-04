# Unloopr support

Get unstuck when a code scan, agent connection or explanation does not work.

**[Search issues](https://github.com/jabbertones-cloud/unloopr_support/issues)** · **[Report a bug](https://github.com/jabbertones-cloud/unloopr_support/issues/new/choose)** · **[Read agent instructions](AGENT-GITHUB-ISSUES.md)**

## Find an answer first

Search the [open and closed issues](https://github.com/jabbertones-cloud/unloopr_support/issues?q=is%3Aissue) for your symptom or MCP tool name. You may find a workaround without opening a new report.

- [Getting started](docs/getting-started.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq/faq.md)
- [Glossary](https://unloopr.com/terms)

## Report a problem

1. Select **Report a bug** and choose the matching issue form.
2. Describe what you tried, what happened and the result you wanted. Include the affected Unloopr feature, your AI tool or MCP client and safe reproduction steps. You do not need to know coding terminology.
3. Remove passwords, access tokens, customer information, private source code, screenshots with personal data and raw logs before posting.
4. Submit and keep the issue URL so you or your agent can check replies.

**Do not publish private or security information.** Use [private product support](https://unloopr.com/support) when the details cannot be shared publicly. Read [Security](SECURITY.md) before reporting a vulnerability.

## Use an AI agent to get help

An agent with a separately authorized GitHub connection can search issues, read the full discussion, prepare a safe report and, when requested, create an issue or post a reply. The maintained [GitHub MCP Server](https://github.com/github/github-mcp-server) exposes these issue operations. The product MCP does **not** automatically give the agent GitHub permissions.

Ask your agent: **"Check existing Unloopr support issues for this error and tell me whether there is a fix or workaround."**

To file a report, ask: **"Prepare a public bug report with safe details. Search for duplicates, then file it using my GitHub connection."**

If GitHub is not connected, your agent can prepare a report and give you the [new issue form](https://github.com/jabbertones-cloud/unloopr_support/issues/new/choose). It must not claim a ticket was created.

Read [Agent workflow](AGENTS.md) and [GitHub issue operations](AGENT-GITHUB-ISSUES.md).

## What happens next

You can track an issue and respond in its GitHub thread. A maintainer may ask for a minimal reproduction, share a workaround or request a new test. There is no guaranteed response time. A report is not fixed until the affected behavior has been independently checked.

Do not include your private repository name, code, scan report or secrets in an issue. A passing code check is not proof of a fixed deployed application.

## Contribute

Corrections and reusable troubleshooting notes are welcome. See [Contributing](CONTRIBUTING.md) and [Support policy](SUPPORT.md).
