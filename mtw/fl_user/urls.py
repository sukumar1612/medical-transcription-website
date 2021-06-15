from django.urls import path
from fl_user import views


app_name = 'fl_user'

urlpatterns = [
    path('receive_data/',views.receive_data, name='receive_data'),
    path('home/', views.home, name='home'),
    path('view_task/',views.view_task,name="view_task"),
    path('view_task_doc/',views.view_task_doc,name="view_task_doc"),
    path('view_task_slu/',views.view_task_slu,name="view_task_slu"),
]
