# TaskRelay v1 — normative specification

Message REQUEST has required string fields request_id and payload. A receiver MUST
preserve request_id unchanged in all responses. Message ACK has required string
field request_id and indicates completion of the matching REQUEST. Message ERROR
has required fields request_id and reason.

The initial state is IDLE. A REQUEST in IDLE enters WAITING. An ACK with the
matching request_id in WAITING enters DONE. An ERROR with the matching request_id
in WAITING enters FAILED. No other state transition is valid.

If no ACK arrives within 30 seconds of entering WAITING, the sender MUST emit
ERROR with the original request_id and reason TIMEOUT, then enter FAILED.
