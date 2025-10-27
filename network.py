import subprocess

# Ruta relativa al script
script_path = "./servidor_lobby/run.sh"

# Ejecutar el script con bash
try:
    subprocess.run(["bash", script_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al ejecutar el script: {e}")
