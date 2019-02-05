from django.views import generic
from .models import Deals
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class DealsListView(generic.ListView):
	template_name = 'deals/dealsList.html'
	context_object_name = 'deals'
	paginate_by = 53

	def get_queryset(self):
		return Deals.objects.all()


class DealsDetailView(generic.DetailView):
	model = Deals
	template_name = 'deals/DealsDetail.html'
	context_object_name = 'deal'


class DealsUpdateView(PermissionRequiredMixin, generic.UpdateView):
	model = Deals
	fields = '__all__'
	success_url = '/clientList'
	permission_required = 'clients.change_client'
		

class DealsDeleteView(PermissionRequiredMixin, generic.DeleteView):
	model = Deals
	success_url = '/clientList'
	context_object_name = 'deal'
	permission_required = 'clients.delete_client'

		