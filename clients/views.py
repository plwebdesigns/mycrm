from .models import Client
from deals.models import Deals
from task_manager.models import Tasks
from django.views import generic
from django.urls import reverse

# Create your views here.
class clientList(generic.ListView):
	template_name = 'clients/clientList.html'
	context_object_name = 'clients'
	paginate_by = 25

	def get_queryset(self):
		if self.request.method == 'GET' and self.request.GET:
			if 'id' in self.request.GET:
				if self.request.GET['id']:
					searchtxt = self.request.GET.get('id', None)
					return Client.objects.filter(id__icontains=searchtxt)

				if self.request.GET['last_name']:
					searchtxt_2 = self.request.GET.get('last_name', None)
					return Client.objects.filter(last_name__icontains=searchtxt_2)

				else:
					return Client.objects.order_by('id')

		else:
			return Client.objects.order_by('id')
		

class DetailView(generic.DetailView):
	model = Client
	template_name = 'clients/clientDetail.html'
	context_object_name = 'client'

	def get_context_data(self, **kwargs):
		    context = super(DetailView, self).get_context_data(**kwargs)
		    #Get slug(client id)
		    cid = self.kwargs['pk']
		    context['deal_list'] = Deals.objects.filter(client_id_id=cid)
		    context['task_list'] = Tasks.objects.filter(client_id=cid)
		    return context

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


class dealsCreateView(generic.CreateView):
	model = Deals
	fields = '__all__'
	template_name_suffix = '_create_form'
	

	def get_context_data(self, **kwargs):
		context = super(dealsCreateView, self).get_context_data(**kwargs)
		cid = self.kwargs['pk']
		context['cid'] = cid
		context['client'] = Client.objects.get(id=cid)
		return context

	def get_success_url(self, **kwargs):
		return reverse('clients:detail', kwargs = {'pk': self.object.client_id_id})

	

class taskCreateView(generic.CreateView):
	model = Tasks
	fields = '__all__'
	template_name = 'tasks/task_create_form.html'

	def get_context_data(self, **kwargs):
		context = super(taskCreateView, self).get_context_data(**kwargs)
		cid = self.kwargs['pk']
		context['cid'] = cid
		context['client'] = Client.objects.get(id=cid)

		return context

	def get_success_url(self, **kwargs):
		return reverse('clients:detail', kwargs = {'pk': self.object.client_id_id})
