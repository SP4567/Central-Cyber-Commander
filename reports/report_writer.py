# reports/report_writer.py

import json
import os
from datetime import datetime

REPORT_DIR = "reports"

def save_report(event, analysis, severity, actions):
    """
    Saves a structured incident report to disk.
    """

    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"incident_{timestamp}.json"
    path = os.path.join(REPORT_DIR, filename)

    report = {
        "timestamp": timestamp,
        "event": event,
        "analysis": analysis,
        "severity": severity,
        "recommended_actions": actions
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    return path
