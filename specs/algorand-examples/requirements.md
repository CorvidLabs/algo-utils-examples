---
spec: algorand-examples.spec.md
---

# Requirements

### REQ-algorand-examples-001

The examples SHALL load named accounts through the configured AlgoKit client, request the caller's initial LocalNet funding amount, and expose account balances in ALGO.

Acceptance Criteria
- LocalNet tests create a funded named account, confirm a non-empty address and private key, and confirm the requested minimum balance.

### REQ-algorand-examples-002

The examples SHALL generate signing accounts and convert between private keys, mnemonic phrases, and recovered signing accounts through the documented AlgoKit and SDK APIs.

Acceptance Criteria
- Import verification confirms the account helpers remain available with their documented inputs and return types.

### REQ-algorand-examples-003

The examples SHALL accept a signing account or address for each payment endpoint, convert ALGO to integer microAlgos, and return the send result.

Acceptance Criteria
- LocalNet tests send a funded payment by address and confirm the receiver's resulting balance.

### REQ-algorand-examples-004

The examples SHALL add an ordered list of payment parameters to one atomic transaction group and send that group once.

Acceptance Criteria
- Import and module validation confirm the atomic-group helper and its ordered payment-parameter contract remain available.

### REQ-algorand-examples-005

The examples SHALL create an Algorand Standard Asset with the supplied metadata and supply, default omitted control addresses to the sender, and return the resulting asset ID.

Acceptance Criteria
- LocalNet tests create an asset and confirm its ID is a positive integer.

### REQ-algorand-examples-006

The examples SHALL support asset opt-in, base-unit transfer, zero-balance opt-out to the creator, and holding lookup for signing accounts or addresses.

Acceptance Criteria
- LocalNet tests opt in a funded account, transfer base units, confirm sender and receiver holdings, opt out, and confirm the holding is removed.

### REQ-algorand-examples-007

The examples SHALL return zero when an account has no holding for the requested asset ID.

Acceptance Criteria
- The holding lookup completes without fabricating a transaction or raising a missing-holding success-path error.

### REQ-algorand-examples-008

The package SHALL expose a LocalNet demonstration that composes account creation, balances, payments, asset lifecycle operations, and an atomic payment group.

Acceptance Criteria
- Import verification loads `main` without executing the interactive demonstration, while LocalNet tests cover its underlying helper boundaries.

### REQ-algorand-examples-009

The repository SHALL verify the examples with Python 3.14, Poetry, AlgoKit LocalNet tests, and package import checks.

Acceptance Criteria
- The Fledge `verify` lane completes the LocalNet test suite and imports every public module and the `main` entry point.

### REQ-algorand-examples-010

The repository SHALL run the unified Trust gate for pull requests and main-branch pushes using the immutable Trust 1.0.0 release commit.

Acceptance Criteria
- The hosted workflow preserves Python 3.14, Poetry, Docker preparation, full history, and the exact immutable Trust action pin.

