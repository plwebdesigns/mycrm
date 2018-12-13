from django.db import models
from employees.models import Employee
from clients.models import Client


class Deals(models.Model):
    id = models.AutoField(primary_key=True),
    client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
    employee_id = models.ForeignKey(Employee, on_delete=models.PROTECT)
    gross_amount = models.DecimalField(max_digits=12, decimal_places=2)
    net_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payments_purchased = models.IntegerField()

    def __str__(self):
        template = '{0.id} --${0.gross_amount}'
        return template.format(self)