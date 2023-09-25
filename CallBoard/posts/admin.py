from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Category, Post, Reply


# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['author', 'category', 'title', 'content']


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Reply)