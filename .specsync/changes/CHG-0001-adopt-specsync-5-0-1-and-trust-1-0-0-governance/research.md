---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance
artifact: research
---

# Research

Repository inspection identified thirteen public Python helpers across account, payment, atomic-group, asset, and demonstration modules. Existing tests exercise funded account creation, balance retrieval, payments, asset creation, opt-in, transfer, balance, and opt-out against AlgoKit LocalNet. Import checks cover every module and the `main` entry point. The existing CI also preserves Python 3.14, Poetry, Docker/LocalNet setup, tests, import checks, CodeQL, and optional lint boundaries. No source or existing test change is needed to document this behavior accurately.
