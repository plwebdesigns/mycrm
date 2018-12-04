from django.urls import path
from . import views

urlpatterns = [
    path('', views.createEmployee, name='createEmployee'),
    path('employeeList/', views.empList, name='employeeList'),
]