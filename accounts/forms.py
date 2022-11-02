from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Profile
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Surname'}),
            'fathers_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Father name'}),
            'mothers_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mother name'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control datepicker-here', 'data-language':'en'}),
            'sex_name': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone number'}),
            'postel_code': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Postel code'}),
            'nid_card_no': forms.TextInput(attrs={'class': 'form-control','placeholder': 'NID card no...'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'City'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Address'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nationality'}),
            'marital_Status': forms.CheckboxInput(attrs={'type': 'checkbox'})
            
        }

