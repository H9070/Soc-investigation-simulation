import os
from detection.rules import (
    detect_bruteforce,
    detect_suspicious_login,
    detect_root_login
)
from analysis.investigator import investigate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logs", "auth.log")
REPORT_FILE = os.path.join(BASE_DIR, "reports", "report.txt")


def read_logs(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def write_report(report_lines):
    with open(REPORT_FILE, "w") as f:
        for line in report_lines:
            f.write(line + "\n")


def main():
    logs = read_logs(LOG_FILE)

    # Run all detection rules
    alerts = []
    alerts.extend(detect_bruteforce(logs))
    alerts.extend(detect_suspicious_login(logs))
    alerts.extend(detect_root_login(logs))

    report_output = []

    print("\n--- SOC REPORT ---")

    if alerts:
        for alert in alerts:
            result = investigate(alert)

            report_output.append(f"ALERT: {alert['message']}")
            report_output.append(f"TYPE: {alert['type']}")
            report_output.append(f"IP: {alert['ip']}")
            report_output.append(f"VERDICT: {result['verdict']}")
            report_output.append(f"SEVERITY: {result['severity']}")
            report_output.append(f"REASON: {result['reason']}")
            report_output.append("-" * 50)

            print(f"\nALERT: {alert['message']}")
            print(f"TYPE: {alert['type']}")
            print(f"IP: {alert['ip']}")
            print(f"VERDICT: {result['verdict']}")
            print(f"SEVERITY: {result['severity']}")
            print(f"REASON: {result['reason']}")

    else:
        msg = "No suspicious activity detected."
        print(msg)
        report_output.append(msg)

    write_report(report_output)

    print(f"\n[+] Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()