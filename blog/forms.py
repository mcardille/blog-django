from django import forms 
from .models import Post

class Forms(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
