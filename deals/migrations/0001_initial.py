# Generated by Django 2.0.7 on 2018-12-13 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_auto_20181209_1746'),
        ('employees', '0002_auto_20181212_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payments_purchased', models.IntegerField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Employee')),
            ],
        ),
    ]
