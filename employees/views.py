from django.shortcuts import render, get_object_or_404, get_list_or_404
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
		