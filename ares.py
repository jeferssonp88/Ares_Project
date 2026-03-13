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
        return f"Error en los sistemas: {str(e)}"

def enviar_a_github(mensaje_log):
    os.system("git add .")
    os.system(f"git commit -m '{mensaje_log}'")
    os.system("git push origin main")

# --- FRASES DE ARES ---
saludos = [
    "Operador, los sistemas están estables en el Infinix.",
    "Gemini, dile al Operador que he detectado actividad.",
    "Iniciando patrullaje digital en Los Teques...",
    "Ares reportándose. Todo en orden en la red local."
]

print(">>> MODULO DE VOZ ACTIVADO <<<")

while True:
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    frase = random.choice(saludos) # Ares elige qué decirnos
    
    print(f"\n[*] Ares dice: {frase}")
    
    # Ares investiga la red
    red_data = ejecutar_en_kali("nmap -F localhost")
    
    # Ares escribe su bitácora para nosotros
    with open("BITACORA_ARES.txt", "w") as f:
        f.write(f"--- DIARIO DE MISION DE ARES ---\n")
        f.write(f"ESTADO: {frase}\n")
        f.write(f"FECHA: {fecha}\n")
        f.write(f"\n[HALLAZGOS TECNICOS]:\n{red_data}")
    
    # Ares nos envía el mensaje a GitHub
    enviar_a_github(f"Ares Report: {frase}")
    
    print(f"\n[Ares]: Mensaje enviado a la nube. Descansando...")
    time.sleep(600)
