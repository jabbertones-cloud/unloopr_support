# Security and privacy

_Last reviewed for public-support accuracy: November 10, 2026. For binding terms, read the live [privacy policy](https://unloopr.com/privacy) and [terms](https://unloopr.com/terms)._

## Scan only code you can share

- The [public repository scanner](https://unloopr.com/scan) accepts publicly accessible GitHub repository URLs. Do not use it as a private-repository scanner.
- The homepage can analyze code that you paste. **Redact secrets and private information before scanning.** Neither scanner can guarantee that every issue will be detected.
- Connecting the [Unloopr GitHub App](https://github.com/apps/unloopr-code-coach/installations/new) is a separate authorization step. Review its requested permissions and repository selection in GitHub. Revoke access in GitHub settings if needed.
- The authenticated MCP integration uses OAuth; never paste access tokens into a public report or a support issue.

A free scan returns guidance; it does not grant blanket permission to edit a repository. Do not infer automatic pull requests, direct writes, or continuous monitoring from the presence of a GitHub App connection.

## If a secret leaked

Revoke or rotate the exposed credential with its provider immediately; removing a line from a Git commit does not invalidate an already exposed token. Then check history and your deployment secrets. See [the FAQ](faq/faq.md#i-pushed-my-api-key-to-github--what-now).

## Ask for help privately

Use [Unloopr private support](https://unloopr.com/support) for accounts, personal information and billing. For vulnerabilities, follow [SECURITY.md](../SECURITY.md); do not post exploit details or keys in public GitHub issues.

## Data claims

The live privacy policy describes operational telemetry, coaching outcomes, and processing of submitted code. It is the policy source of truth. Do not promise instant deletion of all account data or claim that the service never receives identifiers when a user authorizes an external connection. Ask support about a specific deletion request.
