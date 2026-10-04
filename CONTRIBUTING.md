# Contributing

Seplico is currently a small specification maintained around a deliberately narrow core.

Contributions should preserve these invariants:

1. An Application ID identifies one application, not a person.
2. No global applicant ID in the core application format.
3. No applicant-controlled `verified`, `anonymous` or `unlinkable` trust flags.
4. Evidence references are not verification results.
5. Transport, wallets, credential infrastructure and custom cryptography are not automatically core features.
6. New fields must be justified against data minimization and re-identification risk.

Changes to normative behavior should include:

- an update to `SPECIFICATION.md`;
- matching schema changes;
- examples/tests;
- an entry in `CHANGELOG.md`.

Contributions do not alter the historical authorship statement in `AUTHORS.md`; contributors can be acknowledged separately as the project evolves.
