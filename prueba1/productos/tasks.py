from celery import shared_task
import random
import string

@shared_task
def save_random_letter():
    letter = random.choice(string.ascii_letters)
    with open('alphabet.txt', 'a+') as file:
        file.write(letter + '\n')
