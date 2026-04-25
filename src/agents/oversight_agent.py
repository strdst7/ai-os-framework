class OversightAgent:
    name = "Human Oversight Agent"

    def run(self, tier):
        return {
            "approval_required": tier == "Critical"
        }
