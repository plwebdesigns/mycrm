from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'deals'
urlpatterns = [
	path('', views.DealsListView.as_view(), name='dealsList'),
]