import os
import random

# Get absolute path of current file (generator.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute path to auth.log
LOG_FILE = os.path.join(BASE_DIR, "auth.log")

ips = [
    "192.168.1.10",  # attacker
    "192.168.1.5",   # normal user
    "203.0.113.50"   # suspicious external
]

users = ["root", "admin", "user1"]

def generate_logs():
    logs = []

    for _ in range(50):
        ip = random.choice(ips)
        user = random.choice(users)

        # Attacker behavior (mostly failures)
        if ip == "192.168.1.10":
            logs.append(f"Failed password for {user} from {ip} port 22")

        else:
            if random.random() > 0.5:
                logs.append(f"Accepted password for {user} from {ip}")
            else:
                logs.append(f"Failed password for {user} from {ip}")

    return logs


def write_logs():
    logs = generate_logs()

    with open(LOG_FILE, "w") as f:
        for line in logs:
            f.write(line + "\n")

    print(f"[+] Logs written to: {LOG_FILE}")


if __name__ == "__main__":
    write_logs()