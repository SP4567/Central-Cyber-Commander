def suggest_actions(severity):
    if severity > 85:
        return ["Isolate system", "Block IP", "Alert admin"]
    elif severity > 60:
        return ["Monitor closely", "Enable firewall rules"]
    else:
        return ["Log event", "No action needed"]