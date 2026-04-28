def detect_bruteforce(logs, threshold=5):
    """
    Detect multiple failed login attempts from same IP
    """
    failed_attempts = {}
    alerts = []

    for line in logs:
        if "Failed password" in line:
            try:
                ip = line.split("from ")[1].split(" ")[0]
            except IndexError:
                continue

            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            if failed_attempts[ip] == threshold:
                alerts.append({
                    "type": "Brute Force",
                    "ip": ip,
                    "message": f"Brute force suspected from {ip}"
                })

    return alerts


def detect_suspicious_login(logs):
    """
    Detect logins from external IPs (only one alert per IP)
    """
    alerts = []
    seen_ips = set()  # keeps track of already alerted IPs

    for line in logs:
        if "Accepted password" in line:
            try:
                ip = line.split("from ")[1].split(" ")[0]
            except IndexError:
                continue

            # Only alert once per external IP
            if not ip.startswith("192.168") and ip not in seen_ips:
                alerts.append({
                    "type": "Suspicious Login",
                    "ip": ip,
                    "message": f"Login from external IP {ip}"
                })
                seen_ips.add(ip)

    return alerts


def detect_root_login(logs):
    """
    Detect root account login (high risk)
    """
    alerts = []

    for line in logs:
        if "Accepted password for root" in line:
            try:
                ip = line.split("from ")[1].split(" ")[0]
            except IndexError:
                continue

            alerts.append({
                "type": "Root Login",
                "ip": ip,
                "message": f"Root login detected from {ip}"
            })

    return alerts