from django.shortcuts import render, get_object_or_404
from clients.models import Client

# Create your views here.
def clientList(request):
	obj = Client.objects.all()[:50]
	return render(request, 'clients/clientList.html', {'clients': obj})


def detailView(request, id_client):
	obj = get_object_or_404(Client, pk=id_client)
	return render(request, 'clients/clientDetail.html', {'client': obj})