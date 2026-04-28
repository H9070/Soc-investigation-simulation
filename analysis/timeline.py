def build_timeline(logs, alerts):
    """
    Build chronological sequence of events from logs + alerts
    """

    timeline = []

    step = 1  # sequence counter

    # Step 1: Process raw logs
    for line in logs:
        line = line.strip()

        if "Failed password" in line:
            try:
                ip = line.split("from ")[1].split(" ")[0]
                timeline.append(f"[{step}] Failed login attempt from {ip}")
                step += 1
            except IndexError:
                continue

        elif "Accepted password" in line:
            try:
                ip = line.split("from ")[1].split(" ")[0]
                timeline.append(f"[{step}] Successful login from {ip}")
                step += 1
            except IndexError:
                continue

    # Step 2: Add alerts at the end (summary style)
    for alert in alerts:
        timeline.append(f"[{step}] ALERT TRIGGERED: {alert['type']} from {alert['ip']}")
        step += 1

    return timeline