from django.contrib import admin
from login.models import UserProfileInfo,CustomUser
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserProfileInfo)