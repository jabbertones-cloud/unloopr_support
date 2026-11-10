# Unloopr engineering suite

_Verified source capabilities: November 10, 2026. Not all components are public products._

**Find the loop. Prove the fix. Keep the work.** Unloopr is the code-coaching front door of a connected engineering workflow. The supporting components have distinct responsibilities; a standalone repository or local command is not evidence of a live hosted customer feature.

| Component | What it does | Availability |
| --- | --- | --- |
| **Unloopr** | Check pasted code and chosen public GitHub repositories for known problems and suggest next steps. Users review and test the fixes. | Free public website scans live at https://unloopr.com/scan; authenticated MCP separate |
| **Overwrite Guard** | Re-run banked real-use MCP behavior against a changed, isolated Git tree; show field-level differences and block known contradictory changes. | Standalone local/CI utility, opt-in, no automatically installed hook |
| **AgentGit** | Coordinate agent attempts, fenced leases, workspaces, evidence attestations, and independent reproduction for higher-assurance merge gates. | Engineering component; no verified separate public subscription |
| **Sweepr** | Review, salvage, and reclaim provably recoverable worktrees/clones using AgentGit's `agentgit reclaim` command. | Integrated into AgentGit; not a separate paid app |
| **StateLayer** | Answer whether an exact source revision is safely live with evidence freshness, conflict handling and dependency-aware invalidation. | Internal preview, not public SaaS |
| **Handroll Rehab** | Read-only audit of custom handwritten code, including local Swift/SwiftUI review candidates and native API alternatives. | Local-only, not a hosted automatic rewrite tool |

## How the pieces connect

1. **Diagnose:** Unloopr returns a bounded analysis, not a guarantee of security or complete code correctness.
2. **Protect:** Where configured by an engineering operator, Overwrite Guard replays trusted observations and identifies regressions against them. A bank covers recorded behavior, not every possible scenario.
3. **Govern:** AgentGit coordinates authorized agent work and evidence, with independent reproduction for its stronger gate.
4. **Verify:** StateLayer may provide internal evidence-backed release state; it does not independently deploy a release.
5. **Recover:** Sweepr can safely reclaim eligible worktrees after a reviewed plan and re-verification.
6. **Review native alternatives:** Handroll Rehab is a local candidate detector, not automated code replacement.

**Do not interpret the sequence as a live one-click workflow.** Each component has separate access, prerequisites, authorization, and proof boundaries.

The planned website overview is https://unloopr.com/suite. Use https://unloopr.com/status for actual live availability, and https://unloopr.com/support for help. Founder and Pro checkout remain unavailable while billing verification is incomplete; the ChatGPT directory listing has not been independently confirmed.

## Source provenance

Descriptions are derived from first-party source and README contracts in `jabbertones-cloud/unloopr/overwrite_guard`, `jabbertones-cloud/agentgit`, and `jabbertones-cloud/StateLayer`. Sweepr is an AgentGit subcommand rather than an independent `jabbertones-cloud/sweepr` repo. Handroll Rehab's local-only boundary is documented in `unloopr-agent/docs/handroll-rehab-swift.md`. Product claims are intentionally narrower than internal architecture ambitions.
