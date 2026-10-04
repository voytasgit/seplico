# Seplico v0.2 - explicit non-goals

The v0.2 core is intentionally small. The following items are **not** required to publish or demonstrate the Seplico Standard:

- no proprietary skill taxonomy;
- no global applicant ID;
- no permanent applicant profile;
- no central applicant database;
- no job board;
- no ATS replacement;
- no ranking or matching engine;
- no credential issuing infrastructure;
- no applicant-controlled `verified` flag;
- no custom cryptography;
- no wallet requirement;
- no blockchain;
- no BBS / zero-knowledge requirement;
- no mandatory identity provider;
- no mandatory relay service;
- no guarantee of anonymity or unlinkability;
- no attempt to standardize all professional data.

## Scope filter

For v0.2, a proposed feature belongs in the core only if it is necessary to demonstrate this flow:

```text
professional data
      ->
job-specific Seplico Application
      ->
employer selects Application X
      ->
Identity Request(X)
      ->
applicant consent
      ->
Identity Response(X)
```

If a feature is not needed for this flow, it belongs in future research or a later profile, not in the v0.2 core.
