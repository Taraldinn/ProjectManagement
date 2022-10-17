from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter Your Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Confirm Password'}),
            
        }
