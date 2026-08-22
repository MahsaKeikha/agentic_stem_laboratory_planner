from AGENTS.lab_objective_agent import run as objective
from AGENTS.learning_assessment_agent import run as assessment
from AGENTS.procedure_planner_agent import run as procedure
from AGENTS.resource_planner_agent import run as resources
from AGENTS.safety_reviewer_agent import run as safety
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run planning specialists and apply fail-closed laboratory governance."""
    results = [
        objective(context),
        procedure(context),
        safety(context),
        resources(context),
        assessment(context),
    ]
    governance = authorize("planning_release", context)
    return {
        "system": "F95",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "physical_lab_execution": False,
        "equipment_activation": False,
        "hazardous_material_authority": False,
    }
