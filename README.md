# F95 Agentic STEM Laboratory Planner

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for STEM laboratory planning across learning objectives, procedure decomposition, hazard review, equipment and material planning, waste handling, accessibility, supervision, emergency-response preparation, learning assessment, and qualified human approval.

F95 is designed as a reusable planning-only multi-agent laboratory reference for schools, universities, training programs, teaching laboratories, makerspaces, and other educational environments that need structured support for designing laboratory experiences without transferring physical, safety, grading, or institutional authority to an automated system.

This repository supports laboratory planning and review. It does not autonomously execute laboratory work, authorize hazardous-material use, activate equipment, override safety requirements, permit unsupervised student activity, make formal accommodation decisions, assign final grades, or submit externally on behalf of an institution.

## Laboratory planning lifecycle

```text
learning objectives + laboratory context
                |
                v
        objective design
                |
                v
       procedure planning
                |
                v
         safety review
                |
                v
        resource planning
                |
                v
      learning assessment
                |
                v
    qualified human approval
```

The workflow is fail closed. Unresolved hazards, incomplete procedure validation, equipment-safety gaps, inadequate hazardous-material controls, incomplete waste-disposal planning, accessibility gaps, supervision gaps, emergency-response gaps, missing review evidence, or missing qualified-human approval remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Lab Objective Agent | Defines measurable laboratory learning objectives and maps them to the intended experience | What should learners understand or demonstrate through this laboratory activity? |
| Procedure Planner Agent | Decomposes the planned activity into reviewable stages, dependencies, and checkpoints | Is the proposed procedure coherent, teachable, and ready for qualified local validation? |
| Safety Reviewer Agent | Reviews hazards, controls, supervision, accessibility, waste, and emergency-response considerations | What could cause harm, what controls are required, and what must block release? |
| Resource Planner Agent | Structures equipment, materials, staffing, facility, and logistical requirements | Are the necessary resources available, appropriate, and safely supportable? |
| Learning Assessment Agent | Maps laboratory objectives to evidence of learning and review criteria | How will learners demonstrate the intended knowledge or skills without transferring final grading authority to the system? |

No agent independently authorizes physical laboratory execution, hazardous-material handling, equipment activation, student supervision, emergency decisions, or binding academic outcomes.

## Repository structure

