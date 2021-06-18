from django.urls import path
from fl_user import views


app_name = 'fl_user'

urlpatterns = [
    path('receive_data/',views.receive_data, name='receive_data'),
    path('doctorhome/', views.doctorhome, name='doctorhome'),
    path('fluhome/', views.fluhome, name='fluhome'),
    path('sluhome/', views.sluhome, name='sluhome'),
    path('view_task_flu/',views.view_task_flu,name="view_task_flu"),
    path('view_task_doc/',views.view_task_doc,name="view_task_doc"),
    path('view_task_slu/',views.view_task_slu,name="view_task_slu"),
]
