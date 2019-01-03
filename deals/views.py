from django.views import generic
from .models import Deals

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


class DealsUpdateView(generic.UpdateView):
	model = Deals
	fields = '__all__'
	success_url = '/clientList'
		

class DealsDeleteView(generic.DeleteView):
	model = Deals
	success_url = '/clientList'
	context_object_name = 'deal'
		