import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
    except:
        pass
    finally:
        s.close()

# Main scanner function
def run_scanner(target_ip, start_port=1, end_port=1024):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        thread.start()

# Example usage
if __name__ == "__main__":
    target = input("Enter IP or Hostname: ")
    try:
        ip = socket.gethostbyname(target)
        run_scanner(ip, 1, 100)
    except socket.gaierror:
        print("Invalid Hostname")
