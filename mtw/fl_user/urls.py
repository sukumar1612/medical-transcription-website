from django.urls import path
from fl_user import views


app_name = 'fl_user'

urlpatterns = [
    path('',views.display, name='display'),
]