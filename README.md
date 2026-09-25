# AutonomousProtocolEvolution

A GenLayer primitive for **compatibility-preserving evolution of agent interaction protocols**. This is not a truth oracle, reputation system, or certificate gate. Its state transition is promotion of a new normative protocol version.

## Problem

Agent ecosystems publish human-readable message and state-machine obligations. A syntactically valid replacement can still change a required field's meaning, invalidate an old interaction trace, or remove a timeout guarantee. A hash or deterministic schema diff alone cannot decide that semantic compatibility.

## Consensus boundary

The owner registers an initial HTTPS specification with its exact SHA-256. GenLayer validators independently fetch and hash it before activation. An invited, accepting maintainer may propose a successor, bound to the active version, HTTPS URL, and expected hash.

During resolution, **leader and validators each fetch the complete old and candidate specifications**. Both independently assess four decision-bearing dimensions: old message meanings, old valid transitions, error/timeout obligations, and candidate coherence. Each dimension is exactly PASS, FAIL, or UNKNOWN. Consensus requires exact equality of both HTTP statuses, both full-response hashes, both hash-match flags, completeness flags, and the entire four-value vector. A FAIL yields INCOMPATIBLE; any missing, changed, truncated, or uncertain evidence yields INCONCLUSIVE. Only four PASS results activate the successor. Validator disagreement cannot promote a version.

```text
DRAFT --fetch/hash baseline--> ACTIVE(v0)
ACTIVE(vN) --member proposal at parent N--> PROPOSED
PROPOSED --independent fetch + semantic consensus--> ACTIVATED(vN+1)
                                           |--> INCOMPATIBLE / INCONCLUSIVE
                                           |--> STALE if active parent changed
```

Version records and decisions are append-only. A competing proposal tied to a displaced parent becomes STALE; it cannot overwrite the new active version. This initial release intentionally does **not** claim branching, merge adapters, executable conformance, or real-world protocol quality. Its consensus claim is limited to the two pinned published documents and the stated compatibility rubric.

## Contract API

`register_protocol`, `activate_protocol`, `invite_member`, `accept_membership`, `propose_upgrade`, `resolve_upgrade`, `get_protocol`, `get_version`, `get_proposal`, `get_report`.

## Build and test

```powershell
python -m pip install genvm-linter genlayer-test pytest
genvm-lint check contracts/AutonomousProtocolEvolution.py
pytest tests/direct -q
```

Direct tests exercise access control, bindings, and state transitions; they do not reproduce multi-validator consensus. StudioNet receipts and source comparison are required for that evidence.

## Deploy

```powershell
genlayer network set studionet
genlayer deploy --contract contracts/AutonomousProtocolEvolution.py
genlayer code <address>
genlayer schema <address>
```

Use immutable, content-addressed HTTPS URLs. The examples under `examples/specs` are deliberately simple: v2 is additive, while v3 removes required identity and timeout semantics. Compute SHA-256 of the exact bytes served by the pinned URL before registration or proposal. See `LIVE_PROOFS.md` for verified transactions, if present.

## Security limits

Public specifications may contain adversarial instructions, so the prompt treats both documents only as data. The contract limits fetched body size, verifies full-response hashes, and never trusts caller-supplied summaries or scores. A domain or author can still publish a bad protocol; the contract does not prove safety or operational success. See `SECURITY.md`.
