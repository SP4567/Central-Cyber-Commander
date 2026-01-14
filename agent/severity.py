def calculate_severity(event, llm_response):
    score = 0

    if "ransomware" in llm_response.lower():
        score += 80
    if "phishing" in llm_response.lower():
        score += 40
    if "critical" in llm_response.lower():
        score += 90

    return min(score, 100)
