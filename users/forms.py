from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')