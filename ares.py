import subprocess
import datetime
import os
import time

def ejecutar_en_kali(comando):
    # Usamos proot-distro para entrar al sistema que instalaste
    proceso = f"proot-distro login debian -- /bin/bash -c '{comando}'"
    try:
        resultado = subprocess.check_output(proceso, shell=True, stderr=subprocess.STDOUT)
        return resultado.decode('utf-8')
    except Exception as e:
        return f"Ares detectó un problema técnico: {str(e)}"

def sincronizar_github():
    print("[Ares]: Subiendo reporte actualizado a la nube...")
    os.system("git add .")
    os.system("git commit -m 'Ares: Actualización de estado autónoma'")
    os.system("git push origin main")

# --- INICIO DEL CICLO ---
print(">>> ARES ESTÁ DESPIERTO EN TU INFINIX NOTE 40 <<<")

while True:
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n[*] Ares iniciando tarea: {ahora}")
    
    # Ares realiza un escaneo rápido
    datos = ejecutar_en_kali("nmap -F google.com")
    
    # Creamos el reporte que verás en GitHub
    with open("status_ares.txt", "w") as f:
        f.write(f"REPORTE AUTÓNOMO DE ARES\n")
        f.write(f"Última actualización: {ahora}\n")
        f.write(f"Datos obtenidos:\n{datos}")
    
    # Ares sube su trabajo solo
    sincronizar_github()
    
    print("\n[Ares]: Tarea terminada. Vigilando de nuevo en 10 minutos...")
    time.sleep(600)
