import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CallBoard.settings')

app = Celery('CallBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'mass_email_sending': {
    #     'task': 'news.tasks.task_mass_email_sending',
    #     # 'schedule': 10,
    #     # 'schedule': crontab(minute='0', hour='8', day_of_week='mon')
    #     # 'args': (5,),
    # },
}