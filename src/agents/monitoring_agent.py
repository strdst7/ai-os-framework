class MonitoringAgent:
    name = "Monitoring Agent"

    def run(self, telemetry):
        return {
            "status": "observed",
            "telemetry": telemetry
        }
