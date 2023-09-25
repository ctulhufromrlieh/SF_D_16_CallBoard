from django import forms
from django.contrib.auth.models import User

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Category, Reply


class PostForm(forms.ModelForm):
    # author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор:")
    # author = forms.IntegerField(widget=forms.HiddenInput(), disabled=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория:")
    title = forms.CharField(max_length=255, label="Заголовок")
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Текст")

    class Meta:
        model = Post
        # fields = ['author', 'category', 'title', 'content']
        fields = ['category', 'title', 'content']

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', None) # pop the 'user' from kwargs dictionary
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['author'] = forms.ModelChoiceField(queryset=User.objects.filter(id=user.id), empty_label=None, label="Автор:")
    #     # self.fields['author'].initial = user.id


class ReplyForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label="Текст:")
    # user = forms.IntegerField(widget=forms.HiddenInput(), disabled=True, initial=-1)
    # post = forms.IntegerField(widget=forms.HiddenInput(), disabled=True, initial=-1)
    class Meta:
        model = Reply
        # fields = ['text', 'user', 'post']
        fields = ['text']

