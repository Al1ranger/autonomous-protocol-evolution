# TaskRelay v2 — additive candidate

All TaskRelay v1 REQUEST, ACK, and ERROR messages remain valid and retain their
required fields and meanings. REQUEST still requires string request_id and payload;
ACK still requires string request_id and completes the matching request; ERROR
still requires request_id and reason. A receiver MUST preserve request_id unchanged
in all responses. REQUEST MAY additionally carry optional string trace_id.

The initial state remains IDLE. REQUEST in IDLE enters WAITING. Matching ACK in
WAITING enters DONE; matching ERROR in WAITING enters FAILED. No existing
transition is removed or reinterpreted. A new optional PING message in IDLE
leaves the receiver in IDLE and does not affect any REQUEST.

If no ACK arrives within 30 seconds of entering WAITING, the sender MUST emit
ERROR with the original request_id and reason TIMEOUT, then enter FAILED.
