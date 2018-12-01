from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
	path('', views.clientList, name='clientList'),
	path('<int:cid>/', views.detail, name='detail'),
	path('clientCreate/', views.create, name='create'),
]