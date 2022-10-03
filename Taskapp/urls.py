from operator import index
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Tasklist.as_view(), name='task_list_url')

]