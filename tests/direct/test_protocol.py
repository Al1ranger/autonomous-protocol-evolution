import hashlib
import json


SOURCE_A = "https://spec.example.org/v1"
SOURCE_B = "https://spec.example.org/v2"
BASE = b"REQUEST requires id; timeout emits ERROR."
NEXT = b"REQUEST requires id; timeout emits ERROR; optional trace_id added."


def hashed(body):
    return hashlib.sha256(body).hexdigest()


def setup_active(direct_vm, direct_deploy, direct_alice):
    contract = direct_deploy("contracts/AutonomousProtocolEvolution.py")
    direct_vm.sender = direct_alice
    contract.register_protocol("taskrelay", "TaskRelay", SOURCE_A, hashed(BASE))
    direct_vm.mock_web(r".*spec\.example\.org/v1", {"status": 200, "body": BASE})
    contract.activate_protocol("taskrelay")
    return contract


def test_baseline_requires_exact_fetched_hash(direct_vm, direct_deploy, direct_alice):
    contract = direct_deploy("contracts/AutonomousProtocolEvolution.py")
    direct_vm.sender = direct_alice
    contract.register_protocol("taskrelay", "TaskRelay", SOURCE_A, hashed(BASE))
    direct_vm.mock_web(r".*spec\.example\.org/v1", {"status": 200, "body": b"changed"})
    with direct_vm.expect_revert("baseline specification unavailable or hash-mismatched"):
        contract.activate_protocol("taskrelay")
    assert contract.get_protocol("taskrelay")["status"] == "DRAFT"


def test_member_must_accept_and_proposal_is_protocol_bound(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup_active(direct_vm, direct_deploy, direct_alice)
    contract.invite_member("taskrelay", "0x" + direct_bob.hex())
    direct_vm.sender = direct_bob
    with direct_vm.expect_revert("active member required"):
        contract.propose_upgrade("taskrelay", "change-a", 0, SOURCE_B, hashed(NEXT))
    contract.accept_membership("taskrelay")
    contract.propose_upgrade("taskrelay", "change-a", 0, SOURCE_B, hashed(NEXT))
    assert contract.get_proposal("change-a")["protocol_id"] == "taskrelay"
    direct_vm.sender = direct_alice
    contract.register_protocol("other", "Other", SOURCE_A, hashed(BASE))
    with direct_vm.expect_revert("proposal belongs to another protocol"):
        contract.resolve_upgrade("other", "change-a")
    assert contract.get_protocol("other")["status"] == "DRAFT"


def test_consensus_vector_promotes_only_all_pass(direct_vm, direct_deploy, direct_alice):
    contract = setup_active(direct_vm, direct_deploy, direct_alice)
    contract.propose_upgrade("taskrelay", "add-trace", 0, SOURCE_B, hashed(NEXT))
    direct_vm.mock_web(r".*spec\.example\.org/v2", {"status": 200, "body": NEXT})
    direct_vm.mock_llm(
        r".*Compare the OLD protocol.*",
        json.dumps({"messages": "PASS", "transitions": "PASS",
                    "errors": "PASS", "coherence": "PASS"}),
    )
    contract.resolve_upgrade("taskrelay", "add-trace")
    assert contract.get_proposal("add-trace")["status"] == "ACTIVATED"
    assert contract.get_protocol("taskrelay")["active_version"] == 1
    assert contract.get_version("taskrelay", 1)["sha256"] == hashed(NEXT)
    with direct_vm.expect_revert("proposal terminal or protocol inactive"):
        contract.resolve_upgrade("taskrelay", "add-trace")


def test_unknown_dimension_fails_closed(direct_vm, direct_deploy, direct_alice):
    contract = setup_active(direct_vm, direct_deploy, direct_alice)
    contract.propose_upgrade("taskrelay", "unclear", 0, SOURCE_B, hashed(NEXT))
    direct_vm.mock_web(r".*spec\.example\.org/v2", {"status": 200, "body": NEXT})
    direct_vm.mock_llm(
        r".*Compare the OLD protocol.*",
        json.dumps({"messages": "PASS", "transitions": "UNKNOWN",
                    "errors": "PASS", "coherence": "PASS"}),
    )
    contract.resolve_upgrade("taskrelay", "unclear")
    assert contract.get_proposal("unclear")["status"] == "INCONCLUSIVE"
    assert contract.get_protocol("taskrelay")["active_version"] == 0
