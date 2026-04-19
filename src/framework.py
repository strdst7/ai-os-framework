from src.scoring import compute_adsi
from src.tiers import classify_tier

def evaluate(ahi, ihi, dhi):
    score = compute_adsi(ahi, ihi, dhi)
    tier = classify_tier(score)

    return {
        "score": score,
        "tier": tier
    }