from src.agents import GovernanceAgent

def test_agent():
    g = GovernanceAgent()
    assert g.decide(0.6) == "Critical"
