from src.scoring import compute_adsi

def test_score():
    assert compute_adsi(0.9,0.8,0.7) == 0.8