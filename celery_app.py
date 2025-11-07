import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

app = Celery('alx_backend_security')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Periodic task configuration
app.conf.beat_schedule = {
    'detect-anomalies-hourly': {
        'task': 'ip_tracking.tasks.detect_anomalies',
        'schedule': 3600.0,  # Run every hour (3600 seconds)
    },
}
app.conf.timezone = 'UTC'