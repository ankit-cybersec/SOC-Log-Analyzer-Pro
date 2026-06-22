SOC Log Analyzer Pro

Overview

SOC Log Analyzer Pro is a Python-based Security Operations Center (SOC) project designed to analyze security logs, detect suspicious login activities, classify threat levels, store attack records in a SQLite database, generate reports, and visualize attack statistics.

This project simulates real-world SOC analyst workflows including log analysis, threat detection, incident reporting, database management, and attack visualization.

⸻

Features

* Real-Time Log Monitoring
* Failed Login Detection
* Risk Classification (High, Medium, Low)
* SQLite Database Integration
* IP Search Functionality
* CSV Report Generation
* PDF Report Generation
* Email Alert Notification
* Risk Distribution Pie Chart
* Top Attackers Bar Chart
* GUI Interface using Tkinter

⸻

Technologies Used

* Python 3
* Tkinter
* SQLite3
* Matplotlib
* ReportLab
* SMTP Email Alerts

⸻

Project Structure

SOC_Log_Analyzer_Pro/
│
├── logs/
│   ├── sample.log
│   └── ssh_test.log
│
├── reports/
│   ├── incident_report.csv
│   ├── incident_report.html
│   ├── incident_report.json
│   └── incident_report.txt
│
├── screenshots/
│   ├── dashboard.png
│   ├── database.png
│   ├── pie_chart.png
│   └── bar_chart.png
│
├── analyzer.py
├── gui.py
├── soc_attacks.db
├── requirements.txt
└── README.md

⸻

Risk Classification Logic

Failed Attempts	       Risk Level
1-2	                    Low
3-5	                    Medium
6+	                    High

⸻

Database Storage

Detected attacks are stored in SQLite database:

Table: attacks

Columns:

* id
* ip
* attempts
* risk

Example:

IP Address	     Attempts	         Risk
192.168.1.10	   7	             HIGH
172.16.0.55        3	             MEDIUM
203.0.113.50	   1	             LOW

⸻

Screenshots

Dashboard

Database Records

Risk Distribution Chart

Top Attackers

⸻

How To Run

Install dependencies:

pip install -r requirements.txt

Run:

python gui.py

⸻

Future Improvements

* SIEM Integration
* GeoIP Mapping
* Threat Intelligence Feed
* Splunk Integration
* ELK Stack Integration
* Real-Time Dashboard Analytics


Screenshots

Main Dashboard

⸻

Database View

⸻

Risk Distribution Chart

⸻

Top Attackers Chart

⸻

PDF Report Generation

⸻

Author

Ankit Shivhare

BCA Graduate | SOC Analyst Aspirant | Cyber Security Enthusiast