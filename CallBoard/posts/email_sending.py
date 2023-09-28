from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import mail_managers, EmailMultiAlternatives

from .models import Post, Category, Reply
from .models import SchedulingMailData


def save_email_last_send_date(new_last_send_date):
    smds = SchedulingMailData.objects.all()
    if smds.count():
        smd = SchedulingMailData.objects.all()[0]
    else:
        smd = SchedulingMailData(last_send_date=new_last_send_date)

    smd.last_send_date = new_last_send_date
    smd.save()


def load_email_last_send_date():
    smds = SchedulingMailData.objects.all()
    if smds.count():
        return smds[0].last_send_date
    else:
        return None


def mass_email_sending():
    print("mass_email_sending")
    # last_send_date = get_last_send_date()
    last_send_date = load_email_last_send_date()
    print(last_send_date)
    # sub_user_ids = Subscription.objects.all().distinct().values_list("user", flat=True)
    # All users - subscribers (later can be changed) !
    sub_user_ids = User.objects.all().values_list("id", flat=True)

    new_last_send_date = datetime.utcnow()

    for curr_sub_user_id in sub_user_ids:
        curr_sub_user = User.objects.get(id=curr_sub_user_id)

        if last_send_date:
            curr_posts = Post.objects.all().exclude(creation_date__lt=last_send_date)
        else:
            curr_posts = Post.objects.all()

        if curr_posts.count() == 0:
            print(f"{curr_sub_user}: Ничего нет!")

            continue

        text_content = f"Новые объявления для {curr_sub_user.username}:\n"
        html_content = f"Новые объявления для {curr_sub_user.username}:<br>"
        for curr_post in curr_posts:
            text_content += f"{curr_post.title} от {curr_post.author.username}\n"
            html_content += f'{curr_post.title} от {curr_post.author.username}'

        text_contents = (text_content)
        html_contents = (html_content)

        msg = EmailMultiAlternatives(f"Новые объявления", text_contents, None, [curr_sub_user.email])
        msg.attach_alternative(html_contents, "text/html")
        msg.send()

    save_email_last_send_date(new_last_send_date)


def send_email_about_reply_create(reply_id):
    instances = Reply.objects.filter(id=reply_id)
    if instances.count() == 0:
        return
    instance = instances[0]

    text_content = (
        f'Вышел отклик на Ваше объявление, {instance.post.author.username}:\n'
        f'Заголовок: {instance.post.title}\n'
        f'Категория: {instance.post.category.name}\n'
        f'Автор отклика: {instance.user.username}\n'
        f'Текст отклика: {instance.text}\n'
    )
    html_content = (
        f'Вышел отклик на Ваше объявление, {instance.post.author.username}:<br>'
        f'Заголовок: {instance.post.title}<br>'
        f'Категория: {instance.post.category.name}<br>'
        f'Автор отклика: {instance.user.username}<br>'
        f'Текст отклика: {instance.text}<br>'
    )
    subject = f'Отклик на Ваше объявление {instance.post.title} от {instance.user.username}!'

    msg = EmailMultiAlternatives(subject, text_content, None, [instance.post.author.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_email_about_reply_accept(reply_id):
    instances = Reply.objects.filter(id=reply_id)
    if instances.count() == 0:
        return

    instance = instances[0]
    text_content = (
        f'Ваш отклик одобрен, {instance.user.username}:\n'
        f'Автор: {instance.post.author.username}\n'
        f'Заголовок: {instance.post.title}\n'
        f'Категория: {instance.post.category.name}\n'
        f'Текст отклика: {instance.text}\n'
    )
    html_content = (
        f'Ваш отклик одобрен, {instance.user.username}<br>:'
        f'Автор: {instance.post.author.username}<br>'
        f'Заголовок: {instance.post.title}<br>'
        f'Категория: {instance.post.category.name}<br>'
        f'Текст отклика: {instance.text}<br>'
    )
    subject = f'Ваш отклик на статью {instance.post.title} от {instance.post.author.username} принят!'

    msg = EmailMultiAlternatives(subject, text_content, None, [instance.user.email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
