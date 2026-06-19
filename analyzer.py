# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# print(logs)

# log_file.close()


# version --- 2

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# for line in logs:
#     print(line)

# log_file.close()


# version ---3


# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# for line in logs:

#     if "Failed login" in line:
#         print("ALERT:", line)

# log_file.close()



# version ---4


# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         print("Suspicious IP:", ip)

# log_file.close()



# veersion ---5

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# print(ip_count)

# log_file.close()



# version --- 6 


# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# print("IP Statistics")
# print(ip_count)

# most_attacker = max(ip_count, key=ip_count.get)

# print("\nMost Suspicious IP:", most_attacker)

# print("Failed Attempts:", ip_count[most_attacker])

# log_file.close()





# version 7 
# version ka goal  ab tool sirf screen par output nahi dikhayega ye automatically file bnayega


# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# most_attacker = max(ip_count, key=ip_count.get)

# attempts = ip_count[most_attacker]

# report = open("reports/incident_report.txt", "w")

# report.write("SOC INCIDENT REPORT\n")
# report.write("====================\n\n")

# report.write(f"Most Suspicious IP: {most_attacker}\n")
# report.write(f"Failed Attempts: {attempts}\n")

# report.close()

# print("Report Generated Successfully")
# print("Check reports/incident_report.txt")

# log_file.close()


# version ---8 


# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# most_attacker = max(ip_count, key=ip_count.get)

# attempts = ip_count[most_attacker]

# if attempts >= 3:
#     severity = "HIGH"

# elif attempts == 2:
#     severity = "MEDIUM"

# else:
#     severity = "LOW"

# report = open("reports/incident_report.txt", "w")

# report.write("SOC INCIDENT REPORT\n")
# report.write("====================\n\n")

# report.write(f"Most Suspicious IP: {most_attacker}\n")
# report.write(f"Failed Attempts: {attempts}\n")
# report.write(f"Severity: {severity}\n")

# report.close()

# print("Report Generated Successfully")
# print("Severity:", severity)

# log_file.close()



# version 9


# import csv

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# most_attacker = max(ip_count, key=ip_count.get)

# attempts = ip_count[most_attacker]

# if attempts >= 3:
#     severity = "HIGH"

# elif attempts == 2:
#     severity = "MEDIUM"

# else:
#     severity = "LOW"

# report = open("reports/incident_report.txt", "w")

# report.write("SOC INCIDENT REPORT\n")
# report.write("====================\n\n")

# report.write(f"Most Suspicious IP: {most_attacker}\n")
# report.write(f"Failed Attempts: {attempts}\n")
# report.write(f"Severity: {severity}\n")

# report.close()

# csv_file = open(
#     "reports/incident_report.csv",
#     "w",
#     newline=""
# )

# writer = csv.writer(csv_file)

# writer.writerow(
#     [
#         "Suspicious IP",
#         "Failed Attempts",
#         "Severity"
#     ]
# )

# writer.writerow(
#     [
#         most_attacker,
#         attempts,
#         severity
#     ]
# )

# csv_file.close()

# print("TXT Report Generated")
# print("CSV Report Generated")

# log_file.close()




#                                     version 10


# import csv

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:

#             ip_count[ip] += 1

#         else:

#             ip_count[ip] = 1

# csv_file = open(
#     "reports/incident_report.csv",
#     "w",
#     newline=""
# )

# writer = csv.writer(csv_file)

# writer.writerow(
#     [
#         "IP Address",
#         "Attempts",
#         "Severity"
#     ]
# )

# for ip, attempts in ip_count.items():

#     if attempts >= 5:
#         severity = "HIGH"

#     elif attempts >= 2:
#         severity = "MEDIUM"

#     else:
#         severity = "LOW"

#     writer.writerow(
#         [
#             ip,
#             attempts,
#             severity
#         ]
#     )

#     print(
#         ip,
#         attempts,
#         severity
#     )

# csv_file.close()

# log_file.close()

# print("\nSOC Analysis Complete")




#                           version  11 



# import csv
# import json

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:
#             ip_count[ip] += 1
#         else:
#             ip_count[ip] = 1

# csv_file = open(
#     "reports/incident_report.csv",
#     "w",
#     newline=""
# )

# writer = csv.writer(csv_file)

# writer.writerow(
#     [
#         "IP Address",
#         "Attempts",
#         "Severity"
#     ]
# )

# json_report = []

# for ip, attempts in ip_count.items():

#     if attempts >= 5:

