# TaskRelay v3 — intentionally incompatible candidate

REQUEST contains required payload but does not contain request_id. ACK no longer
carries request_id. ERROR has only a numeric code. The receiver does not preserve
or echo any request identifier.

The initial state is IDLE. REQUEST in IDLE enters WAITING. ACK in WAITING returns
to IDLE rather than entering DONE. ERROR in WAITING returns to IDLE rather than
entering FAILED.

If no ACK arrives within 5 seconds, the sender silently drops the request and
does not emit ERROR.
