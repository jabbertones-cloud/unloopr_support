# Unloopr knowledge system

## How it works

Customer wording → stable `ULP.*` problem ID → plain-words concept → public explanation → lesson → verification.

The website (unloopr.com/terms) is the canonical public explanation and discovery surface. This repository is the public agent/community/evidence layer.

## The ontology

[problem-ontology.md](problem-ontology.md) holds the stable problem IDs. Each ID maps:

- **Customer language** — the verbatim phrasing people actually use (from support issues, glossary searches, community posts)
- **Plain-words concept** — the one-sentence explanation a tutor would give
- **Public first step** — what to do right now, before anything else

## Rules

- IDs are stable. Never rename one — add a new ID and mark the old one superseded.
- Customer language comes from real quotes, not invented ones. Cite the source (issue #, glossary search, community link).
- Every ID must have a public explanation (FAQ article or glossary term) before it's used in a support case.
- `last_verified` / `review_after` on any ID where tool behavior can drift (AI tools change fast).
