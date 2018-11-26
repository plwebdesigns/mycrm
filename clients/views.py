from django.shortcuts import render, get_object_or_404
from clients.models import Client

# Create your views here.
def clientList(request):
	obj = Client.objects.all()[:50]
	return render(request, 'clients/clientList.html', {'clients': obj})


def detail(request, cid):
	objClient = get_object_or_404(Client, pk=cid)
	return render(request, 'clients/clientDetail.html', {'client': objClient})


	