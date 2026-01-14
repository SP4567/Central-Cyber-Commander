# ingestion/normalizer.py

def normalize_event(event: dict) -> dict:
    """
    Normalizes different event types into a common schema
    that the Cyber Commander LLM can reason over.
    """

    normalized = {
        "type": event.get("event", "UNKNOWN"),
        "severity_hint": event.get("severity_hint", "low"),
        "source_ip": event.get("src_ip"),
        "destination_ip": event.get("dst_ip"),
        "protocol": event.get("protocol"),
        "details": event.get("raw", ""),
    }

    # Add flags for LLM reasoning
    flags = []

    if normalized["severity_hint"] == "high":
        flags.append("HIGH_RISK")

    if normalized["source_ip"] and normalized["destination_ip"]:
        flags.append("NETWORK_BASED")

    if "malware" in normalized["details"].lower():
        flags.append("MALWARE_INDICATOR")

    if "auth" in normalized["details"].lower():
        flags.append("AUTH_RELATED")

    normalized["flags"] = flags

    return normalized
