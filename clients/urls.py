from django.urls import path
from . import views


urlpatterns = [
	path('', views.clientList, name='clientList'),
	path('', views.detailView, name='detailView'),
]