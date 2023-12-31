from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'intro', 'full_text', 'date']
        widgets = {
            'title' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Title of the Article'
            }),
            'intro' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Intro of the Article'
            }),
            'date' : DateTimeInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Date of Publication'
            }),
            'full_text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Text of the Article'
            }),
        }