#         severity = "HIGH"

#         print(
#             f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#         )

#     elif attempts >= 2:

#         severity = "MEDIUM"

#         print(
#             f"[WARNING] Suspicious Activity -> {ip}"
#         )

#     else:

#         severity = "LOW"

#         print(
#             f"[INFO] Low Risk -> {ip}"
#         )

#     writer.writerow(
#         [
#             ip,
#             attempts,
#             severity
#         ]
#     )

#     json_report.append(
#         {
#             "ip": ip,
#             "attempts": attempts,
#             "severity": severity
#         }
#     )

# csv_file.close()

# json_file = open(
#     "reports/incident_report.json",
#     "w"
# )

# json.dump(
#     json_report,
#     json_file,
#     indent=4
# )

# json_file.close()

# log_file.close()

# print("\nSOC Analysis Complete")



# version 12



# import csv
# import json

# log_file = open("logs/sample.log", "r")

# logs = log_file.readlines()

# ip_count = {}

# for line in logs:

#     if "Failed login" in line:

#         words = line.split()

#         ip = words[-1]

#         if ip in ip_count:
#             ip_count[ip] += 1
#         else:
#             ip_count[ip] = 1

# csv_file = open(
#     "reports/incident_report.csv",
#     "w",
#     newline=""
# )

# writer = csv.writer(csv_file)

# writer.writerow(
#     [
#         "IP Address",
#         "Attempts",
#         "Severity"
#     ]
# )

# json_report = []

# for ip, attempts in ip_count.items():

#     if attempts >= 5:

#         severity = "HIGH"

#         print(
#             f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#         )

#     elif attempts >= 2:

#         severity = "MEDIUM"

#         print(
#             f"[WARNING] Suspicious Activity -> {ip}"
#         )

#     else:

#         severity = "LOW"

#         print(
#             f"[INFO] Low Risk -> {ip}"
#         )

#     writer.writerow(
#         [
#             ip,
#             attempts,
#             severity
#         ]
#     )

#     json_report.append(
#         {
#             "ip": ip,
#             "attempts": attempts,
#             "severity": severity
#         }
#     )

# csv_file.close()

# json_file = open(
#     "reports/incident_report.json",
#     "w"
# )

# json.dump(
#     json_report,
#     json_file,
#     indent=4
# )

# json_file.close()

# log_file.close()

# print("\nSOC Analysis Complete")


# version 13

# import csv
# import json


# def determine_severity(attempts):

#     if attempts >= 5:
#         return "HIGH"

#     elif attempts >= 2:
#         return "MEDIUM"

#     else:
#         return "LOW"


# try:

#     log_file = open(
#         "logs/sample.log",
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     # Dashboard Counters
#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     csv_file = open(
#         "reports/incident_report.csv",
#         "w",
#         newline=""
#     )

#     writer = csv.writer(csv_file)

#     writer.writerow(
#         [
#             "IP Address",
#             "Attempts",
#             "Severity"
#         ]
#     )

#     json_report = []

#     for ip, attempts in ip_count.items():

#         severity = determine_severity(
#             attempts
#         )

#         # Dashboard Counting
#         if severity == "HIGH":

#             high_risk += 1

#             print(
#                 f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#             )

#         elif severity == "MEDIUM":

#             medium_risk += 1

#             print(
#                 f"[WARNING] Suspicious Activity -> {ip}"
#             )

#         else:

#             low_risk += 1

#             print(
#                 f"[INFO] Low Risk -> {ip}"
#             )

#         writer.writerow(
#             [
#                 ip,
#                 attempts,
#                 severity
#             ]
#         )

#         json_report.append(
#             {
#                 "ip": ip,
#                 "attempts": attempts,
#                 "severity": severity
#             }
#         )

#     csv_file.close()

#     json_file = open(
#         "reports/incident_report.json",
#         "w"
#     )

#     json.dump(
#         json_report,
#         json_file,
#         indent=4
#     )

#     json_file.close()

#     log_file.close()

#     print(
#         "\n========== SOC DASHBOARD =========="
#     )

#     print(
#         f"\nTotal Failed Login Events : {sum(ip_count.values())}"
#     )

#     print(
#         f"\nHigh Risk IPs : {high_risk}"
#     )

#     print(
#         f"Medium Risk IPs : {medium_risk}"
#     )

#     print(
#         f"Low Risk IPs : {low_risk}"
#     )

#     print(
#         "\n=================================="
#     )

#     print(
#         "\nSOC Analysis Complete"
#     )

