def validate_action(action, safe_mode=True):
    if safe_mode and action in ["Delete files", "Shutdown system"]:
        return False
    return True
