from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
	path('', views.TaskList.as_view(), name='taskList'),
]