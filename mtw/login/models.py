from django.db import models
from django.contrib.auth.models import User

# Create your models here.

user_options=[
    ('doctor', 'doctor'),
    ('first level user', 'first level user'),
    ('second level user', 'second level user')
]

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_designation = models.CharField(max_length=50,choices=user_options)

    def __str__(self):
        return self.user.username