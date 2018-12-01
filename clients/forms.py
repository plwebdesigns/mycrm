from django import forms
from .models import Client

class createForm(forms.ModelForm):
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
	notes = forms.CharField(max_length=400, required=False)
	
	class Meta:
		model = Client
		fields = '__all__'
	
