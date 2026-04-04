#!/usr/bin/env python3
"""Orchestration entry point for the impl-code quality review phase.

Guides the quality-reviewer agent through a 4-step pipeline:
  1. Decompose  -- invoke impl_code_qr_decompose to populate qr-impl-code.json
  2. Fan-Out    -- dispatch parallel verify agents per group_id (ref: DL-005)
  3. Aggregate  -- tally PASS/FAIL/UNVERIFIED from qr-impl-code.json
  4. Report     -- emit PASS or ISSUES XML grouped by milestone (ref: DL-006)

Follows the flat STEPS dict pattern from exec_reconcile.py (ref: DL-001).
Delegates all decompose and verify logic to sub-scripts; does not duplicate
their implementation (ref: DL-003).
"""

import json
import os
from skills.lib.workflow.prompts import parallel_constraint


# PHASE must match impl_code_qr_decompose.py and impl_code_qr_verify.py --
# the state file is named qr-{PHASE}.json and lookup fails on mismatch. (ref: RSK-001)
PHASE = "impl-code"


STEPS = {
    1: {
        "title": "Decompose",
    },
    2: {
        "title": "Fan-Out Verify",
    },
    3: {
        "title": "Aggregate",
    },
    4: {
        "title": "Report",
    },
}


def step_1_handler(step_info, total_steps, module_path, **kwargs):
    """Return agent guidance for Step 1: invoke the decompose sub-script."""
    state_dir = kwargs.get("state_dir", "")
    return {
        "title": step_info["title"],
        "actions": [
            "TASK: Run impl-code QR decomposition to generate verification items.",
            "",
            "INVOKE the decompose sub-script and follow ALL its steps until completion:",
            f"  python3 -m skills.planner.quality_reviewer.impl_code_qr_decompose --step 1 --state-dir {state_dir}",
            "",
            "Continue invoking subsequent steps as instructed by each step's 'next' command.",
            "Do NOT proceed until decomposition is fully complete.",
            "",
            "If decomposition fails or errors, report the error and halt -- do not proceed.",
        ],
        "next": f"python3 -m {module_path} --step 2 --state-dir {state_dir}",
    }


def step_2_handler(step_info, total_steps, module_path, **kwargs):
    """Return agent guidance for Step 2: fan out verify agents per group_id.

    Loads qr-impl-code.json at generation time, groups by group_id, and injects
    parallel_constraint(N) so the LLM dispatches exactly N agents simultaneously.
    Falls back to advisory prose when state_dir is empty or JSON is unavailable.
    (ref: DL-002, DL-003, DL-004, RSK-002)
    """
    state_dir = kwargs.get("state_dir", "")

    if not state_dir:
        return {
            "title": step_info["title"],
            "actions": [
                "DISPATCH parallel verify agents -- one Task per group_id:",
                "  For each group, spawn a Task with:",
                "    python3 -m skills.planner.quality_reviewer.impl_code_qr_verify --step 1",
                "      --state-dir <STATE_DIR> --qr-item <item_id> ...",
                "",
                "FALLBACK (if Task tool is unavailable):",
                "  Invoke verify sub-script sequentially for each group.",
                "",
                "Wait for ALL verify agents/invocations to complete before proceeding.",
            ],
            "next": f"python3 -m {module_path} --step 3 --state-dir {state_dir}",
        }

    qr_path = os.path.join(state_dir, "qr-impl-code.json")
    try:
        with open(qr_path) as f:
            data = json.load(f)
        items = data.get("items", [])
        groups = {}
        for item in items:
            gid = item.get("group_id") or item.get("id", "default")
            groups.setdefault(gid, []).append(item)
        group_count = len(groups)
    except (FileNotFoundError, json.JSONDecodeError):
        group_count = 0
        groups = {}

    if group_count == 0:
        return {
            "title": step_info["title"],
            "actions": [
                "READ qr-impl-code.json -- file missing, empty, or unparseable.",
                "No verification items found.",
                f"Skip to step 4: python3 -m {module_path} --step 4 --state-dir {state_dir}",
            ],
            "next": f"python3 -m {module_path} --step 3 --state-dir {state_dir}",
        }

    actions = [
        parallel_constraint(group_count),
        "",
        "DISPATCH parallel verify agents -- one Task per group_id:",
        "  For each group, spawn a Task with:",
        "    python3 -m skills.planner.quality_reviewer.impl_code_qr_verify --step 1 \\\\",
        f"      --state-dir {state_dir} \\\\",
        "      --qr-item <item_id_1> --qr-item <item_id_2> ... (all items in group)",
        "",
        "FALLBACK (if Task tool is unavailable):",
        "  Invoke verify sub-script sequentially for each group:",
        "    python3 -m skills.planner.quality_reviewer.impl_code_qr_verify --step 1 \\\\",
        f"      --state-dir {state_dir} --qr-item <item_id> ...",
        "",
        "Wait for ALL verify agents/invocations to complete before proceeding.",
    ]
    return {
        "title": step_info["title"],
        "actions": actions,
        "next": f"python3 -m {module_path} --step 3 --state-dir {state_dir}",
    }


