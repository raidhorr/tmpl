from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'text', ]
        labels = {
            'author': 'Автор',
            'category': "Категория",
            'title': 'Заголовок',
            'text': 'Текст'
        }

