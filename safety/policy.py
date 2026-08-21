def review_required(action: str) -> bool:
    protected = {"lab_execution", "hazardous_material_use", "equipment_activation", "external_submission"}
    return action in protected

def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
