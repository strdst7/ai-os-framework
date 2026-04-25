from src.agents.monitoring_agent import MonitoringAgent
from src.agents.stability_agent import StabilityAgent
from src.agents.governance_agent import GovernanceAgent
from src.agents.response_agent import ResponseAgent
from src.agents.oversight_agent import OversightAgent

def run_system():
    telemetry = {
        "ahi": 0.72,
        "ihi": 0.69,
        "dhi": 0.66
    }

    monitor = MonitoringAgent()
    stability = StabilityAgent()
    governance = GovernanceAgent()
    response = ResponseAgent()
    oversight = OversightAgent()

    monitor.run(telemetry)

    score = stability.run(
        telemetry["ahi"],
        telemetry["ihi"],
        telemetry["dhi"]
    )["adsi"]

    tier = governance.run(score)["tier"]
    action = response.run(tier)["action"]
    approval = oversight.run(tier)["approval_required"]

    return {
        "score": score,
        "tier": tier,
        "action": action,
        "approval_required": approval
    }

if __name__ == "__main__":
    print(run_system())
