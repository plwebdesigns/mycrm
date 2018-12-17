from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
	path('', views.clientList.as_view(), name='clientList'),
	path('<int:cid>/', views.detail, name='detail'),
	path('clientCreate/', views.create, name='create'),
	path('clientDelete/<int:cid>/', views.deleteClient, name='deleteClient'),
]