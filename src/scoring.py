def compute_adsi(ahi, ihi, dhi):
    score = (ahi + ihi + dhi) / 3
    score = max(0.0, min(score, 1.0))
    return round(score, 3)