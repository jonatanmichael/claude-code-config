# quality_reviewer/

Quality Review modules for all plan phases, with QA decomposition and verification.

## Files

| File                        | What                                                   | When to read                                   |
| --------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| `README.md`                 | QR architecture, QA integration, state file naming     | Understanding QR workflow, phase state files   |
| `qr_verify_base.py`         | Base verification logic shared across QR phases        | Modifying shared verification behavior         |
| `exec_reconcile.py`         | Reconciliation between plan and implementation         | Modifying reconciliation step                  |
| `impl_code_qr_decompose.py` | Decomposes impl-code QA into verifiable items          | Modifying Code QR decomposition                |
| `impl_code_qr_verify.py`    | Verifies individual impl-code QA items                 | Modifying Code QR verification                 |
| `impl_docs_qr_decompose.py` | Decomposes impl-docs QA into verifiable items          | Modifying Doc QR decomposition                 |
| `impl_docs_qr_verify.py`    | Verifies individual impl-docs QA items                 | Modifying Doc QR verification                  |
| `plan_code_qr_decompose.py` | Decomposes plan-code QA into verifiable items          | Modifying plan Code QR decomposition           |
| `plan_code_qr_verify.py`    | Verifies individual plan-code QA items                 | Modifying plan Code QR verification            |
| `plan_design_qr_decompose.py` | Decomposes plan-design QA into verifiable items      | Modifying plan design QR decomposition         |
| `plan_design_qr_verify.py`  | Verifies individual plan-design QA items               | Modifying plan design QR verification          |
| `plan_docs_qr_decompose.py` | Decomposes plan-docs QA into verifiable items          | Modifying plan docs QR decomposition           |
| `plan_docs_qr_verify.py`    | Verifies individual plan-docs QA items                 | Modifying plan docs QR verification            |

## Subdirectories

| Directory | What                            | When to read                     |
| --------- | ------------------------------- | -------------------------------- |
| `prompts/` | Prompt templates for QR phases | Modifying QR prompt content      |
