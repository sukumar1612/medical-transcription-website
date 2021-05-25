from django.urls import path
from login import views

urlpatterns = [
    path('login/',views.auth_login, name='auth_login'),
    path('registerdoc/',views.registerdoc, name='registerdoc'),
    path('registerflu/',views.registerflu, name='registerflu'),
    path('registerslu/',views.registerslu, name='registerslu'),
]