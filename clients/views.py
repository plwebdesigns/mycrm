from clients.models import Client
from django.views import generic

# Create your views here.
class clientList(generic.ListView):
	template_name = 'clients/clientList.html'
	context_object_name = 'clients'
	paginate_by = 25

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

class DetailView(generic.DetailView):
	model = Client
	template_name = 'clients/clientDetail.html'
	context_object_name = 'client'

class UpdateView(generic.UpdateView):
	model = Client
	fields = '__all__'
	success_url = '/clientList'

class CreateView(generic.CreateView):
	model = Client
	fields = '__all__'
	template_name_suffix = '_create_form'
	success_url = '/clientList'

class DeleteView(generic.DeleteView):
	model = Client
	success_url = '/clientList'

