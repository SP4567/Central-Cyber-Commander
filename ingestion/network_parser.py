# ingestion/network_parser.py

import re

IP_REGEX = r"(?:\d{1,3}\.){3}\d{1,3}"

def parse_network_log(line: str) -> dict:
    """
    Parses network-related log entries and extracts
    IPs, ports, protocol, and threat hints.
    """

    event = {
        "event": "NETWORK_ACTIVITY",
        "src_ip": None,
        "dst_ip": None,
        "protocol": None,
        "severity_hint": "low",
        "raw": line
    }

    # Extract IPs
    ips = re.findall(IP_REGEX, line)
    if len(ips) >= 2:
        event["src_ip"] = ips[0]
        event["dst_ip"] = ips[1]

    # Detect protocol
    if "tcp" in line.lower():
        event["protocol"] = "TCP"
    elif "udp" in line.lower():
        event["protocol"] = "UDP"
    elif "icmp" in line.lower():
        event["protocol"] = "ICMP"

    # Threat heuristics
    lowered = line.lower()
    if any(x in lowered for x in ["port scan", "nmap", "syn flood"]):
        event["event"] = "PORT_SCAN"
        event["severity_hint"] = "medium"

    if any(x in lowered for x in ["ddos", "flood", "amplification"]):
        event["event"] = "DDOS_ATTACK"
        event["severity_hint"] = "high"

    if any(x in lowered for x in ["tor exit", "known bad ip", "c2"]):
        event["event"] = "SUSPICIOUS_IP"
        event["severity_hint"] = "high"

    return event
