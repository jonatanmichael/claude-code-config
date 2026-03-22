# orchestrator/

Main planner workflows: plan creation (`planner.py`) and step execution (`executor.py`).

`executor.py` registers all fix-mode router mappings in `FIX_ROUTER_MAP` (module level). Each key is a `fix_target` string matching an `AgentRole` value; each value is the router script path relative to the planner package. When adding a new `AgentRole`, add its entry to `FIX_ROUTER_MAP` or dispatch fails with `KeyError`.

## Dispatch Architecture

Fix-mode dispatches use routers, not leaf fix scripts:

- `developer/exec-implement.py` routes to the correct developer fix target
- `technical_writer/exec-docs.py` routes to the correct TW fix target
- Leaf scripts (e.g. `exec_implement_qr_fix.py`) are internal targets routed to by these routers

Dispatching directly to a leaf script bypasses routing and breaks fix-mode detection.

## fix_target String Invariant

`fix_target` is dual-use: it must match a `FIX_ROUTER_MAP` key (to resolve the router script)
AND the `agent_type` argument passed to `subagent_dispatch` (to set the agent identity). These
are the same string. When adding a new `AgentRole`, both `FIX_ROUTER_MAP` and the corresponding
`AgentRole` enum value must use the same string.

## Fix-Mode Routing Invariants

Routers detect fix mode by calling `has_qr_failures(state_dir)`. When `state_dir` is `None`
the router defaults to execute mode. Every fix-mode `invoke_cmd` must include `--state-dir $STATE_DIR`.

Step 3 (`format_step_3_implementation`) and step 6 (`format_step_6_documentation`) dispatch sites
are structural analogs and follow the same fix-mode pattern. The generic QR handler
(`handle_qr_step_generic`) applies the same requirement to all other QR steps.

## Standard Args

`--qr-fail` and `--qr-iteration` are accepted by all `mode_main` scripts but are not used
for routing decisions. Routing is purely state-file based.
