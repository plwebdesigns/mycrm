from .models import Tasks
from django.views import generic

# Create your views here.
class TaskList(generic.ListView):
	template_name = 'tasks/taskList.html'
	context_object_name = 'tasks'
	paginate_by = 25

	def get_queryset(self):
		if self.request.method == 'GET' and self.request.GET:
			if 'id' in self.request.GET:
				if self.request.GET['id']:
					searchtxt = self.request.GET.get('id', None)
					return Tasks.objects.filter(id__icontains=searchtxt)

				if self.request.GET['last_name']:
					searchtxt_2 = self.request.GET.get('last_name', None)
					return Tasks.objects.filter(last_name__icontains=searchtxt_2)

				else:
					return Tasks.objects.order_by('id')

		else:
			return Tasks.objects.order_by('id')