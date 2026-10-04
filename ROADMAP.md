# Roadmap

## v0.2 - lean core (current)

Goal: make the Seplico concept small enough to understand, implement and review independently.

- Seplico Application schema
- fresh per-application identifier
- no global applicant identifier
- minimal skills / experience / qualifications / evidence references
- Identity Request
- selective Identity Response
- local generator and viewer
- explicit separation between schema validation, privacy linting and cryptographic verification

## v0.3 - implementation feedback

Only after the v0.2 flow has been tested with real examples:

- improve validation rules;
- define a small interoperability profile if needed;
- test integration into one realistic recruiting workflow;
- refine privacy guidance based on concrete re-identification cases.

## Later research - not v0.2 requirements

- message authenticity and continuity binding;
- verifiable credentials;
- selective-disclosure mechanisms;
- OpenID-based presentation flows;
- pairwise or relay-based transports;
- formal media-type registration;
- ATS adapters;
- mappings to external skill/career standards.

No future technology should be promoted into the Seplico core merely because it exists. It should solve a demonstrated interoperability or privacy need.
