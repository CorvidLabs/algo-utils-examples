---
spec: algorand-examples.spec.md
---

## Test Plan

Run the repository's existing Python 3.14 test suite against AlgoKit LocalNet, then import every package module and the demonstration entry point. Account tests cover environment-backed creation and balance retrieval; transaction tests cover funded payment behavior; asset tests cover creation, opt-in, transfer, balance, and opt-out behavior.

Run strict SpecSync validation at 100%, all four agent status checks, Trust doctor, and the full Trust gate. Hosted verification repeats the Poetry and LocalNet boundary on Ubuntu. No test may turn an unavailable LocalNet into proof that blockchain behavior passed.
