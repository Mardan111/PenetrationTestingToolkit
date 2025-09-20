import sys
from port_scanner import port_scan
from brute_forcer import brute_force_ssh
from vuln_scanner import check_http_version
from dir_brute import brute_force_dirs
from header_scanner import scan_http_headers

def display_menu():
    print("\nPenetration Testing Toolkit")
    print("===========================")
    print("1. Port Scanner")
    print("2. Brute Forcer (SSH)")
    print("3. Vulnerability Scanner (HTTP Version Check)")
    print("4. Directory Brute Force (Web Server)")
    print("5. HTTP Header Scanner")
    print("0. Exit")
    choice = input("Select an option: ")
    return choice

def run_tool(choice):
    if choice == '1':
        target_ip = input("Enter target IP or domain: ")
        ports = input("Enter ports (comma-separated): ").split(',')
        ports = [int(port.strip()) for port in ports]
        port_scan(target_ip, ports)
    elif choice == '2':
        target_ip = input("Enter target IP: ")
        username = input("Enter username: ")
        password_file = input("Enter path to password file: ")
        brute_force_ssh(target_ip, username, password_file)
    elif choice == '3':
        target_url = input("Enter target URL: ")
        check_http_version(target_url)
    elif choice == '4':
        target_url = input("Enter target URL: ")
        wordlist = input("Enter path to wordlist: ")
        brute_force_dirs(target_url, wordlist)
    elif choice == '5':
        target_url = input("Enter target URL: ")
        scan_http_headers(target_url)
    elif choice == '0':
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    while True:
        choice = display_menu()
        run_tool(choice)
