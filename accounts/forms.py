# from django import forms
from .models import User
from django.contrib.auth.models import AbstractUser
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'image', 'phone', 'email']
        help_texts = {
            'username': None,  # This removes the help text for username
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True  
        if commit:
            user.save()
        return user

from django import forms
from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'image']  