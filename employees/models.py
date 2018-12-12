from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    phone_1 = models.CharField(max_length=12, blank=True)
    phone_2 = models.CharField(max_length=12, blank=True)
    dob = models.CharField(max_length=12, blank=True)
    ssn = models.CharField(max_length=12, blank=True)
    department = models.CharField(max_length=80, blank=True)
    manager = models.CharField(max_length=80, blank=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
