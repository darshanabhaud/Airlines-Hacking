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

