from django import forms
from django.db.models import fields

from .models import Article

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumb']