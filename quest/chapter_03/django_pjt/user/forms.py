from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms
from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "nickname", "profile_img", "bio"]
        

# 프로필
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname", "profile_img", "bio"]
        widgets = {
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nickname',
                'placeholder': 'Nickname'
            }),
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'bio',
                'placeholder': 'Bio'
            }),            
            'profile_img': forms.FileInput(attrs={
                'class': 'form-control',
                'id': 'formFile'
            })
        }  