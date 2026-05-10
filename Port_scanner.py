import socket

def port_scanner(ip, ports):
    print(f"--- Escaneando {ip} ---")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Puerto {port}: ABIERTO")
        sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1" 
    target_ports = [21, 22, 80, 443, 8080]
    port_scanner(target_ip, target_ports)

