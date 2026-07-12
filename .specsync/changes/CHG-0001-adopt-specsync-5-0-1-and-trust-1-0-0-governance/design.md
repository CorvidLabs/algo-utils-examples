---
change: CHG-0001-adopt-specsync-5-0-1-and-trust-1-0-0-governance
artifact: design
---

# Design

Keep existing workflows and data intact. Add a separate trust job pinned to the immutable Trust v1.0.0 commit. Trust invokes a Fledge lane for Python 3.14, Poetry, AlgoKit LocalNet tests, imports, and module validation, uses advisory coverage zero, blocking risk, progressive provenance, and disables Trust-managed Atlas.
