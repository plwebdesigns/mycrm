from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'deals'
urlpatterns = [
	path('', views.DealsListView.as_view(), name='dealsList'),
	path('<int:pk>/', views.DealsDetailView.as_view(), name='DealsDetailView'),
	path('<int:pk>/updateDeal/', views.DealsUpdateView.as_view(), name='DealsUpdateView'),
	path('<int:pk>/deleteDeal/', views.DealsDeleteView.as_view(), name='DealsDeleteView'),
]