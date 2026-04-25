class StabilityAgent:
    name = "Stability Agent"

    def run(self, ahi, ihi, dhi):
        score = round((ahi + ihi + dhi) / 3, 3)
        return {
            "adsi": score
        }
