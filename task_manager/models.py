from django.db import models
from employees.models import Employee
from clients.models import Client

# Create your models here.
class Tasks(models.Model):
	STATUS_CHOICES = (
			('processing', 'Processing'),
			('completed', 'Completed'),
			('attention', 'Needs Attention'),
			('research', 'Research'),
		)
	id = models.AutoField(primary_key=True)
	client = models.ForeignKey(Client, on_delete=models.PROTECT)
	employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
	status = models.CharField(max_length=100, choices=STATUS_CHOICES)
	department = models.CharField(max_length=100)
	date_created = models.DateField(auto_now=True)
	date_due = models.DateField(auto_now=False)
	summary = models.CharField(max_length=500, blank=True)
	attachment = models.FileField(upload_to='uploads/%y/%m/', blank=True)
