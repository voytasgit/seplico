# Seplico v0.3 - explicit non-goals

The core is intentionally small. The following items are **not** required to publish or demonstrate the Seplico Standard:

- no Seplico-owned job-description or job-requirement standard;
- no proprietary skill taxonomy;
- no global applicant ID;
- no permanent applicant profile;
- no central applicant database;
- no job board;
- no ATS replacement;
- no ranking or matching engine;
- no universal fit score or hiring decision;
- no credential issuing infrastructure;
- no applicant-controlled `verified` flag;
- no custom cryptography;
- no wallet requirement;
- no blockchain;
- no BBS / zero-knowledge requirement;
- no mandatory identity provider;
- no mandatory relay service;
- no guarantee of anonymity or unlinkability;
- no attempt to standardize all professional or job data.

## Scope filter

For v0.3, a proposed core feature should be necessary to demonstrate one of these two linked flows:

```text
external requirement reference
      ->
application-local claim
      ->
optional evidence reference
```

and

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

If a feature is not needed for these flows, it belongs in an implementation, future research or a later profile rather than the v0.3 core.
