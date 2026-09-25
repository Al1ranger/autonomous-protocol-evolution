# Security

Experimental and unaudited. Do not use as the sole control for production protocol upgrades.

- A specification URL is caller-selected but must be HTTPS; network-level SSRF protection is delegated to GenVM's web sandbox. Deployment operators should add an allowlist if their environment permits private network access.
- Expected hashes are exact lowercase SHA-256 commitments. The full response is hashed before its text is used; bodies over 12,000 bytes fail closed.
- The initial baseline is fetched and checked before activation. Every upgrade refetches both baseline and candidate; changing either source causes a hash mismatch.
- Both leader and validators must independently reproduce the entire status/hash/compatibility vector. No confidence tolerance crosses a promotion threshold.
- An invited maintainer must accept before proposing. A proposal binds its protocol and exact active parent version; a stale or cross-protocol proposal cannot promote.
- Semantic compatibility is bounded to the published text and rubric. It is not an executable conformance test, formal proof, or assurance that a protocol works in production.

Report security problems privately through the repository's security advisory flow.
