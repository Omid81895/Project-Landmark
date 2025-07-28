from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput({'class': 'form-control'})
                                )
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput({'class': 'form-control'})
                                )
    class Meta:
        model = User
        fields = ['username']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
# J.J :jjandbfm