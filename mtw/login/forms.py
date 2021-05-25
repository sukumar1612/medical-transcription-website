from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo,CustomUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = CustomUser
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('user_designation',)