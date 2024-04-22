from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from django.conf import settings

# Configura el entorno Django para Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba1.settings')

# Configura la instancia de Celery
app = Celery('prueba1')

# Carga las configuraciones desde tu proyecto Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubre automáticamente las tareas en las aplicaciones instaladas
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Configuración del logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.task(bind=True)
def debug_task(self):
    logger.info('Request: {0!r}'.format(self.request))
