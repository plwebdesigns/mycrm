from django.db import models

# Create your models here.
class Client (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    phone_1 = models.CharField(max_length=30)
    phone_2 = models.CharField(max_length=30)
    phone_3 = models.CharField(max_length=30)
    phone_4 = models.CharField(max_length=30)
    dob = models.CharField(max_length=30)
    ssn = models.CharField(max_length=30)
    notes = models.CharField(max_length=400)

    def __str__(self):
        template = '{0.last_name} {0.first_name}'
        return template.format(self)