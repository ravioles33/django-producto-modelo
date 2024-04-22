# from celery import shared_task
# import random
# import string

# @shared_task
# def save_random_letter_txt():
#     letter = random.choice(string.ascii_letters)
#     with open('alphabet.txt', 'a+') as file:
#         file.write(letter + '\n')

from celery import shared_task
import random
import string
from .models import RandomLetter  # Asegúrate de importar el modelo correcto

@shared_task
def save_random_letter():
    letter = random.choice(string.ascii_letters)
    RandomLetter.objects.create(letter=letter)  # Crea una nueva entrada en la base de datos
