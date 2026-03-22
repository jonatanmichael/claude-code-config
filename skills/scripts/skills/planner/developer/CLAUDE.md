# developer/

Developer sub-agent workflows for code filling (plan phase) and implementation (execution phase), each with a router, execute script, and QR-fix script.

## Files

| File                       | What                                                               | When to read                                           |
| -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------ |
| `plan_code.py`             | Router: dispatches plan-code phase to execute or QR-fix            | Debugging plan-code routing decisions                  |
| `plan_code_execute.py`     | 4-step first-time code filling workflow (diffs into plan.json)     | Modifying plan-code execution steps                    |
| `plan_code_qr_fix.py`      | 3-step targeted repair workflow for plan-code QR failures          | Modifying plan-code fix behavior                       |
| `exec_implement.py`        | Router: dispatches impl-code phase to execute or QR-fix            | Debugging impl-code routing decisions                  |
| `exec_implement_execute.py`| 4-step wave-aware implementation workflow for first-time runs      | Modifying implementation execution steps               |
| `exec_implement_qr_fix.py` | 3-step targeted repair workflow for impl-code QR failures          | Modifying implementation fix behavior                  |
