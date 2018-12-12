from .models import Employee
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
	template_name = 'employees/employeeList.html'
	context_object_name = 'employees'
	paginate_by = 62

	def get_queryset(self):
		return Employee.objects.order_by('id')
	

class DetailView(generic.DeleteView):
	model = Employee
	template_name = 'employees/detail.html'
	

class UpdateView(generic.UpdateView):
	model = Employee
	fields = '__all__'
	success_url = '/employeeList/'
	
		
class CreateView(generic.CreateView):
		model = Employee
		fields = '__all__'
		template_name_suffix = '_create_form'
		success_url = '/employeeList/'

class DeleteView(generic.DeleteView):
	model = Employee
	success_url = '/employeeList/'
						