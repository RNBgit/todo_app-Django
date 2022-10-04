from operator import index
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Tasklist.as_view(), name='task_list_url'),
    path('<str:id>/completed/', views.TaskComplete.as_view(), name="task_complete_url" ),
    path('<str:id>/delete/', views.TaskDelete.as_view(), name="task_delete_url" ),
]