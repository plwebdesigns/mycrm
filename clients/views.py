from django.shortcuts import render, get_object_or_404, redirect
from clients.models import Client
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/accounts/login/')
def clientList(request):
	obj = Client.objects.all()[:50]
	return render(request, 'clients/clientList.html', {'clients': obj})

@login_required(login_url = '/accounts/login/')
def detail(request, cid):
	client = get_object_or_404(Client, pk=cid)
	if request.method == 'POST':
		client.first_name = request.POST['first_name']
		client.last_name = request.POST['last_name']
		client.address_1 = request.POST['address_1']
		client.address_2 = request.POST['address_2']
		client.city = request.POST['city']
		client.state = request.POST['state']
		client.zipcode = request.POST['zipcode']
		client.phone_1 = request.POST['phone_1']
		client.phone_2 = request.POST['phone_2']
		client.phone_3 = request.POST['phone_3']
		client.phone_4 = request.POST['phone_4']
		client.dob = request.POST['dob']
		client.ssn = request.POST['ssn']
		client.notes = request.POST['notes']
		client.save()
		

		return redirect('/clientList/' + str(cid))

	else:
		return render(request, 'clients/clientDetail.html', {'client': client})

