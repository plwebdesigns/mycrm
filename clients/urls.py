from django.urls import path
from . import views


urlpatterns = [
	path('', views.clientList, name='clientList'),
	path('<int:id_client>/', views.detailView, name='detailView'),
]