def check_ip_reputation(ip):
    """
    Simulated threat intelligence lookup
    In real SOC → this comes from APIs like VirusTotal
    """

    # Known bad IPs (simulated threat feed)
    malicious_ips = ["192.168.1.10"]

    # Known internal network
    internal_prefix = "192.168"

    # Check if IP is malicious
    if ip in malicious_ips:
        return {
            "reputation": "Malicious",
            "location": "Unknown",
            "confidence": "High"
        }

    # Check if IP is internal
    elif ip.startswith(internal_prefix):
        return {
            "reputation": "Internal",
            "location": "Local Network",
            "confidence": "Trusted"
        }

    # Otherwise treat as external
    else:
        return {
            "reputation": "Unknown",
            "location": "External Network",
            "confidence": "Medium"
        }