from django import forms
from django.contrib.auth.models import User
from login.models import CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = CustomUser
        fields = ('email', 'password')
