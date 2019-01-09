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

class TaskDetail(generic.DetailView):
	model = Tasks
	template_name = 'tasks/taskDetail.html'
	context_object_name = 'task'


class TaskEdit(generic.UpdateView):
	model = Tasks
	fields = '__all__'
	success_url = '/taskList'
	template_name = 'tasks/task_edit_form.html'
	context_object_name = 'task'


class TaskDelete(generic.DeleteView):
	model = Tasks
	success_url = '/taskList'
	context_object_name = 'task'
	template_name = 'tasks/task_confirm_delete.html'		


		
		