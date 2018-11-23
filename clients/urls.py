from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
	path('', views.clientList, name='clientList'),
	path('<int:id_client>/', views.detailView, name='detailView'),
]