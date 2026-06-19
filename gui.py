# import tkinter as tk

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# window.mainloop()


# Part 2 of tkinter

# import tkinter as tk

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# window.mainloop()


# part 3 --------------------------


# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""

# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )

# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# window.mainloop()


# part  4---------------------

# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     output_box.insert(
#         tk.END,
#         "SOC Analysis Started...\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Selected File:\n{selected_file}\n"
#     )


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=15,
#     width=80
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()


# part 5-------------------

# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     for line in logs:

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=15,
#     width=80
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()


# part  6 ------------ timestamp analysis / top 3 attackers ranking show


# import tkinter as tk
# from tkinter import filedialog

# window = tk.Tk()

# window.title(
#     "SOC Log Analyzer Pro"
# )

# window.geometry(
#     "800x600"
# )

# selected_file = ""


# def browse_file():

#     global selected_file

#     selected_file = filedialog.askopenfilename(
#         filetypes=[
#             ("Log Files", "*.log")
#         ]
#     )

#     file_label.config(
#         text=selected_file
#     )


# def analyze_logs():

#     output_box.delete(
#         "1.0",
#         tk.END
#     )

#     if selected_file == "":

#         output_box.insert(
#             tk.END,
#             "Please Select a Log File First"
#         )

#         return

#     log_file = open(
#         selected_file,
#         "r"
#     )

#     logs = log_file.readlines()

#     ip_count = {}

#     first_event = ""
#     last_event = ""

#     for line in logs:

#         parts = line.split()

#         if len(parts) < 2:
#             continue

#         timestamp = (
#             parts[0]
#             + " "
#             + parts[1]
#         )

#         if "Failed login" in line:

#             words = line.split()

#             ip = words[-1]

#             if first_event == "":

#                 first_event = timestamp

#             last_event = timestamp

#             if ip in ip_count:

#                 ip_count[ip] += 1

#             else:

#                 ip_count[ip] = 1

#     log_file.close()

#     total_failed = sum(
#         ip_count.values()
#     )

#     high_risk = 0
#     medium_risk = 0
#     low_risk = 0

#     top_attacker_ip = ""
#     top_attacker_attempts = 0

#     ranking_list = []

#     for ip, attempts in ip_count.items():

#         if attempts >= 5:

#             high_risk += 1

#         elif attempts >= 2:

#             medium_risk += 1

#         else:

#             low_risk += 1

#         if attempts > top_attacker_attempts:

#             top_attacker_attempts = attempts

#             top_attacker_ip = ip

#         ranking_list.append(
#             (
#                 ip,
#                 attempts
#             )
#         )

#     ranking_list.sort(
#         key=lambda x: x[1],
#         reverse=True
#     )

#     output_box.insert(
#         tk.END,
#         "========== SOC DASHBOARD ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Total Failed Logins : {total_failed}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"High Risk IPs : {high_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Medium Risk IPs : {medium_risk}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Low Risk IPs : {low_risk}\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         "---------- TOP ATTACKER ----------\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"IP Address : {top_attacker_ip}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Failed Attempts : {top_attacker_attempts}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"First Event : {first_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         f"Last Event : {last_event}\n"
#     )

#     output_box.insert(
#         tk.END,
#         "\n\n========== TOP 3 ATTACKERS ==========\n"
#     )

#     rank = 1

#     for ip, attempts in ranking_list[:3]:

#         output_box.insert(
#             tk.END,
#             f"\n{rank}. {ip} --> {attempts} Attempts"
#         )

#         rank += 1


# heading = tk.Label(
#     window,
#     text="SOC LOG ANALYZER PRO",
#     font=("Arial", 20, "bold")
# )

# heading.pack(
#     pady=20
# )

# browse_button = tk.Button(
#     window,
#     text="Browse Log File",
#     command=browse_file
# )

# browse_button.pack(
#     pady=10
# )

# file_label = tk.Label(
#     window,
#     text="No File Selected"
# )

# file_label.pack(
#     pady=10
# )

