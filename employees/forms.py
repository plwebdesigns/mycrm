from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
	first_name = forms.CharField(max_length=80, required=False)
	last_name = forms.CharField(max_length=80, required=False)
	address_1 = forms.CharField(max_length=150, required=False)
	address_2 = forms.CharField(max_length=150, required=False)
	city = forms.CharField(max_length=30, required=False)
	state = forms.CharField(max_length=30, required=False)
	zipcode = forms.CharField(max_length=30, required=False)
	phone_1 = forms.CharField(max_length=30, required=False)
	phone_2 = forms.CharField(max_length=30, required=False)
	phone_3 = forms.CharField(max_length=30, required=False)
	phone_4 = forms.CharField(max_length=30, required=False)
	dob = forms.CharField(max_length=30, required=False)
	ssn = forms.CharField(max_length=30, required=False)
	department = forms.CharField(max_length=30, required=False)
	manager = forms.CharField(max_length=30, required=False)
	Salary = forms.CharField(max_length=30, required=False)
	
	class Meta:
		model = Employee
		fields = '__all__'