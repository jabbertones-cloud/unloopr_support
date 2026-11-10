# Connect Unloopr to a coding agent

_Last verified: November 10, 2026. Connection screens may differ by client._

Unloopr is a code coach for people building with AI. Its authenticated MCP service provides failure-mode guidance, diff checks, and reports so you can review and test fixes before shipping.

## Set up a supported MCP client

1. Open your coding tool's MCP integration or server settings.
2. Use **https://mcp.unloopr.com/mcp** as the remote MCP server address.
3. When the client requests authorization, follow its advertised OAuth flow. The current authorization issuer is **https://unloopr-mcp.smatdesigns.workers.dev**. Do not manually replace the issuer or invent a token.
4. Once connected, ask the agent to check a small, non-secret diff. Review the returned findings before making changes.

The `/mcp` endpoint uses authenticated HTTP requests. Opening it as a website in a browser is not an MCP connectivity test. An unauthenticated JSON-RPC POST is expected to return a 401 authorization challenge.

## Can I connect through ChatGPT?

The hosted MCP endpoint is live, but **publication in the ChatGPT app directory has not been confirmed**. Do not assume the app can be selected in the directory. When a verified listing is available, connection instructions will be updated on [Unloopr Support](https://unloopr.com/support).

## Scan without an MCP connection

You can scan a [public GitHub repository](https://unloopr.com/scan) without registering or entering a card, or paste redacted code on the [homepage](https://unloopr.com/). The public website currently allows up to three repo scans a day, independent of authenticated MCP coaching allowances.

## Troubleshoot safely

If a coding tool shows a 401, confirm that its OAuth connection completed; do not paste credentials or raw tokens into a support issue. If the server shows no tools after authorization, check the client connection and its negotiated permissions. If a scan shows no findings, that does not mean all code is safe.

Use [troubleshooting](troubleshooting.md), the [current product status](current-product.md), or [public issues](https://github.com/jabbertones-cloud/unloopr_support/issues) for sanitized questions. Private account or billing help is at [unloopr.com/support](https://unloopr.com/support).
