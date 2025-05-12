
🧠 Introduction

Airlines Hacking Vulnerability Analyzer is a Python-based tool developed to identify and analyze vulnerabilities in the aviation sector, focusing on ADS-B (Automatic Dependent Surveillance-Broadcast), in-flight WiFi systems, and aircraft maintenance networks. The project utilizes data analysis and machine learning techniques to simulate and demonstrate attack scenarios, detect anomalies in network traffic, and raise awareness about potential cyber threats in airline digital infrastructure.

🚨 Problem Statement

As the aviation industry increasingly relies on digital communications and networks, systems such as ADS-B, in-flight WiFi, and aircraft maintenance systems are exposed to sophisticated cyber threats, including spoofing, eavesdropping, and remote exploitation. Traditional methods struggle to detect these complex attack patterns. This project uses Python and machine learning to detect anomalies, simulate attacks, and help understand these vulnerabilities via a localhost-accessible reporting system.

🧰 Features

ADS-B Vulnerability Analysis: Simulates spoofing attacks and detects abnormal ADS-B broadcasts.

In-flight WiFi Attack Simulation: Demonstrates MITM attacks, captive portal phishing, and traffic manipulation scenarios.

Maintenance System Vulnerability Analysis: Detects insecure configurations and exposed services using simulation and static analysis.

Anomaly Detection Models: Applies algorithms like Isolation Forest and Random Forest on aviation-related datasets.

Browser-Based Reporting on Localhost: Generates visual reports and summaries accessible at http://localhost:<port> using Flask or Jupyter Notebook.

Runs via Terminal (Windows Command Prompt / PowerShell).

📈 Workflow Diagram

ADS-B / WiFi / Maintenance System Data
⬇
Data Preprocessing & Anomaly Detection
⬇
Simulation & Risk Assessment
⬇
Reports & Visualization (Accessible on localhost)

⚙️ Setup Instructions (Windows + Terminal + Localhost)

✅ Prerequisites

Windows 10/11

Python 3.8 or higher

Internet connection (for installing dependencies and data fetching)

1.Simulated Aircraft Flights Paths

   ![Screenshot (4)](https://github.com/user-attachments/assets/cf968d67-67f3-432a-89ab-798e3282638d)
   ![Screenshot (3)](https://github.com/user-attachments/assets/8cef9ef8-d9e1-4a9f-ba90-78e4fd55cb00)
   ![Screenshot (5)](https://github.com/user-attachments/assets/96b587f2-4924-4ae0-8bdb-90a305836357)



2.Anmaly Detction

   ![Screenshot (8)](https://github.com/user-attachments/assets/a33870a9-bdb9-4fed-8496-129ce40d501d)
   ![Screenshot (7)](https://github.com/user-attachments/assets/3845acc3-bad3-46a9-a125-412633b9938b)
   ![Screenshot (6)](https://github.com/user-attachments/assets/2f02ce75-a7e8-4375-872e-c9aeb602668f)



3.CSV Logging

   ![Screenshot (10)](https://github.com/user-attachments/assets/70eeffad-a712-4b3f-b570-0437b7a71568)
   ![Screenshot (9)](https://github.com/user-attachments/assets/824f2ff5-c133-43ce-99c8-a79df7310cc0)


4.Maintence checker

   ![Screenshot (13)](https://github.com/user-attachments/assets/0ef0ca8f-74f6-4cab-a398-34aec4662113)



5. ICOA cloaning dectector
   
   ![Screenshot (14)](https://github.com/user-attachments/assets/fde03494-d482-463d-a554-5ac26e9f8a55)


6.Flight path visualization

   ![Screenshot (18)](https://github.com/user-attachments/assets/72a54334-2527-4604-b39d-b982caa3bf2b)
   

👤 Developed By

Darshana Bhaud

Digisuraksha Internship Program

Date: 12-May-2025

License & Disclaimer

This project is released under the MIT License. See the LICENSE file for details.

Disclaimer:

This research project on airline cybersecurity, specifically focusing on ADS-B vulnerabilities, in-flight WiFi, and maintenance system exploits, is intended for educational and research purposes only. The information presented does not guarantee the security of any systems or networks. It is important to note that hacking or exploiting these vulnerabilities is illegal and unethical. This work is not intended to encourage or promote malicious activities. Users should adhere to all applicable laws and regulations and implement proper security measures to protect their systems from potential threats. The findings and recommendations provided should be complemented by professional cybersecurity practices.


