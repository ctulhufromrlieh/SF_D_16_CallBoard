from celery import shared_task

from .email_sending import mass_email_sending, send_email_about_reply_create, send_email_about_reply_accept


@shared_task
def task_mass_email_sending():
    mass_email_sending()

@shared_task
def task_send_email_about_reply_create(reply_id):
    send_email_about_reply_create(reply_id)

@shared_task
def task_send_email_about_reply_accept(reply_id):
    send_email_about_reply_accept(reply_id)

