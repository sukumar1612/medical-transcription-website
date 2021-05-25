from django.urls import path
from login import views

urlpatterns = [
    path('login/',views.auth_login, name='auth_login'),
]