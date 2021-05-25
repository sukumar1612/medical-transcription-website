from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.email

user_options=[
    ('doctor', 'doctor'),
    ('first level user', 'first level user'),
    ('second level user', 'second level user')
]

class UserProfileInfo(models.Model):

    customuser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_designation = models.CharField(max_length=50,choices=user_options)

    def __str__(self):
        return self.customuser.username