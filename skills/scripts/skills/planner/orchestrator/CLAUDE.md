# orchestrator/

Main entry points for the plan-execute workflow.

## Files

| File          | What                                                  | When to read                                    |
| ------------- | ----------------------------------------------------- | ----------------------------------------------- |
| `planner.py`  | Plan creation workflow (context gathering, architect) | Modifying planning steps, plan state management |
| `executor.py` | Plan execution workflow (9-step: dev, QR, TW, retro)  | Modifying execution steps, QR dispatch, routing |
