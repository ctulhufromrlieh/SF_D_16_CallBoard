from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Category name")

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True, help_text="Category name")
    content = RichTextUploadingField()

    @property
    def preview(self):
        txt = str(self.content)
        if len(txt) > 124:
            return txt[:124] + "..."
        else:
            return txt

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")
    is_accepted = models.BooleanField(default=False)

    def accept(self):
        self.is_accepted = True