# except FileNotFoundError:

#     print(
#         "ERROR: Log file not found"
#     )

# except Exception as error:

#     print(
#         f"Unexpected Error: {error}"
#     )


# version 14


# import csv
# import json


# def determine_severity(attempts):

#     if attempts >= 5:
#         return "HIGH"

#     elif attempts >= 2:
#         return "MEDIUM"

#     else:
#         return "LOW"


# try:

#     log_file = open(
#         "logs/sample.log",
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     # Dashboard Counters
#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     # Top Attacker Variables
#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     csv_file = open(
#         "reports/incident_report.csv",
#         "w",
#         newline=""
#     )

#     writer = csv.writer(csv_file)

#     writer.writerow(
#         [
#             "IP Address",
#             "Attempts",
#             "Severity"
#         ]
#     )

#     json_report = []

#     for ip, attempts in ip_count.items():

#         severity = determine_severity(
#             attempts
#         )

#         # Top Attacker Detection
#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         # Dashboard Counting
#         if severity == "HIGH":

#             high_risk += 1

#             print(
#                 f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#             )

#         elif severity == "MEDIUM":

#             medium_risk += 1

#             print(
#                 f"[WARNING] Suspicious Activity -> {ip}"
#             )

#         else:

#             low_risk += 1

#             print(
#                 f"[INFO] Low Risk -> {ip}"
#             )

#         writer.writerow(
#             [
#                 ip,
#                 attempts,
#                 severity
#             ]
#         )

#         json_report.append(
#             {
#                 "ip": ip,
#                 "attempts": attempts,
#                 "severity": severity
#             }
#         )

#     csv_file.close()

#     json_file = open(
#         "reports/incident_report.json",
#         "w"
#     )

#     json.dump(
#         json_report,
#         json_file,
#         indent=4
#     )

#     json_file.close()

#     log_file.close()

#     print(
#         "\n========== SOC DASHBOARD =========="
#     )

#     print(
#         f"\nTotal Failed Login Events : {sum(ip_count.values())}"
#     )

#     print(
#         f"\nHigh Risk IPs : {high_risk}"
#     )

#     print(
#         f"Medium Risk IPs : {medium_risk}"
#     )

#     print(
#         f"Low Risk IPs : {low_risk}"
#     )

#     print(
#         "\n---------- TOP ATTACKER ----------"
#     )

#     print(
#         f"\nIP Address : {top_attacker_ip}"
#     )

#     print(
#         f"\nFailed Attempts : {top_attacker_attempts}"
#     )

#     print(
#         "\n=================================="
#     )

#     print(
#         "\nSOC Analysis Complete"
#     )

# except FileNotFoundError:

#     print(
#         "ERROR: Log file not found"
#     )

# except Exception as error:

#     print(
#         f"Unexpected Error: {error}"
#     )


# version 15


# import csv
# import json


# def determine_severity(attempts):

#     if attempts >= 5:
#         return "HIGH"

#     elif attempts >= 2:
#         return "MEDIUM"

#     else:
#         return "LOW"


# try:

#     log_file = open(
#         "logs/sample.log",
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     # Dashboard Counters
#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     # Top Attacker Variables
#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     csv_file = open(
#         "reports/incident_report.csv",
#         "w",
#         newline=""
#     )

#     writer = csv.writer(csv_file)

#     writer.writerow(
#         [
#             "IP Address",
#             "Attempts",
#             "Severity"
#         ]
#     )

#     json_report = []
#     ranking_list = []

#     for ip, attempts in ip_count.items():

#         severity = determine_severity(
#             attempts
#         )

#         # Top Attacker Detection
#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         # Dashboard Counting
#         if severity == "HIGH":

#             high_risk += 1

#             print(
#                 f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#             )

#         elif severity == "MEDIUM":

#             medium_risk += 1

#             print(
#                 f"[WARNING] Suspicious Activity -> {ip}"
#             )

#         else:

#             low_risk += 1

#             print(
#                 f"[INFO] Low Risk -> {ip}"
#             )

#         writer.writerow(
#             [
#                 ip,
#                 attempts,
#                 severity
#             ]
#         )

#         json_report.append(
#             {
#                 "ip": ip,
#                 "attempts": attempts,
#                 "severity": severity
#             }
#         )

#         ranking_list.append(
#             (

#                 ip,
#                 attempts
#             )
#         )

