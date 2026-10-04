# Seplico Specification v0.2.0-draft

**Status:** Initial Public Draft
**Original concept and specification:** Vadym Voytas
**First public release:** 2026-10-04

## 1. Purpose

Seplico defines a minimal interchange format for a **single job application** whose professional content is initially separated from direct identity data. It also defines a minimal interaction format for requesting and selectively releasing identity later in that application process.

The key rule is:

> **An application identifies an application - not the person behind it.**

Seplico does not define a permanent applicant profile.

## 2. Terminology

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express normative requirements in this draft.

- **Application**: one job-specific Seplico record.
- **Application ID**: a fresh identifier for exactly one application.
- **Applicant**: the person behind an application.
- **Identity data**: data that directly identifies or contacts the applicant, such as name, e-mail address or telephone number.
- **Identity Request**: a message asking the applicant to release selected identity attributes for one application.
- **Identity Response**: the applicant's explicit release of selected identity attributes for that request.
- **Evidence reference**: a statement that supporting material exists. It is not proof of verification.

## 3. Three-layer model

Seplico deliberately separates three layers.

### 3.1 Existing professional data

Skills, qualifications, experience and credentials may already exist in other systems or formats. Seplico does not attempt to replace those systems.

### 3.2 Seplico Application Projection

For one concrete job application, relevant professional data is projected into a new Seplico Application. The application has a fresh Application ID and no global applicant ID.

### 3.3 Seplico Interaction

If the employer wants to continue, it can create an Identity Request referring to that Application ID. The applicant can then explicitly release selected identity attributes in an Identity Response.

The transport of these messages is outside the v0.2 core specification.

## 4. Seplico Application

A Seplico Application MUST validate against `schema/application.schema.json`.

A conforming application:

- MUST use `seplico_version: "0.2"`;
- MUST use `type: "application"`;
- MUST contain a fresh `application_id`;
- MUST describe one target vacancy or application context;
- MUST NOT contain a global applicant/person identifier;
- MUST NOT contain direct identity fields such as name, e-mail, phone number, full address, birth date or photo;
- MUST NOT claim that the application is anonymous, unlinkable or verified;
- SHOULD contain only data relevant to the target application.

### 4.1 Application ID

The Application ID is a process identifier, not a person identifier.

It MUST:

- be generated independently for each application;
- be generated from at least 128 bits of cryptographically secure random input;
- not be derived from name, e-mail address, telephone number or another applicant identifier;
- not be reused for another application.

The reference representation is:

```text
seplico_<base64url-random-value>
```

A 16-byte random value encoded as unpadded Base64URL satisfies the minimum random-input requirement.

### 4.2 Target

`target.reference` identifies the job, vacancy or receiving process. Seplico does not prescribe the employer's job-description format.

`target.role_label` is optional human-readable context.

### 4.3 Skills

A skill MUST contain a human-readable `label`.

Optional identifiers can reference an external vocabulary:

```json
{
  "label": "Python",
  "identifier": {
    "scheme": "external-scheme",
    "value": "external-id"
  }
}
```

Seplico does not define its own universal skill taxonomy.

An optional proficiency value MUST identify its scheme. Seplico does not define a universal 1-5 proficiency scale.

### 4.4 Experience

Experience is intentionally coarse in this draft. `duration_band` uses broad bands rather than exact month counts to reduce unnecessary precision.

### 4.5 Qualifications

Qualifications can include a title and optional level or issuer label. Implementers SHOULD consider whether specific issuers or rare qualifications increase re-identification risk.

### 4.6 Evidence

Evidence is separate from assertion.

A Seplico file MAY state that supporting material exists, for example:

- `self_asserted`
- `portfolio_reference`
- `credential_reference`
- `assessment_reference`
- `employer_reference`

The existence of an evidence reference MUST NOT be presented as successful verification.

In particular, the application schema has no applicant-controlled `verified: true` flag.

Actual credential verification is outside the v0.2 core.

## 5. Seplico Interaction

Interaction messages MUST validate against `schema/interaction.schema.json`.

### 5.1 Identity Request

An Identity Request identifies:

- the `application_id`;
- a fresh `request_id`;
- the identity attributes requested by the employer.

The `request_id` is a process identifier for one identity request. It MUST be newly generated for each request and MUST NOT be reused for another request. The reference implementation uses 128 bits of cryptographically secure random input, encoded in the same style as the Application ID.

