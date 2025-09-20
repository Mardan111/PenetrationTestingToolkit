# Penetration Testing Toolkit


*COMPANY* : CODTECH IT SOLUTIONS PVT.LTD

*NAME* : MOHAMMED MARDAN ALI

*INTERN ID* : CT04DY1075

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR

## Overview

The **Penetration Testing Toolkit** is a Python-based framework designed for performing common penetration testing activities. This modular toolkit includes tools for scanning open ports, brute-forcing SSH login credentials, checking HTTP versions, brute-forcing web directories, and scanning HTTP headers for vulnerabilities. This toolkit is intended for **ethical hacking** and **security research** purposes, so **only use it on systems you have explicit permission to test**.

### **Modules Included:**

1. **Port Scanner** (`port_scanner.py`): A tool to scan open ports on a target IP or domain.
2. **Brute-Force SSH** (`brute_forcer.py`): Attempts to brute-force SSH login credentials using a wordlist.
3. **HTTP Version Check (Vulnerability Scanner)** (`vuln_scanner.py`): Checks the HTTP version and server details of a target.
4. **Directory Brute-Force** (`dir_brute.py`): Brute-forces common web directories using a wordlist.
5. **HTTP Header Scanner** (`header_scanner.py`): Scans HTTP headers for vulnerabilities.

---



## Project Setup

This toolkit is organized as a modular system where each script corresponds to a specific penetration testing task. The main script (`main.py`) acts as an entry point that provides a simple menu for selecting and running different tools.

### **Prerequisites**

Before you run the tools, make sure you have the following:

- **Python 3.x** (Recommended version: Python 3.6+)
- Python libraries:
  - `requests`
  - `paramiko`

To install the required libraries, run the following:

```bash
pip install requests paramiko
```

## Usage

The main entry point for the toolkit is the main.py file. This script provides an interactive menu to choose and run each of the penetration testing tools.

Main Program (main.py)

To start the toolkit, run the main.py script:

python3 main.py

Penetration Testing Toolkit
===========================
1. Port Scanner
2. Brute Forcer (SSH)
3. Vulnerability Scanner (HTTP Version Check)
4. Directory Brute Force (Web Server)
5. HTTP Header Scanner
0. Exit

Example Commands

 Port Scanning

Enter target IP or domain: 8.8.8.8
Enter ports (comma-separated): 22,80,443

SSH Brute Forcing

Enter target IP: 192.168.1.10
Enter username: admin
Enter path to password file: passwords.txt

HTTP Version Check

Enter target URL: http://example.com

Directory Brute Forcing

Enter target URL: http://example.com
Enter path to wordlist: wordlist.txt

HTTP Header Scanning

Enter target URL: http://example.com
