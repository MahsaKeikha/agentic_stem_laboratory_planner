from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "learning_objectives": ["plan a safe instructional laboratory activity"],
    "lab_context": "instructional planning only",
    "learning_objectives_reviewed": True,
    "procedure_reviewed": True,
    "hazard_reviewed": True,
    "equipment_reviewed": True,
    "materials_reviewed": True,
    "waste_disposal_reviewed": True,
    "accessibility_reviewed": True,
    "supervision_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
