# Generated by Django 2.0.7 on 2019-01-06 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0002_auto_20181212_1627'),
        ('clients', '0002_auto_20181209_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_due', models.DateField()),
                ('summary', models.CharField(max_length=500)),
                ('attachment', models.FileField(upload_to='uploads/%y/%m/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.Client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Employee')),
            ],
        ),
    ]
