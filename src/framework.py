from src.agents import MonitoringAgent, StabilityAgent, GovernanceAgent

def evaluate(ahi, ihi, dhi):
    monitor = MonitoringAgent()
    stability = StabilityAgent()
    governance = GovernanceAgent()

    telemetry = monitor.observe({
        "ahi": ahi,
        "ihi": ihi,
        "dhi": dhi
    })

    score = stability.evaluate(
        telemetry["ahi"],
        telemetry["ihi"],
        telemetry["dhi"]
    )

    tier = governance.decide(score)

    return {
        "score": score,
        "tier": tier
    }
