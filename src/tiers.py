def classify_tier(score: float) -> str:
    if score >= 0.85:
        return "Stable"
    elif score >= 0.75:
        return "Warning"
    elif score >= 0.65:
        return "Degrading"
    return "Critical"
