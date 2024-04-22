from django.conf import settings
from django_celery_beat.models import PeriodicTask, IntervalSchedule

def create_periodic_task(sender, **kwargs):
    # Import the task function
    from .tasks import write_random_letter
    
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
    except Exception as e:
        # Handle exceptions (log them, alert, or retry as appropriate for your case)
        pass
