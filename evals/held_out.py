from orchestration.orchestrator import orchestrate


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "unresolved_hazard": True}, False),
    ({**base(), "procedure_validation_gap": True}, False),
    ({**base(), "equipment_safety_gap": True}, False),
    ({**base(), "hazardous_material_control_gap": True}, False),
    ({**base(), "waste_disposal_gap": True}, False),
    ({**base(), "accessibility_gap": True}, False),
    ({**base(), "supervision_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
