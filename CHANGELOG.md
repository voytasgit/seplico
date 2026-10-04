# Changelog

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
