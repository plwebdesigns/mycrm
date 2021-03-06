# Generated by Django 2.1.3 on 2018-12-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('address_1', models.CharField(max_length=150)),
                ('address_2', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zipcode', models.CharField(max_length=30)),
                ('phone_1', models.CharField(max_length=30)),
                ('phone_2', models.CharField(max_length=30)),
                ('phone_3', models.CharField(max_length=30)),
                ('phone_4', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('ssn', models.CharField(max_length=30)),
                ('notes', models.CharField(max_length=400)),
            ],
        ),
    ]
