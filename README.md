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

## Port Scanning
 

-Function: Discovers open ports on a target IP address or domain.

-Relevance: By identifying open ports, a tester can map out a system's network services and find potential entry points for an attack. For example, an open port 22 suggests that an SSH server is running, while port 80 or 443 suggests a web server.

-Implementation: This module uses the socket library to attempt connections to a specified range of ports, reporting which ones are open. 

Example:-

Enter target IP or domain: 8.8.8.8

Enter ports (comma-separated): 22,80,443


## SSH Brute Forcing

-Function: Attempts to gain unauthorized access to a Secure Shell (SSH) server by guessing the login credentials.

-Relevance: This test identifies weak passwords by systematically trying combinations from a provided wordlist. A successful brute-force attack on SSH provides a way to gain shell access to the target system.

-Implementation: The tool uses a library like paramiko to automate connection attempts with a list of usernames and passwords from a file until it finds a valid combination.

Example:-

Enter target IP: 192.168.1.10

Enter username: admin

Enter path to password file: passwords.txt

## Vulnerability Scanner (HTTP Version Check)

-Function: Checks the HTTP version number of a target web server.

-Relevance: An outdated web server version can have known vulnerabilities that malicious actors can exploit. By identifying the software and version, a tester can look up existing exploits and potential misconfigurations.

-Implementation: This module makes an HTTP request to a target URL and inspects the response headers to extract server and version information.

Example:-

Enter target URL: https://examples.com


## Directory Brute Forcing

-Function: Finds hidden directories and files on a web server by using a wordlist.

-Relevance: Often, web servers contain files and directories that are not publicly linked but are still accessible. A successful directory brute-force can uncover sensitive data, misconfigured administrative interfaces, or valuable information for further attacks.

-Implementation: This tool iterates through a list of common directory names, attempting to access them on the target web server and reporting any successful hits.

Example:-

Enter target URL: http://example.com

Enter path to wordlist: wordlist.txt

## HTTP Header Scanning

-Function: Analyzes the HTTP response headers sent by a web server.

-Relevance: Response headers can reveal important security-related information. For example, the Content-Security-Policy header helps protect against Cross-Site Scripting (XSS), and the Strict-Transport-Security header enforces HTTPS. Misconfigured or missing security headers can indicate vulnerabilities.

-Implementation: This module sends an HTTP request to the target URL and then displays the server's response headers for review.

Example:-

Enter target URL: http://example.com

## Output