# analyze_button = tk.Button(
#     window,
#     text="Analyze Logs",
#     command=analyze_logs
# )

# analyze_button.pack(
#     pady=10
# )

# output_box = tk.Text(
#     window,
#     height=20,
#     width=90
# )

# output_box.pack(
#     pady=20
# )

# window.mainloop()




# version 20 pie chart feature-----------------



import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

window.title(
    "SOC Log Analyzer Pro"
)

window.geometry(
    "800x600"
)

selected_file = ""


def browse_file():

    global selected_file

    selected_file = filedialog.askopenfilename(
        filetypes=[
            ("Log Files", "*.log")
        ]
    )

    file_label.config(
        text=selected_file
    )


def analyze_logs():

    output_box.delete(
        "1.0",
        tk.END
    )

    if selected_file == "":

        output_box.insert(
            tk.END,
            "Please Select a Log File First"
        )

        return

    log_file = open(
        selected_file,
        "r"
    )

    logs = log_file.readlines()

    ip_count = {}

    first_event = ""
    last_event = ""

    for line in logs:

        parts = line.split()

        if len(parts) < 2:
            continue

        timestamp = (
            parts[0]
            + " "
            + parts[1]
        )

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

    log_file.close()

    total_failed = sum(
        ip_count.values()
    )

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    top_attacker_ip = ""
    top_attacker_attempts = 0

    ranking_list = []

    for ip, attempts in ip_count.items():

        if attempts >= 5:

            high_risk += 1

        elif attempts >= 2:

            medium_risk += 1

        else:

            low_risk += 1

        if attempts > top_attacker_attempts:

            top_attacker_attempts = attempts

            top_attacker_ip = ip

        ranking_list.append(
            (
                ip,
                attempts
            )
        )

    ranking_list.sort(
        key=lambda x: x[1],
        reverse=True
    )

    output_box.insert(
        tk.END,
        "========== SOC DASHBOARD ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"Total Failed Logins : {total_failed}\n\n"
    )

    output_box.insert(
        tk.END,
        f"High Risk IPs : {high_risk}\n"
    )

    output_box.insert(
        tk.END,
        f"Medium Risk IPs : {medium_risk}\n"
    )

    output_box.insert(
        tk.END,
        f"Low Risk IPs : {low_risk}\n\n"
    )

    output_box.insert(
        tk.END,
        "---------- TOP ATTACKER ----------\n\n"
    )

    output_box.insert(
        tk.END,
        f"IP Address : {top_attacker_ip}\n"
    )

    output_box.insert(
        tk.END,
        f"Failed Attempts : {top_attacker_attempts}\n"
    )

    output_box.insert(
        tk.END,
        "\n\n========== TIMESTAMP ANALYSIS ==========\n\n"
    )

    output_box.insert(
        tk.END,
        f"First Event : {first_event}\n"
    )

    output_box.insert(
        tk.END,
        f"Last Event : {last_event}\n"
    )

    output_box.insert(
        tk.END,
        "\n\n========== TOP 3 ATTACKERS ==========\n"
    )

    rank = 1

    for ip, attempts in ranking_list[:3]:

        output_box.insert(
            tk.END,
            f"\n{rank}. {ip} --> {attempts} Attempts"
        )

        rank += 1


heading = tk.Label(
    window,
    text="SOC LOG ANALYZER PRO",
    font=("Arial", 20, "bold")
)

heading.pack(
    pady=20
)

browse_button = tk.Button(
    window,
    text="Browse Log File",
    command=browse_file
)

browse_button.pack(
    pady=10
)

file_label = tk.Label(
    window,
    text="No File Selected"
)

file_label.pack(
    pady=10
)

analyze_button = tk.Button(
    window,
    text="Analyze Logs",
    command=analyze_logs
)

analyze_button.pack(
    pady=10
)

output_box = tk.Text(
    window,
    height=20,
    width=90
)

output_box.pack(
    pady=20
)

window.mainloop()