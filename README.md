# F95 | Agentic STEM Laboratory Planner | L3 Gold Standard | v1.0

A governed, planning-only multi-agent education reference system for laboratory objectives, procedure planning, safety review, resource planning, and learning assessment.

## Five-agent architecture

- Lab Objective Agent
- Procedure Planner
- Safety Reviewer
- Resource Planner
- Learning Assessment Agent

## Gold-standard laboratory governance

F95 is fail closed and planning only. Release requires reviewed learning objectives, procedures, hazards, equipment, materials, waste disposal, accessibility, supervision, and explicit qualified-human approval.

Release is blocked for unresolved hazards, incomplete procedure validation, equipment-safety gaps, inadequate hazardous-material controls, waste-disposal gaps, accessibility gaps, supervision gaps, or incomplete emergency-response planning.

The reference system cannot authorize physical laboratory execution, hazardous-material use, equipment activation, safety-rule overrides, unsupervised student activity, or external institutional submission. Qualified local laboratory supervision and institutional safety requirements remain authoritative.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out laboratory-governance suite.
