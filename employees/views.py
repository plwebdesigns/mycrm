from .models import Employee
from django.views import generic
from django.contrib.auth.models import User
import random


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

	def form_valid(self, form):
		uname = 'temp' + str(random.randint(1,10000))
		usr = User.objects.create_user(uname, email=None, password='password1234')
		usr.first_name = self.request.POST['first_name']
		usr.last_name =  self.request.POST['last_name']
		usr.username = uname + usr.last_name
		usr.is_staff = True
		usr.save()

		return super(CreateView, self).form_valid(form)




class DeleteView(generic.DeleteView):
	model = Employee
	success_url = '/employeeList/'
						