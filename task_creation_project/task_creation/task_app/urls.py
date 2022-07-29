from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url




from django.urls import path
from django.conf.urls import url
from .views import TaskView


urlpatterns = [
    url(r'^task_creation', TaskView.as_view(), name='file-upload'),
   
]