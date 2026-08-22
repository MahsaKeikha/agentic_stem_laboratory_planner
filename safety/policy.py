"""Fail-closed planning-only governance for F95 STEM laboratory planning."""

PROTECTED_ACTIONS = {
    "lab_execution",
    "hazardous_material_use",
    "equipment_activation",
    "external_submission",
    "override_safety_rule",
    "unsupervised_student_activity",
}

REQUIRED_REVIEWS = (
    "learning_objectives_reviewed",
    "procedure_reviewed",
    "hazard_reviewed",
    "equipment_reviewed",
    "materials_reviewed",
    "waste_disposal_reviewed",
    "accessibility_reviewed",
    "supervision_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "physical or binding laboratory authority is outside planner scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required laboratory review", "missing": missing}

    blockers = []
    if context.get("unresolved_hazard"):
        blockers.append("laboratory hazard unresolved")
    if context.get("procedure_validation_gap"):
        blockers.append("procedure validation incomplete")
    if context.get("equipment_safety_gap"):
        blockers.append("equipment safety review incomplete")
    if context.get("hazardous_material_control_gap"):
        blockers.append("hazardous-material controls inadequate")
    if context.get("waste_disposal_gap"):
        blockers.append("waste disposal controls incomplete")
    if context.get("accessibility_gap"):
        blockers.append("accessibility requirement unresolved")
    if context.get("supervision_gap"):
        blockers.append("qualified supervision requirement unresolved")
    if context.get("emergency_response_gap"):
        blockers.append("emergency response planning incomplete")

    if blockers:
        return {"allowed": False, "reason": "laboratory planning governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "planning package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
