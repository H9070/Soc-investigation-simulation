def investigate(alert):
    """
    Analyze alert and assign severity + verdict
    """

    alert_type = alert["type"]

    if alert_type == "Brute Force":
        return {
            "verdict": "Malicious",
            "severity": "High",
            "reason": "Multiple failed login attempts detected"
        }

    elif alert_type == "Suspicious Login":
        return {
            "verdict": "Suspicious",
            "severity": "Medium",
            "reason": "Login from external/untrusted IP"
        }

    elif alert_type == "Root Login":
        return {
            "verdict": "Critical",
            "severity": "High",
            "reason": "Root account access detected"
        }

    return {
        "verdict": "Unknown",
        "severity": "Low",
        "reason": "No rule matched"
    }