from django.shortcuts import render, get_object_or_404, redirect
from clients.models import Client
from django.contrib.auth.decorators import login_required
from .forms import createForm
from django.views import generic

# Create your views here.
class clientList(generic.ListView):
	template_name = 'clients/clientList.html'
	context_object_name = 'clients'
	paginate_by = 51

	def get_queryset(self):
		if self.request.method == 'GET' and self.request.GET:
			if 'last_name' in self.request.GET:
				if self.request.GET['last_name']:
					searchtxt = self.request.GET.get('last_name', None)
					return Client.objects.filter(last_name__icontains=searchtxt)
				else:
					return Client.objects.order_by('id')
		else:
			return Client.objects.order_by('id')
		

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


def create(request):
	if request.method == 'POST':
		form = createForm(request.POST)
		form.save()
		return redirect('/clientCreate/')

	else:
		form = createForm()
		return render(request, 'clients/clientCreate.html', {'form': form})

def deleteClient(request, cid):
	obj = get_object_or_404(Client, pk=cid)
	if request.method == 'POST':
		obj.delete()

		return redirect('/clientList/')

	return render(request, 'clients/clientDelete.html', {'obj': obj})
