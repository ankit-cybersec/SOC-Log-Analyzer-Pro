SOC Log Analyzer Pro

Overview

SOC Log Analyzer Pro is a Python-based Security Operations Center (SOC) project that analyzes authentication logs, detects suspicious login activity, identifies brute force attacks, and generates multiple security reports.

Features

* Failed Login Detection
* Suspicious IP Identification
* Severity Classification (LOW / MEDIUM / HIGH)
* Brute Force Detection
* SOC Dashboard Summary
* Top Attacker Detection
* Top 3 Attackers Ranking
* CSV Report Generation
* JSON Report Generation
* HTML Report Generation

Technologies Used

* Python
* CSV
* JSON
* HTML
* File Handling

Reports Generated

* incident_report.csv
* incident_report.json
* incident_report.html

Sample Output

[ALERT] BRUTE FORCE DETECTED -> 172.16.0.9

========== SOC DASHBOARD ==========

Total Failed Login Events : 8

High Risk IPs : 1
Medium Risk IPs : 1
Low Risk IPs : 1

––––– TOP ATTACKER –––––

IP Address : 172.16.0.9

Failed Attempts : 5

TOP ATTACKERS RANKING

1. 172.16.0.9 –> 5 Attempts

==================================

SOC Analysis Complete

Author

Ankit Shivhare
