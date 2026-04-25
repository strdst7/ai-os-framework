class GovernanceAgent:
    name = "Governance Agent"

    def run(self, score):
        if score >= 0.85:
            tier = "Stable"
        elif score >= 0.75:
            tier = "Warning"
        elif score >= 0.65:
            tier = "Degrading"
        else:
            tier = "Critical"

        return {"tier": tier}
