from django.shortcuts import render

# Create your views here.
def createEmployee(request):
    return render(request, 'employees/createEmployee.html')

def empList(request):
	return render(request, 'employees/employeeList.html')