import socket
import threading

def scan_port(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip, port))
        print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

def port_scan(target_ip, ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
