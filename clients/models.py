from django.db import models
from django.urls import reverse

# Create your models here.
class Client (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=80, blank=True)
    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=30, blank=True)
    phone_1 = models.CharField(max_length=30, blank=True)
    phone_2 = models.CharField(max_length=30, blank=True)
    phone_3 = models.CharField(max_length=30, blank=True)
    phone_4 = models.CharField(max_length=30, blank=True)
    dob = models.CharField(max_length=30, blank=True)
    ssn = models.CharField(max_length=30, blank=True)
    notes = models.CharField(max_length=400, blank=True)

    def __str__(self):
        template = '{0.last_name} {0.first_name}'
        return template.format(self)
        