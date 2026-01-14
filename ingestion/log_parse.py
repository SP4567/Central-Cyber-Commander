import re

def parse_log(line):
    if "failed password" in line.lower():
        return {
            "event": "AUTH_FAILURE",
            "severity_hint": "medium",
            "raw": line
        }

    if "malware" in line.lower():
        return {
            "event": "MALWARE_DETECTED",
            "severity_hint": "high",
            "raw": line
        }

    return {
        "event": "INFO",
        "severity_hint": "low",
        "raw": line
    }
