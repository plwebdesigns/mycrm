from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('clientList/' request.POST['next'])
		else:
			error_message='Please login first'
			return render(request,'accounts/login.html')

	else:
		return render(request, 'accounts/login.html')


def logout_view(request):
	logout(request)
	return render(request, 'accounts/login.html')