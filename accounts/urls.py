from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
	path('accounts/login/', auth_views.LoginView(template_name='accounts/login.html')),
	path('indexapp/index/', auth_views.LogoutView(template_name='indexapp/index.html')),
]