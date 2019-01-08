from .models import Employee
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
	template_name = 'employees/employeeList.html'
	context_object_name = 'employees'
	paginate_by = 62

	def get_queryset(self):
		if self.request.method == 'GET' and self.request.GET:
			if 'first_name' in self.request.GET:
				if self.request.GET['first_name']:
					searchtxt = self.request.GET.get('first_name', None)
					return Employee.objects.filter(first_name__icontains=searchtxt)

				if self.request.GET['last_name']:
					searchtxt_2 = self.request.GET.get('last_name', None)
					return Employee.objects.filter(last_name__icontains=searchtxt_2)

				else:
					return Employee.objects.order_by('id')

		else:
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
						