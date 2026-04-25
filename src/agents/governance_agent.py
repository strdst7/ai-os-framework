def governance_agent(state):
    if state.score >= 0.85:
        state.tier = "Stable"
    elif state.score >= 0.75:
        state.tier = "Warning"
    elif state.score >= 0.65:
        state.tier = "Degrading"
    else:
        state.tier = "Critical"

    return state
