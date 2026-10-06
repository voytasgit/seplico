# Contributing

Seplico is currently a small specification maintained around a deliberately narrow core.

Contributions should preserve these invariants:

1. An Application ID identifies one application, not a person.
2. No global applicant ID in the core application format.
3. Claim IDs are application-scoped references and MUST NOT become durable person identifiers.
4. No applicant-controlled `verified`, `anonymous` or `unlinkable` trust flags.
5. Evidence references are not verification results.
6. Requirement mappings connect external requirements to claims/evidence; they are not fit scores, rankings or hiring decisions.
7. Seplico does not become a job-description standard, skill taxonomy or ATS.
8. Transport, wallets, credential infrastructure and custom cryptography are not automatically core features.
9. New fields must be justified against data minimization, interoperability need and re-identification risk.

Changes to normative behavior should include:

- an update to `SPECIFICATION.md`;
- matching schema changes;
- examples/tests;
- an entry in `CHANGELOG.md`.

Contributions do not alter the historical authorship statement in `AUTHORS.md`; contributors can be acknowledged separately as the project evolves.
