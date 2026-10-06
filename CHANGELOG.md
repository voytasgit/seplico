# Changelog

## 0.3.0-draft - unreleased

### Interoperability

- Added optional application-scoped `claim_id` fields to skills, experience items and qualifications.
- Added `schema/evidence-mapping.schema.json` for explicit Requirement -> Claim -> optional Evidence edges using externally defined requirement references.
- Kept job/requirement semantics external to Seplico; v0.3 does not define a Seplico Job Contract.
- Explicitly excludes assessment, score and ranking fields from the Evidence Mapping schema.
- Added cross-document tests for Application ID, Claim ID and Evidence ID resolution.

### Compatibility and scope

- Bumped the working message-model version to `0.3`.
- Identity Request / Response semantics remain unchanged from v0.2.
- The v0.2 release remains the first published/archived release; v0.3 is not represented as published until an actual release occurs.

## 0.2.0-draft - pre-publication

Lean redesign of the original prototype.

### Core changes

- Reduced Seplico to two normative message families: Application and Interaction.
- Kept the rule `Application ID != Person ID` as the central invariant.
- Made Identity Request / selective Identity Response part of the core concept.
- Made transport explicitly out of scope.
- Removed applicant-controlled claims such as `verified`, `anonymous`, `identity: hidden` and `linkability: disabled`.
- Removed a universal Seplico 1-5 skill-level scale.
- Kept external skill identifiers and proficiency schemes optional.
- Replaced exact experience-month modeling with coarse duration bands in the core example model.
- Explicitly separated schema validity, privacy linting and cryptographic verification.
- Moved cryptography, wallets, verifiable credentials, selective disclosure and ATS integration to non-normative future research.

### Publication preparation

- Added AUTHORS.md, NOTICE and CITATION.cff.
- Added a publication checklist designed to preserve an honest first-public-release record.

### Naming

- Replaced the former pre-publication working name with **Seplico**.
- Renamed the specification to **Seplico Specification** and the project to **Seplico Standard**.
- Changed the application namespace to `seplico_version` / `seplico_...` and the application extension to `.seplico`.
- Recorded `application/seplico+json` as a proposed future media type only; it is not represented as IANA-registered.