The v0.2 core permits requests for:

- `name`
- `email`
- `phone`

The request does not itself reveal applicant identity.

### 5.2 Identity Response

An Identity Response refers to both the Application ID and Request ID and contains only the attributes the applicant chooses to release.

For the referenced Identity Request:

- the response MUST use the same `application_id`;
- the response MUST use the same `request_id`;
- every released attribute MUST have been included in `requested_attributes`;
- the applicant MAY release fewer attributes than were requested.

The response MUST contain `consent: true`. This field expresses the applicant's decision in the message model. By itself it is not cryptographic proof of authorship, identity, informed consent, or continuity with the person who originally created the application.

The JSON Schema validates each interaction message independently. Cross-message rules, such as matching IDs and ensuring that released attributes are a subset of requested attributes, require flow-level validation by the implementation.

## 6. Transport is out of scope

Seplico v0.2 defines message meaning and structure, not message transport.

Possible future transports include ATS messages, job-board workflows, temporary web links, APIs, relays or wallets. None is required by the v0.2 core.

A transport can reveal identity even when the Seplico Application itself does not. Therefore implementations MUST NOT equate an identity-separated file with an anonymous end-to-end process.

Likewise, v0.2 does not define who is authorized to issue an Identity Request, how a request is delivered, or how message authenticity is established. Those are transport/security concerns for later profiles or implementations.

## 7. Privacy requirements

### 7.1 Direct identity fields

A Seplico Application MUST NOT contain standard fields for:

- first or last name;
- e-mail address;
- telephone number;
- full postal address;
- date of birth;
- photograph;
- global applicant ID;
- social-network account ID.

### 7.2 Free text and indirect identification

Schemas cannot prove that arbitrary strings are non-identifying. A skill label, qualification, evidence reference, rare career path or external URL can still identify a person.

Implementations SHOULD minimize free text, unnecessary precision and person-specific external references.

### 7.3 File privacy versus process privacy

Conformance of a Seplico Application does not mean the overall submission is anonymous. Transport metadata, account data, logs and external references are outside the file and can identify or correlate the applicant.

## 8. Validation and trust

Three different concepts MUST remain separate:

1. **Schema validity** - the JSON structure conforms to a Seplico schema.
2. **Privacy linting** - heuristics find no obvious direct identity markers.
3. **Cryptographic verification** - authenticity or credential proofs were actually checked.

A conforming implementation MUST NOT present (1) or (2) as (3).

The reference viewer performs basic structural checks and privacy linting only. It explicitly does not perform cryptographic verification.

## 9. File representation

A Seplico Application is UTF-8 JSON. Reference examples use the `.seplico` file extension. Implementations MUST NOT infer conformance from a filename extension alone.

The proposed future media type is:

```text
application/seplico+json
```

This draft does **not** represent that media type as IANA-registered. A future registration, if pursued, is a separate publication step.

Object property ordering is not significant.

## 10. Extensions

The v0.2 schemas use strict known properties to keep the privacy surface small. New normative fields require a new compatible schema/specification revision rather than arbitrary vendor-specific identity fields.

Experimental data SHOULD be kept outside the core Seplico document until an extension mechanism is deliberately specified.

## 11. Explicit non-goals

Seplico v0.2 does not define:

- a job board;
- an ATS;
- a professional social network;
- a global applicant profile;
- a skill database or taxonomy;
- a matching or ranking algorithm;
- a credential issuing or verification infrastructure;
- a wallet;
- a blockchain;
- a custom cryptographic system;
- zero-knowledge proofs;
- a permanent identity provider;
- a mandatory relay service;
- a claim of complete anonymity or unlinkability.

See `NON_GOALS.md`.

## 12. Future compatibility

Future versions MAY define profiles or mappings for existing standards such as external skill vocabularies, career-record formats or verifiable credentials. Such integrations should reuse external standards rather than duplicate them inside Seplico.

These integrations are not required for v0.2 conformance.

## 13. Versioning

`seplico_version` identifies the Seplico message-model version, not the implementation version.

This document is a draft and may change before the first stable release.

## 14. Authorship and publication record

**Original concept and specification: Vadym Voytas.**

The initial Seplico specification was created in 2026.

The first public release date MUST be recorded only at actual public publication. Git tags, release metadata and archival records SHOULD preserve that publication history rather than rewriting it retroactively.

This statement records authorship of this specification. It is not a claim that no related concepts existed before Seplico.
