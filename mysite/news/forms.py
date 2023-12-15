from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date','photo']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи',
            }),
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tекст статьи',
            }),
            "file": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'foto',
            }),
        }
