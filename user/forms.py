from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 border border-amber-300 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-amber-500',
            'placeholder': 'Ej: Usuario',
            'autocomplete': 'username',
            'id': 'username'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 border border-amber-400 rounded-lg focus:ring-2 focus:ring-amber-500 focus:border-amber-500',
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
            'id': 'password'
        }),
    )
