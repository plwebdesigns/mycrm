from django.contrib.auth import views as auth_views
from django.urls import path



app_name = 'accounts'
urlpatterns = [
	path('accounts/login/', auth_views.LoginView(template_name='accounts/login.html')),
	path('accounts/logout/', auth_views.LogoutView(template_name='accounts/loggedout.html')),
]