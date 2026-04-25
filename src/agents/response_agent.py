class ResponseAgent:
    name = "Response Agent"

    def run(self, tier):
        actions = {
            "Stable": "Continue operations",
            "Warning": "Increase monitoring",
            "Degrading": "Investigate immediately",
            "Critical": "Escalate and mitigate"
        }

        return {
            "action": actions.get(tier, "Unknown")
        }
