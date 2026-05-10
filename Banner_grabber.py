import socket

def grab_banner(ip, port):
    try:
        # Configuramos el timeout para no quedarnos bloqueados
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        
        # Enviamos una petición genérica por si es un servidor HTTP/Web
        s.send('GET / HTTP/1.1\r\n\r\n'.encode())
        
        # Recibimos la respuesta (el "banner")
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return f"No se pudo obtener banner o puerto cerrado."

if __name__ == '__main__':
    # OBJETIVO: Cambiar por una IP autorizada para auditoría
    target = "127.0.0.1" 
    ports = [22, 21, 80] # SSH, FTP, HTTP
    
    print(f"[*] Iniciando extracción de banners en {target}...")
    print("-" * 40)
    
    for port in ports:
        banner = grab_banner(target, port)
        if banner and "No se pudo" not in banner:
            print(f"[+] Puerto {port} ABIERTO | Servicio/Versión: {banner}")
