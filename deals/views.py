from django.views import generic
from .models import Deals

# Create your views here.
class DealsListView(generic.ListView):
	template_name = 'deals/dealsList.html'
	context_object_name = 'deals'
	paginate_by = 53

	def get_queryset(self):
		return Deals.objects.all()