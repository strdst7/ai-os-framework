from src.orchestrator import run_system

def test_system():
    result = run_system()
    assert "tier" in result
