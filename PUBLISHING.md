# Publication checklist

This repository is intentionally prepared **before** public release so the first public version can be deliberate and internally consistent.

## Before making the repository public

- [ ] Confirm that `Seplico`, `.seplico` and the repository namespace are used consistently; see `NAME_AND_NAMESPACE.md`.
- [ ] Check the chosen final name for obvious naming/trademark conflicts before public launch.
- [ ] Decide whether any patent filing should be considered **before** public disclosure; obtain qualified legal advice if this matters.
- [ ] Review `SPECIFICATION.md`, schemas and examples together.
- [ ] Run all tests.
- [ ] Confirm that examples contain no real personal data.
- [ ] Confirm `AUTHORS.md` and `NOTICE` state the origin accurately.
- [ ] Confirm the chosen license.
- [ ] Set the canonical GitHub repository URL in README/CITATION metadata after the repository exists.
- [ ] Do not invent or backdate a first-publication date.

## First public release

Suggested sequence:

1. Create the canonical GitHub repository as **private** and push the reviewed local history.
2. Set the final repository URL and prepare the actual publication-date metadata while it is still private.
3. Run all tests again and make one reviewed release-candidate commit.
4. Enable GitHub immutable releases **before** publishing the first release.
5. Make the repository public.
6. Create/publish a GitHub Release from the exact reviewed commit, using a tag such as `v0.2.0-draft`.
7. Archive that release with Zenodo and record the assigned DOI in the next metadata update/release.
8. Point the project domain, if any, to the canonical specification and repository.

For a simple provenance story, make the repository public and publish the first release on the same calendar day. Do not backdate commits or release metadata.

## Priority wording

Prefer verifiable wording such as:

> Original concept and specification: Vadym Voytas. First public Seplico release published on YYYY-MM-DD.

Avoid unprovable wording such as:

> The first person in the world to invent anonymous recruiting.

The goal is a strong, accurate publication record, not an exaggerated claim.
