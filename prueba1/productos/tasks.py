from celery import shared_task
import os
import random

@shared_task
def write_random_letter():
    # Obtiene la ruta del directorio actual donde se encuentra este archivo tasks.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta completa del archivo log dentro del directorio actual
    file_path = os.path.join(current_dir, 'alphabet_log.txt')

    # Verifica si el archivo existe, si no, lo crea
    if not os.path.exists(file_path):
        # Crear el archivo y escribir la letra aleatoria
        with open(file_path, 'w') as file:
            pass

    # Cambia los permisos del archivo para que sea escritura y lectura (opcional)
    # os.chmod(file_path, 0o644)

    # Escribe una letra aleatoria en el archivo
    with open(file_path, 'a') as file:
        # Genera una letra aleatoria en mayúscula
        letter = chr(random.randint(65, 90))
        file.write(f"{letter}\n")
