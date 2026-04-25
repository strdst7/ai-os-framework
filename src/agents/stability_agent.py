class StabilityAgent:
    name = "Stability Agent"

    def run(self, ahi, ihi, dhi):
        return {
            "adsi": round((ahi + ihi + dhi) / 3, 3)
        }
