# Unloopr engineering suite

_Last verified: November 17, 2026. This is a map of separate engineering capabilities, **not** a claim that seven public products are available._

**Find the failure. Prove the fix. Keep the work.** Start with [Unloopr's free scanner](https://unloopr.com/scan) or the [live seven-role suite overview](https://unloopr.com/suite). The rest of the workflow has separate local, integrated or internal access. It is not a one-click service and should not be marketed as one.

## The seven roles

| Step | Component | What it actually does | Current availability |
| --- | --- | --- | --- |
| 01 / Diagnose | **Unloopr** | Check selected pasted code and public GitHub repositories for covered patterns; explain findings that a person must verify. | **Public free website scanner** at [unloopr.com/scan](https://unloopr.com/scan); authenticated MCP separately |
| 02 / Review | **Handroll Rehab** | Flag handwritten code that may merit a maintained library or native API. A finding is a review candidate, not proof of a defect. | **Local-only, read-only** audit; no hosted automatic rewrite |
| 03 / Reuse | **Lego Builder** | Research donor implementations, licenses, tests and provenance before assembling a minimal, evidence-backed integration. | **Research-first engineering workflow**, not a hosted code writer or a public checkout |
| 04 / Protect | **Overwrite Guard** | Replay banked real-use MCP observations, inspect field-level differences and block known contradictions. | **Standalone opt-in local/CI gate**; no automatically installed hooks |
| 05 / Govern | **AgentGit** | Fence agent attempts and workspaces, retain evidence and require independent reproduction at stronger gates. | **Engineering component**; no separate public web signup |
| 06 / Verify | **StateLayer** | Track release evidence with freshness and dependency invalidation, including an explicit UNKNOWN when proof is missing. | **Internal preview**, not a sold service |
| 07 / Reclaim | **Sweepr** | Plan, salvage, verify and reclaim eligible agent worktrees and clones using `agentgit reclaim`. | **Integrated into AgentGit**; no separate subscription |

Only **Unloopr** is a public, self-service web scanner today. The component descriptions above are narrower than the team's internal engineering ambitions.

## How the workflow fits together

1. **Diagnose:** Scan with Unloopr. If a local code audit is available, use Handroll Rehab to identify candidate handwritten code worth reviewing.
2. **Research before rewriting:** Use Lego Builder to find a maintained donor. Check its source, pinned revision, license, tests and compatibility. Do not replace code just because a search returned a candidate.
3. **Protect:** Use Overwrite Guard **when explicitly configured** to replay the observations that matter. Recorded behavior is not exhaustive.
4. **Govern and verify:** AgentGit helps isolate the work and preserve independent proof. StateLayer is an internal release-state preview, not a substitute for verifying the live service and source revision.
5. **Reclaim:** Use Sweepr through AgentGit only after reviewed plans and preservation checks.

No step gives agents permission to edit your repository, purchase a subscription, deploy or delete data without its own authorization.

## Start here and get help

- **Try now:** [Free public GitHub scan](https://unloopr.com/scan) or [paste a code snippet](https://unloopr.com/). Neither guarantees complete bug or security coverage.
- **Agent connection:** [MCP setup](ide-setup.md). The authenticated MCP endpoint is `https://mcp.unloopr.com/mcp`; follow OAuth discovery rather than substituting the branded host as the issuer.
- **Availability:** [Current product status](current-product.md) and [live status](https://unloopr.com/status).
- **Technical report:** [Open a sanitized public issue](https://github.com/jabbertones-cloud/unloopr_support/issues/new/choose). Choose the affected component only if you actually use it; otherwise choose “Other / not sure.” Never post private code or keys.
- **Billing or accounts:** Use [private support](https://unloopr.com/support). Founder ($9/month) and Pro ($19/month) checkout remained **unavailable (HTTP 503)** in the November 17 live check.

## Source and release evidence

The seven-role website update was merged in [Unloopr PR #180](https://github.com/jabbertones-cloud/unloopr/pull/180) and deployed on **November 17, 2026** at exact source commit `a11974cb61e0cd23a6e85745ba05b4a017d2fad2`.

- Cloudflare Worker: `unloopr-com` version `12798e66-480d-4ad1-a019-a4245e8014a3`, **100% traffic**, verified with Cloudflare's deployment listing.
- Live `/suite`, `/`, `/llms.txt` and `/sitemap.xml`: HTTP 200 and byte-identical to the verified candidate; `/scan` and `/support`: HTTP 200.
- Protected Founder and Pro checkout routes: HTTP 503; account-billing status: HTTP 503. GitHub OAuth error callback and canonical redirects retained.
- Source: [the merged Worker site](https://github.com/jabbertones-cloud/unloopr/blob/a11974cb61e0cd23a6e85745ba05b4a017d2fad2/site/worker.js) and the linked evidence in its `.lego/research` folder. The published app-directory status is **not independently verified**.
- QA: 24 focused site tests passed and the local suite page passed automated Playwright/axe checks at 280, 320, 375, 768 and 1440 px. This does **not** establish human usability, full language coverage or 100% defect detection.

The [November 10 release](https://github.com/jabbertones-cloud/unloopr/blob/9e457961123bde3b3998e21a4736282ef9b9ef28/site/worker.js) was superseded by this November 17 website release. Neither release is evidence that all component workflows are commercially available.
