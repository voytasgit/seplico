# Seplico Standard

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23136732.svg)](https://doi.org/10.5281/zenodo.23136732)

**Open specification for identity-separated job applications**<br>
**Specification:** Seplico Specification<br>
**Canonical repository:** https://github.com/voytasgit/seplico<br>
**Published v0.2 DOI:** https://doi.org/10.5281/zenodo.23136732<br>
**Development status:** v0.3.0-draft - unreleased interoperability draft

> **Core principle:** An application identifies an application - not the person behind it.

Seplico defines a small, open interchange model for one concrete job application. Professional information can be submitted without making a durable applicant identity part of the application record. External job requirements can optionally be linked to application-local claims and evidence without turning Seplico into a job-description standard or matching engine. If an employer wants to continue, selected identity information can be requested and released in a separate interaction.

## Authorship

**Original concept and specification: Vadym Voytas.**

The initial Seplico Specification was authored by Vadym Voytas in 2026. This repository is the canonical public repository of the Seplico Specification. The initial public release, v0.2.0-draft, was published on October 4, 2026 and archived on Zenodo under DOI 10.5281/zenodo.23136732. See [AUTHORS.md](AUTHORS.md) and [PUBLISHING.md](PUBLISHING.md).

This authorship statement documents the origin of the Seplico Specification. It does **not** claim that no similar idea, research, product, or standard existed previously.

## What Seplico is

Seplico v0.3 defines three small things:

1. **Seplico Application** - a job-specific projection of relevant skills, experience, qualifications and evidence references, with a fresh application ID and without a global applicant ID. Application-local claim IDs may be added when another Seplico document needs to refer to a specific skill, experience item or qualification.
2. **Seplico Evidence Mapping** - an optional mapping from externally defined job/opportunity requirements to application-local claims and optional evidence references. It does not define requirement semantics, fit scores, rankings or hiring decisions.
3. **Seplico Interaction** - an identity request for one application and a selective identity response by the applicant.

The transport channel is intentionally out of scope. Seplico does not require a central server, wallet, job board, identity provider, blockchain or proprietary platform.

## What Seplico is not

Seplico is not a job-description standard, skill taxonomy, professional identity system, credential infrastructure, ATS, job board, matching engine, ranking model, wallet or cryptographic protocol. Existing standards can supply job requirements and professional vocabularies; Seplico only defines how a concrete application can refer to them.

See [NON_GOALS.md](NON_GOALS.md). Naming and namespace conventions are documented in [NAME_AND_NAMESPACE.md](NAME_AND_NAMESPACE.md).

## Repository layout

```text
seplico/
├── README.md
├── SPECIFICATION.md
├── AUTHORS.md
├── CITATION.cff
├── NOTICE
├── LICENSE
├── CHANGELOG.md
├── HISTORY.md
├── NON_GOALS.md
├── NAME_AND_NAMESPACE.md
├── ROADMAP.md
├── PUBLISHING.md
├── VERSION
├── SETUP_WINDOWS.md
├── schema/
│   ├── application.schema.json
│   ├── evidence-mapping.schema.json
│   └── interaction.schema.json
├── examples/
│   ├── software-developer.seplico
│   ├── evidence-mapping.json
│   ├── identity-request.json
│   └── identity-response.json
├── reference/
│   ├── generator/index.html
│   └── viewer/index.html
├── research/
│   └── README.md
├── .github/workflows/
│   └── validate.yml
└── tests/
    └── test_schemas.py
```

## Quick start

Open `reference/generator/index.html` locally in a modern browser to generate sample Seplico messages. Open `reference/viewer/index.html` to inspect a Seplico file or interaction/mapping message.

For schema and cross-document flow tests:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

## Important privacy limitation

A `.seplico` file can omit direct identity data, while the **surrounding submission process can still reveal identity**. Sending the file from a named e-mail account, using an identified job-board account, attaching identifying portfolio links, or including rare combinations of facts can identify the applicant.

Therefore:

> **File privacy is not the same as process privacy.**

Seplico does not claim technical anonymity or unlinkability. Evidence mappings likewise do not make evidence verified or a candidate suitable.

## File extension and future media type

Seplico Application examples use the `.seplico` extension.

The proposed future media type is `application/seplico+json`. It is **not represented as IANA-registered** in this draft.

## License

Unless otherwise stated, this repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE).

## Publication and development

See [SETUP_WINDOWS.md](SETUP_WINDOWS.md) for the local development workflow and [PUBLISHING.md](PUBLISHING.md) for the publication and release process.
