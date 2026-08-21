from AGENTS.lab_objective_agent import run as a
from AGENTS.procedure_planner_agent import run as b
from AGENTS.safety_reviewer_agent import run as c
from AGENTS.resource_planner_agent import run as d
from AGENTS.learning_assessment_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
