# orchestrator/

Main planner entry points: multi-step plan creation and step-by-step plan execution.

## Files

| File          | What                                                           | When to read                                              |
| ------------- | -------------------------------------------------------------- | --------------------------------------------------------- |
| `planner.py`  | 14-step planning workflow with QR gates for all three phases   | Modifying planning flow, adding planning steps            |
| `executor.py` | Step formatting and fix-mode dispatch for execution workflows  | Debugging fix-mode routing, modifying dispatch commands   |
| `README.md`   | Dispatch architecture, fix-mode routing invariants             | Before modifying any dispatch site in executor.py         |
