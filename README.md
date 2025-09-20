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

## Table of Contents

1. [Project Setup](#project-setup)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Main Program (`main.py`)](#main-program-mainpy)
4. [License](#license)
5. [Disclaimer](#disclaimer)
6. [Contact](#contact)

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
