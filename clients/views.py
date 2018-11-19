from django.shortcuts import render

# Create your views here.
def clientList(request):
	return render(request, 'clients/clientList.html')