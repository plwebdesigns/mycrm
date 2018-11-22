from django.shortcuts import render
from clients.models import Client

# Create your views here.
def clientList(request):
	obj = Client.objects.all()[:50]
	return render(request, 'clients/clientList.html', {'clients': obj})


def detailView(request, lname):
	obj = Client.objects.filter(last_name=lname)
	return render(request, 'clients/clientDetail.html', {'clients': obj})