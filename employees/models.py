from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    phone_1 = models.CharField(max_length=12)
    phone_2 = models.CharField(max_length=12)
    dob = models.CharField(max_length=12)
    ssn = models.CharField(max_length=12)
    department = models.CharField(max_length=80)
    manager = models.CharField(max_length=80)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
