from src.tools import send_alert, rollback_model

def response_agent(state):
    if state.tier == "Critical":
        state.action = rollback_model()

    elif state.tier == "Degrading":
        state.action = send_alert("Investigate degradation")

    else:
        state.action = "Continue"

    return state
