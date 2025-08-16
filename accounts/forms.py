from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    username_login = forms.CharField(
        label='Username', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'Your Name',
            }
        ),
    )
    password=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'Type your password',
            }
        ),
    )

class RegisterForms(forms.Form):
    username_register=forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'Your Name',
            }
        ),
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'youremail@xpto.com',
            }
        ),
    )
    password_1=forms.CharField(
        label='Password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'Type your password',
            }
        ),
    )
    password_2=forms.CharField(
        label='Confirm your password', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-stone-600 border border-stone-500 rounded-lg text-stone-300 text-md w-full p-2.5',
                'placeholder': 'Type your password again',
            }
        ),
    )

    def clean_username_register(self):
        username_register = self.cleaned_data.get('username_register')
        if User.objects.filter(username=username_register).exists():
            raise forms.ValidationError("This username is already taken.")
        return username_register
    
    def clean_password_2(self):
        cleaned_data=super().clean()
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data