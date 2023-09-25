from django import template


register = template.Library()


@register.filter()
def add(value1, value2):
    return value1 + value2


@register.filter()
def is_users_post(post, user):
    return post.author.id == user.id

@register.filter()
def is_not_users_post(post, user):
    return not post.author.id == user.id
