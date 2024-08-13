from django import forms
from .models import Publication

class PostForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content']

