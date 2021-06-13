from django.urls import path
from login import views


app_name = 'login'

urlpatterns = [
    path('',views.auth_login, name='auth_login'),
]
