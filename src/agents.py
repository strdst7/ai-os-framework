class MonitoringAgent:
    def observe(self, telemetry):
        return telemetry

class StabilityAgent:
    def evaluate(self, ahi, ihi, dhi):
        return round((ahi + ihi + dhi) / 3, 3)

class GovernanceAgent:
    def decide(self, score):
        if score >= 0.85:
            return "Stable"
        elif score >= 0.75:
            return "Warning"
        elif score >= 0.65:
            return "Degrading"
        return "Critical"
