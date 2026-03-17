"""Per-project planner configuration.

Loads from (priority order):
  1. state_dir/planner.config.json (written by init, copied from project)
  2. <project>/.claude/planner.config.json (found by searching up from CWD)
  3. Built-in defaults

WHY two-stage loading: init_step copies project config into state_dir so
all subsequent steps can read it without CWD assumptions. CWD may differ
between planner invocations in a long session.
"""

import json
from pathlib import Path

DEFAULTS: dict = {
    "qr_iteration_limit": 5,
    "severity_thresholds": {
        "1": ["MUST", "SHOULD", "COULD"],
        "3": ["MUST", "SHOULD"],
        "4": ["MUST"],
    },
}

CONFIG_FILENAME = "planner.config.json"
PROJECT_CONFIG_PATH = f".claude/{CONFIG_FILENAME}"


def find_project_config() -> "Path | None":
    """Search upward from CWD for .claude/planner.config.json."""
    current = Path.cwd()
    for directory in [current, *current.parents]:
        candidate = directory / PROJECT_CONFIG_PATH
        if candidate.exists():
            return candidate
    return None


def load_project_config() -> dict:
    """Load and merge project config with defaults.

    Returns merged config (project overrides defaults).
    Falls back to defaults if no project config found or on parse error.
    """
    config_path = find_project_config()
    if not config_path:
        return dict(DEFAULTS)

    try:
        user_config = json.loads(config_path.read_text())
        # Deep merge nested dicts so partial overrides don't discard defaults.
        # Example: {"severity_thresholds": {"3": ["MUST"]}} should override
        # only key "3", not replace the entire severity_thresholds dict.
        merged = dict(DEFAULTS)
        for key, value in user_config.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = {**merged[key], **value}
            else:
                merged[key] = value
        return merged
    except (json.JSONDecodeError, IOError):
        return dict(DEFAULTS)


def write_config_to_state(state_dir: str) -> dict:
    """Detect project config and persist it to state_dir/planner.config.json.

    Called during plan-init (step 1). Returns the resolved config dict.

    WHY persist to state_dir: CWD at step 1 is the project root. Later
    steps may run from different working directories. Persisting to
    state_dir ensures all steps read the same config without CWD.
    """
    config = load_project_config()
    Path(state_dir, CONFIG_FILENAME).write_text(json.dumps(config, indent=2))
    return config


def read_config_from_state(state_dir: str) -> dict:
    """Read config from state_dir (written by write_config_to_state).

    Falls back to defaults if file missing (e.g., legacy state dirs
    created before this feature existed).
    """
    if not state_dir:
        return dict(DEFAULTS)

    path = Path(state_dir) / CONFIG_FILENAME
    if not path.exists():
        return dict(DEFAULTS)

    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, IOError):
        return dict(DEFAULTS)
