# Generated by Django 2.0.7 on 2018-11-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20181126_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(max_length=30),
        ),
    ]
