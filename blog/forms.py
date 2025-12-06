from django import forms 
from .models import Post, Comment

class Forms(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva seu comentário'})
        }