def stability_agent(state):
    state.score = round(
        (state.ahi + state.ihi + state.dhi) / 3, 3
    )
    return state
