from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
	path('', views.TaskList.as_view(), name='taskList'),
	path('<int:pk>', views.TaskDetail.as_view(), name='taskDetail'),
	path('<int:pk>/edit', views.TaskEdit.as_view(), name='taskEdit'),
	path('<int:pk>/confirmDelete', views.TaskDelete.as_view(), name='taskDelete'),
]