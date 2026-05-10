# 🛡️ Network Security & Audit Toolkit (Python)

Este repositorio contiene herramientas de automatización desarrolladas en **Python** para la fase de reconocimiento y análisis de vulnerabilidades en auditorías de red. El proyecto integra conceptos avanzados de networking alineados con la certificación **Cisco Networking Academy**.

## 🛠️ Herramientas Incluidas

### 1. Advanced Port Scanner (`port_scanner.py`)
Realiza un escaneo de puertos utilizando el protocolo **TCP**. 
* **Lógica:** Utiliza el "Three-way Handshake" de TCP para determinar si un servicio está aceptando conexiones.
* **Uso:** Identificación rápida de superficies de ataque.

### 2. Banner Grabber PRO (`banner_grabber.py`)
Herramienta de enumeración que extrae metadatos de los servicios activos.
* **Lógica:** Se conecta al socket y captura el "banner" de bienvenida del servicio (SSH, FTP, HTTP). 
* **Valor Técnico:** Permite identificar versiones de software específicas para cruzar con bases de datos de vulnerabilidades (CVE).

### 3. Web Directory Fuzzer (`dir_fuzzer.py`)
Script de descubrimiento de contenido oculto en servidores web.
* **Lógica:** Realiza peticiones HTTP automatizadas utilizando un diccionario de palabras clave (fuzzing) y analiza los códigos de estado (200 OK, 403 Forbidden).

## 📊 Especificaciones Técnicas
- **Lenguaje:** Python 3.x
- **Librerías:** `socket`, `requests`
- **Protocolos Analizados:** TCP, HTTP, ARP, ICMP.

## ⚠️ Aviso Ético y Legal
Este toolkit ha sido desarrollado exclusivamente para **fines educativos y auditorías autorizadas**. El acceso no autorizado a sistemas informáticos es un delito. El autor no se hace responsable del uso indebido de estas herramientas.

---
📫 **Contacto Profesional:**
jordi h https://www.linkedin.com/in/jordi-hernansanch-baab55402
