# quality_reviewer/

Quality Review modules for all plan phases, with QA decomposition and verification.

## Files

| File                        | What                                                        | When to read                                              |
| --------------------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| `README.md`                 | QR architecture, QA integration, orchestration entry points | Understanding QR workflow, QA state tracking              |
| `impl_code_qr.py`           | Orchestration entry point for impl-code QR phase            | Modifying impl-code QR pipeline, debugging executor step 4 |
| `impl_docs_qr.py`           | Orchestration entry point for impl-docs QR phase            | Modifying impl-docs QR pipeline, debugging executor step 7 |
| `impl_code_qr_decompose.py` | Decompose sub-script for impl-code phase                    | Modifying impl-code decomposition logic                   |
| `impl_code_qr_verify.py`    | Verify sub-script for impl-code phase                       | Modifying impl-code verification logic                    |
| `impl_docs_qr_decompose.py` | Decompose sub-script for impl-docs phase                    | Modifying impl-docs decomposition logic                   |
| `impl_docs_qr_verify.py`    | Verify sub-script for impl-docs phase                       | Modifying impl-docs verification logic                    |
| `exec_reconcile.py`         | Orchestration entry point for reconciliation QR phase       | Modifying reconciliation QR pipeline                      |
| `qr_verify_base.py`         | Shared base logic for verify sub-scripts                    | Modifying verify behavior across phases                   |
| `plan_code_qr_decompose.py` | Decompose sub-script for plan-code phase                    | Modifying plan-code decomposition logic                   |
| `plan_code_qr_verify.py`    | Verify sub-script for plan-code phase                       | Modifying plan-code verification logic                    |
| `plan_design_qr_decompose.py` | Decompose sub-script for plan-design phase                | Modifying plan-design decomposition logic                 |
| `plan_design_qr_verify.py`  | Verify sub-script for plan-design phase                     | Modifying plan-design verification logic                  |
| `plan_docs_qr_decompose.py` | Decompose sub-script for plan-docs phase                    | Modifying plan-docs decomposition logic                   |
| `plan_docs_qr_verify.py`    | Verify sub-script for plan-docs phase                       | Modifying plan-docs verification logic                    |
