"""Structural tests for impl_code_qr.py and impl_docs_qr.py entry points."""

import pytest

from skills.planner.quality_reviewer.impl_code_qr import get_step_guidance as code_qr_guidance
from skills.planner.quality_reviewer.impl_code_qr import PHASE as CODE_PHASE
from skills.planner.quality_reviewer.impl_docs_qr import get_step_guidance as docs_qr_guidance
from skills.planner.quality_reviewer.impl_docs_qr import PHASE as DOCS_PHASE


STATE_DIR = "/tmp/test-state"
MODULE_CODE = "skills.planner.quality_reviewer.impl_code_qr"
MODULE_DOCS = "skills.planner.quality_reviewer.impl_docs_qr"


class TestImplCodeQrStructure:
    """Verify get_step_guidance returns correct keys and references for each step."""

    def test_phase_constant(self):
        assert CODE_PHASE == "impl-code"

    def test_step_1_returns_required_keys(self):
        result = code_qr_guidance(1, MODULE_CODE, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_2_returns_required_keys(self):
        result = code_qr_guidance(2, MODULE_CODE, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_3_returns_required_keys(self):
        result = code_qr_guidance(3, MODULE_CODE, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_4_returns_required_keys(self):
        result = code_qr_guidance(4, MODULE_CODE, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_1_actions_contain_decompose_module(self):
        result = code_qr_guidance(1, MODULE_CODE, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "impl_code_qr_decompose" in actions_text

    def test_step_2_actions_contain_verify_module(self, tmp_path):
        import json
        (tmp_path / "qr-impl-code.json").write_text(json.dumps(
            {"phase": "impl-code", "items": [{"id": "QR-001", "group_id": "G1", "scope": "M-001"}]}
        ))
        result = code_qr_guidance(2, MODULE_CODE, state_dir=str(tmp_path))
        actions_text = " ".join(result["actions"])
        assert "impl_code_qr_verify" in actions_text

    def test_step_2_actions_contain_task_dispatch(self, tmp_path):
        import json
        (tmp_path / "qr-impl-code.json").write_text(json.dumps(
            {"phase": "impl-code", "items": [{"id": "QR-001", "group_id": "G1", "scope": "M-001"}]}
        ))
        result = code_qr_guidance(2, MODULE_CODE, state_dir=str(tmp_path))
        actions_text = " ".join(result["actions"])
        assert "Task" in actions_text

    def test_step_4_actions_contain_pass_format(self):
        result = code_qr_guidance(4, MODULE_CODE, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "PASS" in actions_text

    def test_step_4_actions_contain_issues_format(self):
        result = code_qr_guidance(4, MODULE_CODE, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "ISSUES" in actions_text or "issues" in actions_text

    def test_step_beyond_max_returns_step_4_content(self):
        result = code_qr_guidance(99, MODULE_CODE, state_dir=STATE_DIR)
        assert result["title"] == "Report"

    def test_next_command_contains_state_dir(self):
        result = code_qr_guidance(1, MODULE_CODE, state_dir=STATE_DIR)
        assert STATE_DIR in result["next"]


class TestImplDocsQrStructure:
    def test_phase_constant(self):
        assert DOCS_PHASE == "impl-docs"

    def test_step_1_returns_required_keys(self):
        result = docs_qr_guidance(1, MODULE_DOCS, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_2_returns_required_keys(self):
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_3_returns_required_keys(self):
        result = docs_qr_guidance(3, MODULE_DOCS, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_4_returns_required_keys(self):
        result = docs_qr_guidance(4, MODULE_DOCS, state_dir=STATE_DIR)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_step_1_actions_contain_decompose_module(self):
        result = docs_qr_guidance(1, MODULE_DOCS, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "impl_docs_qr_decompose" in actions_text

    def test_step_2_actions_contain_verify_module(self, tmp_path):
        import json
        (tmp_path / "qr-impl-docs.json").write_text(json.dumps(
            {"phase": "impl-docs", "items": [{"id": "QR-001", "group_id": "G1", "scope": "M-001"}]}
        ))
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=str(tmp_path))
        actions_text = " ".join(result["actions"])
        assert "impl_docs_qr_verify" in actions_text

    def test_step_2_actions_contain_task_dispatch(self, tmp_path):
        import json
        (tmp_path / "qr-impl-docs.json").write_text(json.dumps(
            {"phase": "impl-docs", "items": [{"id": "QR-001", "group_id": "G1", "scope": "M-001"}]}
        ))
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=str(tmp_path))
        actions_text = " ".join(result["actions"])
        assert "Task" in actions_text

    def test_step_4_actions_contain_pass_format(self):
        result = docs_qr_guidance(4, MODULE_DOCS, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "PASS" in actions_text

    def test_step_4_actions_contain_issues_format(self):
        result = docs_qr_guidance(4, MODULE_DOCS, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "ISSUES" in actions_text or "issues" in actions_text

    def test_step_beyond_max_returns_step_4_content(self):
        result = docs_qr_guidance(99, MODULE_DOCS, state_dir=STATE_DIR)
        assert result["title"] == "Report"

    def test_next_command_contains_state_dir(self):
        result = docs_qr_guidance(1, MODULE_DOCS, state_dir=STATE_DIR)
        assert STATE_DIR in result["next"]


class TestStep2HandlerParallelDispatch:
    """Verify step_2_handler parallel dispatch behavior after the parallel_constraint fix."""

    def test_code_qr_empty_state_dir_returns_fallback(self):
        result = code_qr_guidance(2, MODULE_CODE, state_dir="")
        actions_text = " ".join(result["actions"])
        assert "FALLBACK" in actions_text
        assert "Task" in actions_text

    def test_docs_qr_empty_state_dir_returns_fallback(self):
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir="")
        actions_text = " ".join(result["actions"])
        assert "FALLBACK" in actions_text
        assert "Task" in actions_text

    def test_code_qr_with_three_groups_contains_mandatory_parallel(self, tmp_path):
        qr_file = {"phase": "impl-code", "items": [
            {"id": "QR-001", "group_id": "G1", "scope": "M-001"},
            {"id": "QR-002", "group_id": "G1", "scope": "M-001"},
            {"id": "QR-003", "group_id": "G2", "scope": "M-002"},
            {"id": "QR-004", "group_id": "G3", "scope": "M-003"},
        ]}
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-code.json").write_text(__import__("json").dumps(qr_file))
        result = code_qr_guidance(2, MODULE_CODE, state_dir=state_dir)
        actions_text = " ".join(result["actions"])
        assert "MANDATORY" in actions_text
        assert "3" in actions_text

    def test_docs_qr_with_three_groups_contains_mandatory_parallel(self, tmp_path):
        qr_file = {"phase": "impl-docs", "items": [
            {"id": "QR-001", "group_id": "G1", "scope": "M-001"},
            {"id": "QR-002", "group_id": "G2", "scope": "M-002"},
            {"id": "QR-003", "group_id": "G3", "scope": "M-003"},
        ]}
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-docs.json").write_text(__import__("json").dumps(qr_file))
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=state_dir)
        actions_text = " ".join(result["actions"])
        assert "MANDATORY" in actions_text
        assert "3" in actions_text

    def test_code_qr_corrupt_json_returns_fallback_not_crash(self, tmp_path):
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-code.json").write_text("{ invalid json {")
        result = code_qr_guidance(2, MODULE_CODE, state_dir=state_dir)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_docs_qr_corrupt_json_returns_fallback_not_crash(self, tmp_path):
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-docs.json").write_text("not json at all")
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=state_dir)
        assert "title" in result
        assert "actions" in result
        assert "next" in result

    def test_code_qr_fallback_appears_after_parallel_constraint(self, tmp_path):
        """DL-004 ordering invariant: MANDATORY parallel before FALLBACK sequential."""
        qr_file = {"phase": "impl-code", "items": [
            {"id": "QR-001", "group_id": "G1", "scope": "M-001"},
            {"id": "QR-002", "group_id": "G2", "scope": "M-002"},
        ]}
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-code.json").write_text(__import__("json").dumps(qr_file))
        result = code_qr_guidance(2, MODULE_CODE, state_dir=state_dir)
        actions_text = " ".join(result["actions"])
        mandatory_pos = actions_text.find("MANDATORY")
        fallback_pos = actions_text.find("FALLBACK")
        assert mandatory_pos != -1, "MANDATORY text not found"
        assert fallback_pos != -1, "FALLBACK text not found"
        assert mandatory_pos < fallback_pos, "MANDATORY must appear before FALLBACK (DL-004)"

    def test_docs_qr_fallback_appears_after_parallel_constraint(self, tmp_path):
        """DL-004 ordering invariant: MANDATORY parallel before FALLBACK sequential."""
        qr_file = {"phase": "impl-docs", "items": [
            {"id": "QR-001", "group_id": "G1", "scope": "M-001"},
            {"id": "QR-002", "group_id": "G2", "scope": "M-002"},
        ]}
        state_dir = str(tmp_path)
        (tmp_path / "qr-impl-docs.json").write_text(__import__("json").dumps(qr_file))
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=state_dir)
        actions_text = " ".join(result["actions"])
        mandatory_pos = actions_text.find("MANDATORY")
        fallback_pos = actions_text.find("FALLBACK")
        assert mandatory_pos != -1, "MANDATORY text not found"
        assert fallback_pos != -1, "FALLBACK text not found"
        assert mandatory_pos < fallback_pos, "MANDATORY must appear before FALLBACK (DL-004)"
