# orchestrator/

Main planner entry points: multi-step plan creation and step-by-step plan execution.

## Files

| File          | What                                                           | When to read                                              |
| ------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| `planner.py`  | Plan creation workflow (context gathering, architect)          | Modifying planning steps, plan state management           |
| `executor.py` | Plan execution workflow (9-step: dev, QR, TW, retro); FIX_ROUTER_MAP | Modifying execution steps, QR dispatch, fix routing |
| `README.md`   | Dispatch architecture, fix_target dual-use invariant, fix-mode routing invariants, FIX_ROUTER_MAP maintenance | Adding AgentRole, debugging fix dispatch failures |