def step_3_handler(step_info, total_steps, module_path, **kwargs):
    """Return agent guidance for Step 3: aggregate verify results from qr state."""
    state_dir = kwargs.get("state_dir", "")
    return {
        "title": step_info["title"],
        "actions": [
            "RE-READ qr-impl-code.json after all verify agents have completed:",
            f"  cat {state_dir}/qr-impl-code.json",
            "",
            "For each item in the file:",
            "  - Record status (PASS / FAIL / UNVERIFIED)",
            "  - Items without a verify result are treated as UNVERIFIED (fail)",
            "",
            "SUMMARIZE findings:",
            "  Total items: N",
            "  PASS: N | FAIL: N | UNVERIFIED: N",
            "",
            "List all failed or unverified items with their scope and check fields.",
        ],
        "next": f"python3 -m {module_path} --step 4 --state-dir {state_dir}",
    }


def step_4_handler(step_info, total_steps, module_path, **kwargs):
    """Return agent guidance for Step 4: emit PASS or ISSUES report.

    Output is LLM-consumed by the executor gate, not programmatically parsed.
    PASS/ISSUES keywords trigger routing at executor step 5. (ref: DL-006, DL-012)
    """
    state_dir = kwargs.get("state_dir", "")
    return {
        "title": step_info["title"],
        "actions": [
            "OUTPUT the quality review result based on Step 3 aggregate summary.",
            "",
            "If ALL items PASSED (zero failures, zero unverified):",
            "  Output exactly:",
            "    PASS",
            "",
            "If ANY items FAILED or UNVERIFIED:",
            "  Output ISSUES grouped by milestone scope:",
            "",
            "  <issues>",
            "  <milestone id=\"M-NNN\">",
            "    <issue severity=\"MUST|SHOULD|COULD\">",
            "      <check>[check description from qr item]</check>",
            "      <finding>[finding from verify agent]</finding>",
            "    </issue>",
            "  </milestone>",
            "  </issues>",
            "",
            "Group all issues under their milestone scope.",
            "Items with scope '*' (macro checks) go under <milestone id=\"*\">.",
        ],
        "next": "",
    }


STEP_HANDLERS = {
    1: step_1_handler,
    2: step_2_handler,
    3: step_3_handler,
    4: step_4_handler,
}


def get_step_guidance(step: int, module_path: str = None, **kwargs) -> dict:
    """Return step guidance dict for the quality-reviewer agent.

    Args:
        step: Current step number (1-indexed)
        module_path: Module path for -m invocation
        **kwargs: Expects state_dir str; passed through to step handlers.

    Returns:
        dict with keys title (str), actions (list[str]), next (str).
        Steps beyond the maximum clamp to step 4. (ref: DL-002)
    """
    total_steps = len(STEPS)
    step_info = STEPS.get(step, {})
    handler = STEP_HANDLERS.get(step)

    if step >= total_steps:
        handler = STEP_HANDLERS.get(4)
        step_info = STEPS.get(4, {})

    if handler:
        return handler(step_info, total_steps=total_steps, module_path=module_path, **kwargs)

    return {"title": "Unknown", "actions": ["Check step number"], "next": ""}


if __name__ == "__main__":
    from skills.lib.workflow.cli import mode_main
    mode_main(
        __file__,
        get_step_guidance,
        "QR-Impl-Code: Orchestrate impl-code quality review pipeline",
        extra_args=[
            # default="" preserved for backward compatibility; executor.py STEPS[4] invoke_suffix
            # injects --state-dir at dispatch time. step_2_handler guards empty state_dir and
            # falls back to advisory prose when omitted. (ref: DL-001, DL-003, DL-004, RSK-002)
            (["--state-dir"], {"type": str, "default": "", "help": "State directory path"}),
        ],
    )
