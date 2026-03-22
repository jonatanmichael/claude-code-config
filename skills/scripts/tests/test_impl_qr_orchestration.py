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

    def test_step_2_actions_contain_verify_module(self):
        result = code_qr_guidance(2, MODULE_CODE, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "impl_code_qr_verify" in actions_text

    def test_step_2_actions_contain_task_dispatch(self):
        result = code_qr_guidance(2, MODULE_CODE, state_dir=STATE_DIR)
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

    def test_step_2_actions_contain_verify_module(self):
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=STATE_DIR)
        actions_text = " ".join(result["actions"])
        assert "impl_docs_qr_verify" in actions_text

    def test_step_2_actions_contain_task_dispatch(self):
        result = docs_qr_guidance(2, MODULE_DOCS, state_dir=STATE_DIR)
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
