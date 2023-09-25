from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Reply
from .tasks import task_send_email_about_reply_create, task_send_email_about_reply_accept


@receiver(post_save, sender=Reply)
def reply_created(sender, instance, created, **kwargs):
    if created:
        task_send_email_about_reply_create.delay(instance.id)


@receiver(pre_save, sender=Reply)
def reply_created(sender, instance, *args, **kwargs):
    if instance.id:
        old_version = Reply.object.get(id=instance.id)
        if not old_version.is_accepted == instance.is_accepted:
            task_send_email_about_reply_accept.delay(instance.id)



