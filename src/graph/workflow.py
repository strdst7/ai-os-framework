from src.graph.state import SystemState
from src.agents.monitoring import monitoring_agent
from src.agents.stability import stability_agent
from src.agents.governance import governance_agent
from src.agents.response import response_agent

def run_graph():
    state = SystemState(
        ahi=0.71,
        ihi=0.68,
        dhi=0.64
    )

    state = monitoring_agent(state)
    state = stability_agent(state)
    state = governance_agent(state)
    state = response_agent(state)

    return state
