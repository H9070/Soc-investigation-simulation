# End-to-End SOC Investigation Simulation

## 📌 Overview
This project simulates a Security Operations Center (SOC) workflow:
- Log ingestion
- Threat detection
- Investigation & classification
- Threat intelligence enrichment
- Timeline reconstruction
- Report generation

## ⚙️ Features
- Brute force attack detection
- Suspicious login detection (external IP)
- Root login alerting
- Threat intelligence (simulated)
- Attack timeline generation
- Structured SOC report output

## 🧠 Detection Logic
- Multiple failed logins from same IP → Brute force
- External IP login → Suspicious
- Root login → High risk

## 🔍 Investigation
Each alert is analyzed and assigned:
- Verdict (Malicious / Suspicious / Unknown)
- Severity (High / Medium / Low)
- Reason

## 🌐 Threat Intelligence
Simulated IP reputation:
- Malicious
- Internal
- External

## 🕒 Timeline Reconstruction
Builds a sequence of events to understand attack flow.

## ▶️ How to Run

```bash
cd soc_simulation
python logs/generator.py
python main.py

## 🎯 Outcomes
- Detects brute force attacks, suspicious logins, and root access events from system logs  
- Classifies alerts with severity levels and clear reasoning  
- Enriches alerts with IP-based threat intelligence (internal, external, malicious)  
- Reconstructs a timeline of events to understand attack flow  
- Generates structured SOC reports for analysis and documentation  

## 🚀 Future Improvements
- Integrate real threat intelligence APIs (e.g., VirusTotal)  
- Add timestamps and real-time log processing  
- Implement alert prioritization and scoring system  
- Extend detection rules for additional attack types  
