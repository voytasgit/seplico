# Seplico name and namespace

**Project name:** Seplico Standard
**Specification name:** Seplico Specification
**Repository namespace:** `seplico`
**Application file extension:** `.seplico`

## Naming rule

Seplico is the public name of this specification. Normative terminology should use **Seplico Application** and **Seplico Interaction**.

The specification describes identity-separated job applications. It does not claim that a Seplico file or the surrounding process is fully anonymous or unlinkable.

## File extension

A Seplico Application uses the proposed `.seplico` extension in the reference examples.

The extension is a convention of this specification; conformance MUST be determined from content and schema validation, not from the filename alone.

## Media type

The proposed future media type is:

```text
application/seplico+json
```

This value is **not represented as IANA-registered** in this draft. Until a registration exists, implementations should not claim that it is an officially registered media type.

## Namespace stability

Public releases should keep the `Seplico` name, `seplico` repository namespace, `.seplico` extension and `seplico_*` data namespace consistent unless a later specification version deliberately defines a migration.
