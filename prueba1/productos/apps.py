from django.apps import AppConfig
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError

class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'

    def ready(self):
        # Importa la tarea de Celery aquí para evitar problemas de importación
        from .tasks import write_random_letter

        # django-celery-beat imports
        from django_celery_beat.models import PeriodicTask, IntervalSchedule

        # Configura una tarea periódica
        try:
            # Crea un intervalo de programación cada minuto
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=1,
                period=IntervalSchedule.MINUTES,
            )
            
            # Crea la tarea periódica asociada al intervalo
            PeriodicTask.objects.get_or_create(
                interval=schedule,
                name='Write Random Letter Task',
                task='productos.tasks.write_random_letter',
            )
        except (OperationalError, ProgrammingError):
            # Esto captura la excepción si la base de datos no está lista
            # Un caso común es cuando se ejecutan comandos de manage.py antes de la migración de la base de datos
            pass
