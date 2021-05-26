from django.contrib import admin
from login.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('email','username','fullname','date_joined', 'last_login', 'is_admin','is_staff')
    search_fields = ('email','username','fullname')
    readonly_fields=('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomUserAdmin)