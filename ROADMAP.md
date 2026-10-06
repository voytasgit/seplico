# Roadmap

## v0.2 - lean core (published)

Goal: make the Seplico concept small enough to understand, implement and review independently.

- Seplico Application schema
- fresh per-application identifier
- no global applicant identifier
- minimal skills / experience / qualifications / evidence references
- Identity Request
- selective Identity Response
- local generator and viewer
- explicit separation between schema validation, privacy linting and cryptographic verification

## v0.3 - requirement-to-evidence interoperability (current draft)

Goal: add the smallest missing interoperability layer without turning Seplico into a job standard or matching engine.

- application-scoped Claim IDs for skills, experience and qualifications;
- optional Evidence Mapping document;
- external requirement references rather than a Seplico job-description schema;
- flow-level tests that claim/evidence references resolve against one Application;
- explicit rule that mapping is not scoring, ranking, verification or a hiring decision;
- test the model against realistic job/application pairs and re-identification cases.

## Later research - not v0.3 requirements

- profiles for specific external job/requirement standards;
- message authenticity and continuity binding;
- verifiable credentials;
- selective-disclosure mechanisms;
- OpenID-based presentation flows;
- pairwise or relay-based transports;
- formal media-type registration;
- ATS adapters;
- mappings to external skill/career standards;
- optional evaluation outputs only if a demonstrated interoperability need cannot be solved outside the core.

No future technology should be promoted into the Seplico core merely because it exists. It should solve a demonstrated interoperability or privacy need.
