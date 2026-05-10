import requests

def fuzz_directories(target_url, wordlist):
    print(f"[*] Iniciando Fuzzing de directorios en: {target_url}")
    print("-" * 40)
    
    # Headers falsos para simular un navegador real y evadir bloqueos básicos
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    for directory in wordlist:
        url_to_check = f"{target_url}/{directory}"
        try:
            response = requests.get(url_to_check, headers=headers, timeout=3)
            
            # Código 200 significa OK (Existe y se puede ver)
            if response.status_code == 200:
                print(f"[+] ENCONTRADO (200): {url_to_check}")
            # Código 403 significa Prohibido (Existe pero requiere permisos/login)
            elif response.status_code == 403:
                print(f"[!] RESTRINGIDO (403): {url_to_check}")
                
        except requests.exceptions.RequestException:
            pass # Ignoramos errores de conexión para no ensuciar la pantalla

if __name__ == '__main__':
    # OBJETIVO: Cambiar por URL autorizada
    target = "http://127.0.0.1"
    
    # Diccionario simulado (en la vida real se lee de un archivo .txt con miles de palabras)
    diccionario_comun = [
        "admin", "login", "uploads", "backup", "db", 
        "config", "phpmyadmin", "test", "hidden"
    ]
    
    fuzz_directories(target, diccionario_comun)
