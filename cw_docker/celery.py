import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cw_docker.settings')

app = Celery('cw_docker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-file-every-one-min': {
        'task': 'checker.tasks.check_file',
        'schedule': crontab(minute='*/1'),
    },
}