#     csv_file.close()

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     json_file = open(
#         "reports/incident_report.json",
#         "w"
#     )

#     json.dump(
#         json_report,
#         json_file,
#         indent=4
#     )

#     json_file.close()

#     log_file.close()

#     print(
#         "\n========== SOC DASHBOARD =========="
#     )

#     print(
#         f"\nTotal Failed Login Events : {sum(ip_count.values())}"
#     )

#     print(
#         f"\nHigh Risk IPs : {high_risk}"
#     )

#     print(
#         f"Medium Risk IPs : {medium_risk}"
#     )

#     print(
#         f"Low Risk IPs : {low_risk}"
#     )

#     print(
#         "\n---------- TOP ATTACKER ----------"
#     )

#     print(
#         f"\nIP Address : {top_attacker_ip}"
#     )

#     print(
#         f"\nFailed Attempts : {top_attacker_attempts}"
#     )

#     print(
#     "\nTOP ATTACKERS RANKING"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         print(
#         f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1

#     print(
#         "\n=================================="
#     )

#     print(
#         "\nSOC Analysis Complete"
#     )

# except FileNotFoundError:

#     print(
#         "ERROR: Log file not found"
#     )

# except Exception as error:

#     print(
#         f"Unexpected Error: {error}"
#     )


    # version 16



    
# import csv
# import json


# def determine_severity(attempts):

#     if attempts >= 5:
#         return "HIGH"

#     elif attempts >= 2:
#         return "MEDIUM"

#     else:
#         return "LOW"


# try:

#     log_file = open(
#         "logs/sample.log",
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     # Dashboard Counters
#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     # Top Attacker Variables
#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     csv_file = open(
#         "reports/incident_report.csv",
#         "w",
#         newline=""
#     )

#     writer = csv.writer(csv_file)

#     writer.writerow(
#         [
#             "IP Address",
#             "Attempts",
#             "Severity"
#         ]
#     )

#     json_report = []

#     ranking_list = []

#     html_rows = ""

#     for ip, attempts in ip_count.items():

#         severity = determine_severity(
#             attempts
#         )

#         # Top Attacker Detection
#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         # Dashboard Counting
#         if severity == "HIGH":

#             high_risk += 1

#             print(
#                 f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#             )

#         elif severity == "MEDIUM":

#             medium_risk += 1

#             print(
#                 f"[WARNING] Suspicious Activity -> {ip}"
#             )

#         else:

#             low_risk += 1

#             print(
#                 f"[INFO] Low Risk -> {ip}"
#             )

#         writer.writerow(
#             [
#                 ip,
#                 attempts,
#                 severity
#             ]
#         )

#         json_report.append(
#             {
#                 "ip": ip,
#                 "attempts": attempts,
#                 "severity": severity
#             }
#         )

#         ranking_list.append(
#             (

#                 ip,
#                 attempts
#             )
#         )

#         html_rows += f"""
#         <tr>
#         <td>{ip}</td>
#         <td>{attempts}</td>
#         <td>{severity}</td>
#         </tr>
#         """

#     csv_file.close()

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     json_file = open(
#         "reports/incident_report.json",
#         "w"
#     )

#     json.dump(
#         json_report,
#         json_file,
#         indent=4
#     )

#     json_file.close()

#     html_file = open(
#         "reports/incident_report.html",
#         "w"
#     )

#     html_content = f"""
#     <html>

#     <head>
#     <title>SOC Incident Report</title>
#     </head>

#     <body>

#     <h1>SOC Incident Report</h1>

#     <table border="1">

#     <tr>
#     <th>IP Address</th>
#     <th>Attempts</th>
#     <th>Severity</th>
#     </tr>

#     {html_rows}

#     </table>

#     </body>

#     </html>
#     """

#     html_file.write(
#         html_content
#     )

#     html_file.close()

#     log_file.close()

#     print(
#         "\n========== SOC DASHBOARD =========="
#     )

#     print(
#         f"\nTotal Failed Login Events : {sum(ip_count.values())}"
#     )

#     print(
#         f"\nHigh Risk IPs : {high_risk}"
#     )

#     print(
#         f"Medium Risk IPs : {medium_risk}"
#     )

#     print(
#         f"Low Risk IPs : {low_risk}"
#     )

#     print(
#         "\n---------- TOP ATTACKER ----------"
#     )

#     print(
#         f"\nIP Address : {top_attacker_ip}"
#     )

#     print(
#         f"\nFailed Attempts : {top_attacker_attempts}"
#     )

#     print(
#     "\nTOP ATTACKERS RANKING"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         print(
#         f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1

#     print(
#         "\n=================================="
#     )

#     print(
#     "\nHTML Report Generated"
#     )

#     print(
#         "\nSOC Analysis Complete"
#     )

# except FileNotFoundError:

#     print(
#         "ERROR: Log file not found"
#     )

# except Exception as error:

#     print(
#         f"Unexpected Error: {error}"
#     )


    # version 17 for color output Terminal



# import csv
# import json

# from colorama import Fore
# from colorama import init

# init()

# def determine_severity(attempts):

#     if attempts >= 5:
#         return "HIGH"

#     elif attempts >= 2:
#         return "MEDIUM"

#     else:
#         return "LOW"


# try:

#     log_file = open(
#         "logs/sample.log",
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     # Dashboard Counters
#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     # Top Attacker Variables
#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     csv_file = open(
#         "reports/incident_report.csv",
#         "w",
#         newline=""
#     )

#     writer = csv.writer(csv_file)

#     writer.writerow(
#         [
#             "IP Address",
#             "Attempts",
#             "Severity"
#         ]
#     )

#     json_report = []

#     ranking_list = []

#     html_rows = ""

#     for ip, attempts in ip_count.items():

#         severity = determine_severity(
#             attempts
#         )

#         # Top Attacker Detection
#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         # Dashboard Counting
#         if severity == "HIGH":

#             high_risk += 1

#             print(
#                 Fore.RED +
#                 f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
#             )

#         elif severity == "MEDIUM":

#             medium_risk += 1

#             print(
#                 Fore.YELLOW +
#             f"[WARNING] Suspicious Activity -> {ip}"
#             )

#         else:

#             low_risk += 1

#             print(
#                 Fore.GREEN +
#                 f"[INFO] Low Risk -> {ip}"
#              )
#         writer.writerow(
#             [
#                 ip,
#                 attempts,
#                 severity
#             ]
#         )

#         json_report.append(
#             {
#                 "ip": ip,
#                 "attempts": attempts,
#                 "severity": severity
#             }
#         )

#         ranking_list.append(
#             (

#                 ip,
#                 attempts
#             )
#         )

#         html_rows += f"""
#         <tr>
#         <td>{ip}</td>
#         <td>{attempts}</td>
#         <td>{severity}</td>
#         </tr>
#         """

#     csv_file.close()

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     json_file = open(
#         "reports/incident_report.json",
#         "w"
#     )

#     json.dump(
#         json_report,
#         json_file,
#         indent=4
#     )

#     json_file.close()

#     html_file = open(
#         "reports/incident_report.html",
#         "w"
#     )

#     html_content = f"""
#     <html>

#     <head>
#     <title>SOC Incident Report</title>
#     </head>

#     <body>

#     <h1>SOC Incident Report</h1>

#     <table border="1">

#     <tr>
#     <th>IP Address</th>
#     <th>Attempts</th>
#     <th>Severity</th>
#     </tr>

#     {html_rows}

#     </table>

#     </body>

#     </html>
#     """

#     html_file.write(
#         html_content
#     )

#     html_file.close()

#     log_file.close()

#     print(
#         "\n========== SOC DASHBOARD =========="
#     )

#     print(
#         f"\nTotal Failed Login Events : {sum(ip_count.values())}"
#     )

#     print(
#         f"\nHigh Risk IPs : {high_risk}"
#     )

#     print(
#         f"Medium Risk IPs : {medium_risk}"
#     )

#     print(
#         f"Low Risk IPs : {low_risk}"
#     )

#     print(
#         "\n---------- TOP ATTACKER ----------"
#     )

#     print(
#         f"\nIP Address : {top_attacker_ip}"
#     )

#     print(
#         f"\nFailed Attempts : {top_attacker_attempts}"
#     )

#     print(
#     "\nTOP ATTACKERS RANKING"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         print(
#         f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1

#     print(
#         "\n=================================="
#     )

#     print(
#     "\nHTML Report Generated"
#     )

#     print(
#         "\nSOC Analysis Complete"
#     )

# except FileNotFoundError:

#     print(
#         "ERROR: Log file not found"
#     )

# except Exception as error:

#     print(
#         f"Unexpected Error: {error}"
#     )


# version 18 ///Add a time of loging ip attempts [Timestamp Analysis]


import csv
import json

from colorama import Fore
from colorama import init

init()

def determine_severity(attempts):

    if attempts >= 5:
        return "HIGH"

    elif attempts >= 2:
        return "MEDIUM"

    else:
        return "LOW"


try:

    log_file = open(
        "logs/sample.log",
        "r"
    )

    logs = log_file.readlines()

    ip_count = {}

    # Dashboard Counters
    high_risk = 0
    medium_risk = 0
    low_risk = 0

    first_event = ""
    last_event = ""

    # Top Attacker Variables
    top_attacker_ip = ""
    top_attacker_attempts = 0

    for line in logs:

        parts = line.split()

        if len(parts) < 2:
            print("Problem Line =", repr(line))
            continue

        timestamp = parts[0] + " " + parts[1]

        if "Failed login" in line:

            words = line.split()

            ip = words[-1]

            if first_event == "":
                first_event = timestamp

            last_event = timestamp

            if ip in ip_count:

                ip_count[ip] += 1

            else:

                ip_count[ip] = 1

    csv_file = open(
        "reports/incident_report.csv",
        "w",
        newline=""
    )

    writer = csv.writer(csv_file)

    writer.writerow(
        [
            "IP Address",
            "Attempts",
            "Severity"
        ]
    )

    json_report = []

    ranking_list = []

    html_rows = ""

    for ip, attempts in ip_count.items():

        severity = determine_severity(
            attempts
        )

        # Top Attacker Detection
        if attempts > top_attacker_attempts:

            top_attacker_attempts = attempts

            top_attacker_ip = ip

        # Dashboard Counting
        if severity == "HIGH":

            high_risk += 1

            print(
                Fore.RED +
                f"[ALERT] BRUTE FORCE DETECTED -> {ip}"
            )

        elif severity == "MEDIUM":

            medium_risk += 1

            print(
                Fore.YELLOW +
            f"[WARNING] Suspicious Activity -> {ip}"
            )

        else:

            low_risk += 1

            print(
                Fore.GREEN +
                f"[INFO] Low Risk -> {ip}"
             )
        writer.writerow(
            [
                ip,
                attempts,
                severity
            ]
        )

        json_report.append(
            {
                "ip": ip,
                "attempts": attempts,
                "severity": severity
            }
        )

        ranking_list.append(
            (

                ip,
                attempts
            )
        )

        html_rows += f"""
        <tr>
        <td>{ip}</td>
        <td>{attempts}</td>
        <td>{severity}</td>
        </tr>
        """

    csv_file.close()

    ranking_list.sort(
        key=lambda x: x[1],
        reverse=True
    )

    json_file = open(
        "reports/incident_report.json",
        "w"
    )

    json.dump(
        json_report,
        json_file,
        indent=4
    )

    json_file.close()

    html_file = open(
        "reports/incident_report.html",
        "w"
    )

    html_content = f"""
    <html>

    <head>
    <title>SOC Incident Report</title>
    </head>

    <body>

    <h1>SOC Incident Report</h1>

    <table border="1">

    <tr>
    <th>IP Address</th>
    <th>Attempts</th>
    <th>Severity</th>
    </tr>

    {html_rows}

    </table>

    </body>

    </html>
    """

    html_file.write(
        html_content
    )

    html_file.close()

    log_file.close()

    print(
        "\n========== SOC DASHBOARD =========="
    )

    print(
        f"\nTotal Failed Login Events : {sum(ip_count.values())}"
    )

    print(
        f"\nHigh Risk IPs : {high_risk}"
    )

    print(
        f"Medium Risk IPs : {medium_risk}"
    )

    print(
        f"Low Risk IPs : {low_risk}"
    )

    print(
        "\n---------- TOP ATTACKER ----------"
    )

    print(
        f"\nIP Address : {top_attacker_ip}"
    )

    print(
        f"\nFailed Attempts : {top_attacker_attempts}"
    )

    print(
    "\nTOP ATTACKERS RANKING"
    )

    rank = 1

    for ip, attempts in ranking_list[:3]:

        print(
        f"\n{rank}. {ip} --> {attempts} Attempts"
        )

        rank += 1

    

    print(
    "\nHTML Report Generated"
    )

    print(
        "\n========== TIMESTAMP ANALYSIS =========="
    )

    print(
        f"\nFirst Event : {first_event}"
    )

    print(
        f"\nLast Event : {last_event}"
    )    

    print(
        "\n=================================="
    )

    print(
        "\nSOC Analysis Complete"
    )

except FileNotFoundError:

    print(
        "ERROR: Log file not found"
    )

except Exception as error:

    print(
        f"Unexpected Error: {error}"
    )