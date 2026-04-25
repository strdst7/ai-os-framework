class OversightAgent:
    name = "Human Oversight Agent"

    def run(self, tier):
        if tier == "Critical":
            return {"approval_required": True}

        return {"approval_required": False}
