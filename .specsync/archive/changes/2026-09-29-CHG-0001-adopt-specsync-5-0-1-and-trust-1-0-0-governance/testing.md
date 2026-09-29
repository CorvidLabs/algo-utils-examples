---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance
artifact: testing
---

# Testing

Run `specsync check --strict --require-coverage 100 --force`, `specsync agents status`, `fledge trust doctor`, `fledge lanes run verify`, and `fledge trust verify`. The LocalNet lane must execute the existing tests and package imports; an unavailable LocalNet is not accepted as successful blockchain evidence.

Requirement evidence is provided by the preserved tests, import check, and immutable workflow:

- `REQ-algorand-examples-001` — named funded account creation and ALGO balance.
- `REQ-algorand-examples-002` — account generation and mnemonic conversion API availability.
- `REQ-algorand-examples-003` — ALGO payment address handling and microAlgo conversion.
- `REQ-algorand-examples-004` — ordered atomic payment-group composition.
- `REQ-algorand-examples-005` — asset creation, metadata, control-address defaults, and positive ID.
- `REQ-algorand-examples-006` — asset opt-in, transfer, holding balance, and zero-balance opt-out.
- `REQ-algorand-examples-007` — zero result for a missing asset holding.
- `REQ-algorand-examples-008` — importable LocalNet demonstration composition.
- `REQ-algorand-examples-009` — Python 3.14, Poetry, LocalNet tests, and import verification.
- `REQ-algorand-examples-010` — pull-request and main-branch Trust gate at the immutable release commit.
