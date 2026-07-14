---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance
artifact: context
---

# Context

The repository publishes educational Python helpers for Algorand accounts, ALGO payments, atomic payment groups, and asset operations, plus a LocalNet demonstration. Its existing Python 3.14, Poetry, AlgoKit LocalNet tests, import checks, and CI workflow are the native verification boundary. Because those helpers are a real public contract, the migration requires stable requirements and full SDD coverage rather than a zero-coverage exception.
