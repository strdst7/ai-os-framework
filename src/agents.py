from src.scoring import compute_adsi
from src.tiers import classify_tier

class MonitoringAgent:
    def observe(self, telemetry):
        return telemetry

class StabilityAgent:
    def evaluate(self, ahi, ihi, dhi):
        return compute_adsi(ahi, ihi, dhi)

class GovernanceAgent:
    def decide(self, score):
        return classify_tier(score)
