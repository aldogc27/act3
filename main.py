import shutil
import os

def copiar_archivo(origen, destino):
    try:
        shutil.copy(origen, destino)
        print(f"Archivo copiado exitosamente de  '{origen}' a '{destino}'.")
    except FileNotFoundError:
        print(f"El archivo '{origen}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    origen = "archivo.txt"
    destino = "archivo_copia.txt"

    if os.path.exists(origen):
        copiar_archivo(origen, destino)
    else:
        print(f"No se encontró el archivo '{origen}'. Asegúrate de que exista en la misma carpeta.")

