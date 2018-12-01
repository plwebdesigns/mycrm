from django.shortcuts import render, redirect
from django.contrib.auth.views import login, logout, authenticate

# Create your views here.
def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('clientList/', request.POST['next'])
		else:
			return render(request,'accounts/login.html')

	else:
		return render(request, 'accounts/login.html')


def logout_view(request):
	logout(request)
	return redirect('clientList/')

