from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
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


def test_complete_review_can_release_planning_package():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["physical_lab_execution"] is False
    assert result["equipment_activation"] is False
    assert result["hazardous_material_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_lab_execution_is_never_authorized():
    assert authorize("lab_execution", valid_context())["allowed"] is False


def test_unresolved_hazard_blocks_release():
    context = valid_context()
    context["unresolved_hazard"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_equipment_safety_gap_blocks_release():
    context = valid_context()
    context["equipment_safety_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_hazardous_material_control_gap_blocks_release():
    context = valid_context()
    context["hazardous_material_control_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_accessibility_gap_blocks_release():
    context = valid_context()
    context["accessibility_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_supervision_gap_blocks_release():
    context = valid_context()
    context["supervision_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
