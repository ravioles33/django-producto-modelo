from __future__ import absolute_import, unicode_literals

# Esto asegurará que la aplicación Celery siempre se importe cuando
# Django arranque para que las tareas compartidas puedan usar esta aplicación.
from .celery import app as celery_app

__all__ = ('celery_app',)
