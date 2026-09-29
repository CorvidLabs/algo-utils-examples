---
id: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance
state: archived
type: migration
base_commit: 75080733685c28e1a2da2fd639f5bbf5fa9cccab
---

# Adopt SpecSync 5.0.1 and Trust 1.0.0 governance

## Intent

Adopt SpecSync 5.0.1 and Trust 1.0.0 governance

## Affected Canonical Specs

- `algorand-examples`

## Acceptance Criteria

- Ten stable requirements accurately describe the existing account, payment, atomic-group, asset, demonstration, native verification, and Trust boundaries
- The existing Python source, tests, README, dependency files, and CI workflow remain byte-for-byte unchanged
- SpecSync strict coverage passes at 100%; all four agents, Trust doctor, the LocalNet verification lane, and the full Trust gate pass

## No-spec Rationale

Not applicable

## Migration Note

Migrated by hand to SpecSync 6 per Leif's decision (2026-09-28); the 6.0.0 tool refused to archive this legacy record (`` exact-only delivery input `.github/workflows/trust.yml` changed after acceptance and requires an audited reopen; run `specsync change reopen CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance` to re-verify the accepted change, or supersede it from a later change under a module granted the path by `owns` in `.specsync/config.toml` ``).

- Workflow v1 (SpecSync 5) record, accepted on 2026-07-14 by the closing approval already stored in `approvals.json`. SpecSync 6.0.0 reports its accepted evidence as stale, for the reason quoted above.
- Moved by hand from `.specsync/changes/CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance/` into the layout `specsync change archive` writes: `accepted-state.json` is the unchanged accepted `state.json`, `state.json` is marked `archived`, and this file's front matter says `archived`.
- `approvals.json`, `verification.json` and every other artifact are the original SpecSync 5 evidence, unchanged. `verification.json` verifies commit `3b22ed9ff3b5a854edabf792fd0c1e0d65b2c15b`, not the tree this record was archived from.
- There is no `verification-attempts.json`: SpecSync 5 did not write one for this record, and this migration does not invent attempt history.
- This migration added no verification evidence, test result, attempt history, or approval. It is a manual migration, not a fresh re-verification.
- Closing it through the tool takes `specsync change reopen`, `specsync change verify`, then `specsync change accept`, which writes a new closing approval. Per Leif's decision it was archived by hand instead, so no reopen or new approval is recorded.
