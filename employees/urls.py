from django.urls import path
from . import views

app_name = 'employees'
urlpatterns = [
    path('', views.IndexView.as_view(), name='employeeList'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/editEmployee', views.UpdateView.as_view(), name='update'),
    path('employeeCreate/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]