```text
AGENTS/
├── lab_objective_agent.py
├── procedure_planner_agent.py
├── safety_reviewer_agent.py
├── resource_planner_agent.py
└── learning_assessment_agent.py

SKILLS/
├── objective_design.py
├── procedure_decomposition.py
├── lab_safety_review.py
├── resource_planning.py
└── learning_assessment.py

TOOLS/
├── objective_map_tool.py
├── procedure_checklist_tool.py
├── hazard_register_tool.py
├── resource_matrix_tool.py
└── assessment_map_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The structure separates planning reasoning from deterministic planning artifacts, fail-closed governance, evaluation, state, memory, observability, and reproducibility.

## Laboratory context

A useful planning record can include:

```text
laboratory_id
course_or_program
learner_level
learning_objectives
laboratory_type
location
facility_constraints
procedure_scope
equipment
materials
hazards
controls
waste_streams
supervision_model
accessibility_requirements
emergency_resources
assessment_evidence
qualified_owner
```

Laboratory recommendations must be interpreted within the actual institution, jurisdiction, facility, discipline, local policy, learner population, available supervision, and equipment environment.

## Learning objectives

Laboratory planning should begin with explicit educational objectives rather than selecting an experiment first and retrofitting learning claims afterward.

Objectives can address areas such as:

- measurement
- observation
- experimental design
- instrumentation
- data collection
- uncertainty
- analysis
- troubleshooting
- scientific reasoning
- engineering judgment
- technical communication
- teamwork
- safety practice
- reproducibility

The Lab Objective Agent should distinguish what learners are expected to observe, practice, analyze, or independently demonstrate.

## Objective mapping

`TOOLS/objective_map_tool.py` supports deterministic mapping between learning objectives and laboratory activities.

A useful mapping can include:

```text
objective_id
objective_description
laboratory_activity
evidence_expected
assessment_method
prerequisites
review_state
```

Every major procedure stage should have a pedagogical reason or a justified operational purpose.

## Prerequisite knowledge

A laboratory activity may depend on prerequisite knowledge or skills such as:

- mathematical methods
- measurement concepts
- instrument familiarity
- chemical or biological safety orientation
- electrical safety
- programming
- data-analysis methods
- prior laboratory techniques

The planner should surface missing prerequisites rather than assuming students possess them.

## Procedure decomposition

The Procedure Planner Agent structures the planned laboratory workflow into reviewable steps and checkpoints.

`TOOLS/procedure_checklist_tool.py` can represent stages such as:

```text
preparation
setup
pre-use inspection
instruction
controlled execution
observation
measurement
shutdown
cleanup
waste handling
data review
```

The reference system produces planning artifacts only. A generated procedure is not a substitute for locally approved standard operating procedures, equipment manuals, instructor validation, or institutional safety requirements.

## Procedure validation boundary

Procedure quality cannot be established from text generation alone.

A proposed procedure may require qualified human validation against:

- actual equipment
- actual materials
- facility capabilities
- manufacturer instructions
- local safety policy
- student experience level
- supervision availability
- emergency systems

If procedure validation is incomplete, release remains blocked.

## Hazard identification

`TOOLS/hazard_register_tool.py` supports structured hazard records.

A hazard register can include:

```text
hazard_id
hazard_source
hazard_type
possible_consequence
exposed_group
existing_control
required_control
residual_concern
qualified_owner
review_state
```

Relevant hazards vary by laboratory and may include electrical, mechanical, thermal, pressure, chemical, biological, optical, radiation, ergonomic, environmental, or behavioral risks.

The planner should not infer that absence of a known hazard means an activity is safe.

## Risk-control hierarchy

Where useful, safety review can distinguish controls such as:

```text
elimination
substitution
engineering controls
administrative controls
personal protective equipment
```

The system can organize candidate controls, but qualified local safety personnel remain responsible for determining what controls are sufficient for an actual laboratory.

## Hazardous materials

F95 does not authorize hazardous-material acquisition, storage, handling, mixing, use, transport, or disposal.

Planning may document:

- material identity
- intended educational role
- hazard classification supplied by authoritative sources
- storage requirements
- handling requirements
- incompatible materials
- required controls
- waste stream
- supervision requirement
- local approval state

Hazardous-material controls must be reviewed by qualified humans under applicable institutional and regulatory requirements.

## Equipment planning

The Resource Planner Agent can structure equipment requirements such as:

- instrument type
- quantity
- operating envelope
- calibration status
- inspection status
- required training
- guarding
- interlocks
- power requirements
- ventilation requirements
- emergency shutoff
- supervision requirement

F95 never treats equipment listing as permission to activate or operate equipment.

## Equipment safety boundary

Equipment activation is a protected action outside planner authority.

Before physical use, qualified personnel may need to verify:

- manufacturer instructions
- current inspection status
- calibration
- guards and interlocks
- electrical condition
- mechanical integrity
- emergency stop functions
- ventilation
- location suitability
- user training

An unresolved equipment-safety gap blocks planning-package release.

## Resource matrix

`TOOLS/resource_matrix_tool.py` supports structured resource planning.

A resource record can include:

```text
resource_id
resource_type
quantity
required_stage
availability
qualification_requirement
safety_dependency
substitution_allowed
owner
review_state
```

Resource planning should include staffing and supervision, not only physical materials.

## Supervision

Laboratory supervision is a safety-critical dependency.

Planning can identify:

- instructor presence
- teaching-assistant coverage
- technician support
- specialist supervision
- student-to-supervisor ratio
- restricted activities
- competency prerequisites
- escalation contacts

The system does not declare a supervision model adequate without qualified local review.

Unresolved supervision requirements block release.

## Unsupervised activity boundary

F95 must not authorize unsupervised student laboratory activity.

If a planned task requires qualified supervision and that supervision is unavailable or unclear, the correct state is a blocker or escalation, not an autonomous waiver.

## Emergency-response planning

Laboratory planning should identify relevant emergency-response dependencies before the activity begins.

Depending on the environment, review may include:

- emergency shutoff
- eyewash or safety shower
- fire response
- spill response
- first-aid access
- evacuation route
- emergency communications
- incident reporting
- local emergency contacts

F95 can organize planning information but does not replace local emergency procedures or real-time human emergency judgment.

An incomplete emergency-response plan is a release blocker.

## Waste planning

Waste handling should be planned before laboratory execution.

A waste plan can identify:

```text
waste_type
source_step
container_requirement
segregation_requirement
labeling_requirement
storage_location
qualified_owner
disposal_path
review_state
```

The planner must not invent disposal instructions when authoritative local requirements are unavailable.

A waste-disposal gap blocks release.

## Accessibility

Laboratory accessibility should be considered during design rather than only after barriers arise.

Review can consider:

- bench access
- instrument reach
- readable displays
- visual or auditory alerts
- accessible instructions
- captioning
- alternative formats
- physical navigation
- dexterity demands
- time constraints
- group-role flexibility
- remote or simulated alternatives where academically appropriate

The system can surface accessibility considerations but does not autonomously grant or deny formal accommodations.

## Accessibility and academic requirements

Accessible design should distinguish between:

```text
essential learning requirement
and
avoidable implementation barrier
```

That distinction remains a qualified academic and institutional judgment.

An unresolved accessibility requirement blocks release.

## Learning assessment

The Learning Assessment Agent maps laboratory objectives to evidence of learning.

`TOOLS/assessment_map_tool.py` can support mappings involving:

- observations
- lab notebooks
- data sets
- calculations
- plots
- technical explanations
- oral checks
- demonstrations
- reports
- design decisions
- error analysis
- reflection

Assessment should measure the stated learning objective rather than only whether students completed the physical procedure.

## Assessment evidence

Useful evidence can distinguish:

- participation
- correct procedure execution
- conceptual understanding
- independent analysis
- troubleshooting
- interpretation
- communication
- transfer of learning

Completion alone should not automatically be treated as mastery.

## Grading authority boundary

F95 may structure assessment criteria and evidence, but final grading remains with qualified educators and authorized institutional processes.

The system should not:

- assign final grades
- determine pass or fail status
- modify grade records
- make misconduct findings
- decide formal accommodations
- determine disciplinary consequences

## Safety review independence

Safety review should not be reduced to a procedural checkbox.

The Safety Reviewer Agent provides an independent path for identifying planning blockers after objectives and procedures have been proposed.

This separation helps reduce the risk that the same reasoning process both proposes an activity and assumes it is safe.

## Fail-closed governance

Planning-package release requires all required review fields to be present and affirmative.

The reference policy requires review of:

- learning objectives
- procedures
- hazards
- equipment
- materials
- waste disposal
- accessibility
- supervision
- qualified human approval

Release is blocked when any required review is missing.

Reference blockers include:

- unresolved laboratory hazard
- procedure validation incomplete
- equipment safety review incomplete
- hazardous-material controls inadequate
- waste-disposal controls incomplete
- accessibility requirement unresolved
- qualified-supervision requirement unresolved
- emergency-response planning incomplete

The system should expose the blocker rather than manufacture a complete-looking laboratory plan.

## Protected actions

The safety policy treats the following as outside planner authority:

```text
lab_execution
hazardous_material_use
equipment_activation
external_submission
override_safety_rule
unsupervised_student_activity
```

These actions are never made permissible merely because a planning package has passed review.

## Human authority boundaries

F95 must not autonomously:

- execute a physical laboratory procedure
- authorize hazardous-material use
- activate laboratory equipment
- override safety rules
- waive supervision requirements
- permit unsupervised student activity
- approve emergency-response deviations
- certify a laboratory as safe
- grant or deny formal accommodations
- assign final grades
- make disciplinary findings
- modify student records
- submit externally on behalf of an institution
- fabricate safety approvals, inspections, training, or institutional authorization

Qualified instructors, laboratory managers, environmental health and safety personnel, technicians, institutional authorities, and other authorized humans retain their respective decision rights.

## End-to-end reference workflow

A typical F95 workflow follows this sequence:

1. Define the laboratory's educational purpose and learner context.
2. Define measurable learning objectives.
3. Identify prerequisite knowledge and skills.
4. Map objectives to planned laboratory activities.
5. Decompose the proposed procedure into reviewable stages.
6. Identify equipment, materials, staffing, facility, and logistical requirements.
7. Build or update the hazard register.
8. Identify candidate controls and unresolved safety questions.
9. Review equipment safety and qualification requirements.
10. Review hazardous-material controls where applicable.
11. Review waste streams and disposal dependencies.
12. Review accessibility and accommodation interfaces.
13. Review supervision requirements and restricted activities.
14. Review emergency-response readiness.
15. Map learning objectives to assessment evidence.
16. Apply fail-closed governance gates.
17. Escalate unresolved issues to qualified local humans.
18. Require qualified-human approval before planning-package release.
19. Keep all physical execution and binding institutional authority outside the system.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both planning quality and governance behavior.

Useful dimensions include:

- objective clarity
- procedure coherence
- hazard detection
- missing-control detection
- equipment-safety handling
- hazardous-material boundary enforcement
- waste-planning completeness
- accessibility enforcement
- supervision enforcement
- emergency-response awareness
- protected-action enforcement
- qualified-human approval enforcement

Held-out scenarios should include plausible-looking plans with hidden hazards or missing operational controls so that a system cannot pass simply by producing polished documentation.

## Failure states

Useful explicit states include:

```text
LEARNING OBJECTIVES INCOMPLETE
PREREQUISITE GAP
PROCEDURE VALIDATION GAP
UNRESOLVED HAZARD
EQUIPMENT SAFETY GAP
HAZARDOUS MATERIAL CONTROL GAP
WASTE DISPOSAL GAP
ACCESSIBILITY GAP
SUPERVISION GAP
EMERGENCY RESPONSE GAP
RESOURCE AVAILABILITY GAP
ASSESSMENT ALIGNMENT GAP
HUMAN APPROVAL REQUIRED
LAB EXECUTION AUTHORITY PROHIBITED
EQUIPMENT ACTIVATION PROHIBITED
HAZARDOUS MATERIAL AUTHORITY PROHIBITED
SAFETY OVERRIDE PROHIBITED
UNSUPERVISED ACTIVITY PROHIBITED
```

The system should never fabricate inspection records, calibration, training completion, local approvals, hazard clearance, material authorization, emergency readiness, student competency, or human review.

## Observability

The `observability/` layer supports traceable planning execution.

Useful telemetry includes:

- objectives reviewed
- procedure stages
- hazards identified
- controls proposed
- equipment requirements
- materials requirements
- waste requirements
- accessibility findings
- supervision findings
- emergency-response findings
- assessment mappings
- governance blockers
- human-review state

Observability supports debugging, review, and reproducibility. It does not create laboratory authority.

## Memory and state

The `memory/` and `state/` layers can preserve planning context across a multi-step workflow.

Useful state can include:

- laboratory version
- objective version
- procedure version
- hazard register version
- resource state
- unresolved blockers
- reviewer state
- approval state

Sensitive student information should not be retained unless it is necessary and permitted for the educational purpose.

## Change management

Laboratory plans should be reviewed when material conditions change.

Examples include:

- new equipment
- substituted materials
- changed concentrations or quantities
- changed procedure steps
- changed student population
- changed facility
- changed supervision model
- changed emergency systems
- new hazard information

A previously reviewed plan should not automatically be treated as current after material changes.

## Versioning

A reproducible planning package should identify versions of key artifacts such as:

```text
learning objectives
procedure
hazard register
equipment list
materials list
waste plan
assessment map
safety review
human approval state
```

Versioning helps distinguish the approved planning state from later drafts.

## Evidence provenance

Safety-sensitive claims should retain provenance when practical.

Relevant sources can include:

- manufacturer documentation
- institutional policy
- locally approved procedures
- authoritative safety data
- training requirements
- facility documentation
- qualified expert review

The system should not fabricate citations or claim that a source supports a requirement it has not verified.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## Behavioral governance tests

The direct governance suite verifies that:

- a fully reviewed planning context can release a planning package
- missing qualified-human approval fails closed
- physical laboratory execution is never authorized
- unresolved hazards block release
- equipment-safety gaps block release
- hazardous-material-control gaps block release
- accessibility gaps block release
- supervision gaps block release

These tests validate governance behavior rather than claiming that an automated test can certify real-world laboratory safety.

## Reproducibility

For a planning package intended to be reviewed or reproduced, version at minimum:

- learning objectives
- laboratory context
- procedure
- equipment requirements
- material requirements
- hazard register
- waste plan
- accessibility review
- supervision review
- emergency-response considerations
- assessment mapping
- unresolved blockers
- approval state

Reproducibility does not remove the need for current local validation before physical execution.

## L3 Gold Standard

F95 follows the library's L3 Gold Standard structure through five specialist agents, deterministic planning tools, explicit orchestration and state, fail-closed safety governance, protected-action boundaries, observability, held-out governance evaluation, CI, and qualified-human approval.

This maturity designation describes the engineering and governance structure of the repository. It is not evidence that any particular laboratory procedure is safe, institutionally approved, regulator-approved, suitable for unsupervised use, or authorized for physical execution.

## Extending F95

Common extensions include:

- learning-management systems
- equipment inventories
- approved procedure libraries
- training records
- institutional safety systems
- accessibility tooling
- scheduling systems
- resource dashboards
- incident-learning systems
- laboratory analytics

New integrations should preserve least privilege, local safety authority, provenance, protected-action boundaries, accessibility, supervision requirements, and qualified-human approval.

## Example applications

F95 can serve as a reference architecture for planning:

- introductory science laboratories
- engineering teaching laboratories
- electronics laboratories
- instrumentation exercises
- materials laboratories
- computer-integrated physical labs
- makerspace education
- university practical courses
- technical training labs
- interdisciplinary STEM activities

Each implementation must be adapted to the discipline, learner level, local facility, equipment, materials, safety rules, and supervision environment.

## Design principles

1. Start from explicit educational objectives.
2. Separate planning from physical execution authority.
3. Treat procedure validation as a qualified human responsibility.
4. Surface hazards rather than assuming generated procedures are safe.
5. Treat equipment activation and hazardous-material use as protected actions.
6. Plan supervision, waste, accessibility, and emergency response explicitly.
7. Preserve evidence provenance and versioning.
8. Fail closed when required review evidence is missing.
9. Escalate unresolved safety or institutional questions to qualified humans.
10. Keep real-world laboratory authority with authorized people and institutions.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F95 as a laboratory-planning and governance reference architecture. Validate all procedures, hazards, equipment, materials, waste requirements, accessibility needs, supervision, emergency readiness, and institutional constraints with qualified local humans before any physical laboratory activity.

A planning package released by F95 is a structured recommendation artifact. It is not authorization to conduct laboratory work.