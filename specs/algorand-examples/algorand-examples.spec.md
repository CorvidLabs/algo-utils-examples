---
module: algorand-examples
version: 1
status: stable
files:
  - src/algo_utils_examples/__init__.py
  - src/algo_utils_examples/accounts.py
  - src/algo_utils_examples/transaction.py
  - src/algo_utils_examples/assets.py
  - src/algo_utils_examples/main.py
  - .github/workflows/trust.yml
db_tables: []
depends_on: []
---

# Algorand Utils Examples Specification

## Purpose

Provide educational Python examples for account management, ALGO payments, atomic payment groups, and Algorand Standard Asset operations through AlgoKit Utils, together with a runnable LocalNet demonstration.

## Public API

| Export | Description |
|--------|-------------|
| `create_account` | Load an environment-backed account through the configured client and request LocalNet funding when applicable. |
| `get_balance` | Return an account's ALGO balance as a decimal value. |
| `create_testnet_account` | Return a newly generated signing account from the configured client. |
| `get_mnemonic_from_private_key` | Convert a base64 private key into its mnemonic phrase. |
| `get_account_from_mnemonic` | Recover a signing account from a mnemonic phrase. |
| `payment` | Send an ALGO payment after converting the supplied ALGO amount to integer microAlgos. |
| `group_transaction` | Build and send one atomic group from an ordered list of payment parameters. |
| `create_asset` | Create an Algorand Standard Asset and return its asset ID. |
| `opt_in` | Send an asset opt-in transaction for an account or address. |
| `opt_out` | Send an asset opt-out transaction to the creator for an account or address. |
| `assets_transfer` | Send an asset transfer in base units between accounts or addresses. |
| `get_asset_balance` | Return an account's holding for an asset, or zero when no holding exists. |
| `logger` | Module-scoped logger used by the educational demonstration. |
| `main` | Run the complete LocalNet account, payment, asset, and atomic-group demonstration. |
| `name` | Names the hosted workflow `trust`. |
| `on` | Runs the Trust workflow for pull requests and main-branch pushes. |
| `permissions` | Defines the workflow's least-privilege permission map. |
| `permissions.contents` | Grants read-only repository content access. |
| `jobs` | Contains the workflow job map. |
| `jobs.trust` | Runs Python 3.14, Poetry, Docker/LocalNet preparation, and immutable Trust verification. |

## Invariants

1. APIs accepting `SigningAccount | str` derive the address from a signing account and otherwise use the supplied address unchanged.
2. `payment` converts ALGO to microAlgos by multiplying by 1,000,000 and converting to an integer before sending.
3. `group_transaction` preserves payment parameter order and sends the assembled group once.
4. Asset transfer amounts and balances use integer base units; decimal display interpretation belongs to asset metadata and callers.
5. Asset creation defaults unset manager, reserve, freeze, and clawback addresses to the sender address.
6. A missing asset holding is reported as zero.
7. The demonstration targets an AlgoKit LocalNet client and may expose newly generated LocalNet mnemonics only as an explicit educational warning, never as production secret handling guidance.
8. The hosted Trust gate uses the immutable Trust 1.0.0 commit and preserves the repository's Python 3.14, Poetry, Docker, and LocalNet verification boundary.

## Behavioral Examples

- Creating a LocalNet account with `initial_algo=1000` delegates to `from_environment` with an `AlgoAmount` of 1,000 ALGO.
- Paying `2.5` ALGO constructs a payment amount of 2,500,000 microAlgos.
- Adding multiple `PaymentParams` to `group_transaction` produces one atomic send in the same order.
- Creating an asset without explicit control addresses assigns all four control roles to the creator address.
- Looking up an asset ID absent from an account's holdings returns `0`.

## Error Cases

- AlgoKit client, LocalNet, network, signing, and transaction errors propagate to the caller; the helpers do not convert a failed blockchain operation into success.
- Asset opt-out can fail when the holding is non-zero or the creator is incorrect, according to Algorand protocol rules.
- Payment amounts that cannot be converted to an integer microAlgo value fail before or during transaction construction.
- `main` requires a running LocalNet and valid configured accounts; it is an interactive educational demonstration rather than an offline command.

## Dependencies

- Python 3.14.
- `algokit-utils` 4.x and `py-algorand-sdk` 2.x.
- `python-dotenv` for optional environment-backed mnemonic configuration.
- AlgoKit and Docker for LocalNet execution.
- Poetry for dependency installation and test execution.

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 0 | 2026-07-13 | Baseline contract prepared for SpecSync 5.0.1 and Trust 1.0.0 adoption. |
| 2026-07-14 | CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance: Adopt SpecSync 5.0.1 and Trust 1.0.0 governance |
