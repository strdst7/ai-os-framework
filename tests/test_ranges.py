from src.scoring import compute_adsi

def test_bounds():
    score = compute_adsi(1,1,1)
    assert score == 1
