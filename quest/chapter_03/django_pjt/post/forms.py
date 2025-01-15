from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "post_img"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'title',
                'placeholder': 'Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'content',
                'rows': 7,
                'placeholder': 'Content'
            }),
            'post_img': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'formFile'
            })
        }