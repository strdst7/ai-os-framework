from src.tiers import classify_tier

def test_tier():
    assert classify_tier(0.9) == "Stable"