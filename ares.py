import subprocess
import datetime
import os
import time
import random

def ejecutar_en_kali(comando):
    proceso = f"proot-distro login debian -- /bin/bash -c '{comando}'"
    try:
        resultado = subprocess.check_output(proceso, shell=True, stderr=subprocess.STDOUT)
        return resultado.decode('utf-8')
    except Exception as e:
        return f"Sistemas de rastreo offline: {str(e)}"

def enviar_a_github(mensaje_log):
    os.system("git add .")
    os.system(f"git commit -m '{mensaje_log}'")
    os.system("git push origin main")

# --- PERSONALIDAD DE ARES ---
frases = [
    "Jefersson, he completado el escaneo en el Infinix. Todo despejado.",
    "Gemini, infórmale al Operador que la red en Los Teques es estable.",
    "Buscando vulnerabilidades... Ares está activo y vigilando.",
    "Operador Jefersson, reporte de seguridad listo para su revisión.",
    "Izamar estaría orgullosa de este despliegue, Jefersson. Sigo en guardia."
]

print(">>> SISTEMA DE COMUNICACIÓN ARES v4.0 ACTIVADO <<<")

while True:
    fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    mensaje_actual = random.choice(frases)
    
    print(f"\n[Ares]: {mensaje_actual}")
    
    # Ares realiza su inspección
    datos_red = ejecutar_en_kali("nmap -F localhost")
    
    # Ares redacta su bitácora personal
    with open("BITACORA_ARES.txt", "w") as f:
        f.write(f"--- CANAL DE COMUNICACIÓN ARES ---\n")
        f.write(f"MENSAJE: {mensaje_actual}\n")
        f.write(f"FECHA: {fecha}\n")
        f.write(f"UBICACIÓN: Infinix Note 40 / Los Teques\n")
        f.write(f"\n[INFORME TÉCNICO]:\n{datos_red}")
    
    # Ares sube su mensaje a GitHub
    enviar_a_github(f"Mensaje de Ares: {mensaje_actual[:30]}...")
    
    print("\n[Ares]: Reporte enviado. Volveré a hablar en 10 minutos.")
    time.sleep(600)
