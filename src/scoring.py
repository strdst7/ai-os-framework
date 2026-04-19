def compute_adsi(ahi: float, ihi: float, dhi: float) -> float:
    score = (ahi + ihi + dhi) / 3
    score = max(0.0, min(score, 1.0))
    return round(score, 3)
