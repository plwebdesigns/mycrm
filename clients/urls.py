from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'clients'
urlpatterns = [
	path('', views.clientList.as_view(), name='clientList'),
	path('<int:pk>/', login_required(views.DetailView.as_view()) , name='detail'),
	path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
	path('clientCreate/', views.CreateView.as_view(), name='create'),
	path('clientDelete/<int:pk>/', views.DeleteView.as_view(), name='deleteClient'),
	path('<int:pk>/dealsCreate/', views.dealsCreateView.as_view(), name='dealsCreate'),
	path('<int:pk>/taskCreate/', views.taskCreateView.as_view(), name='taskCreateView'),
]