# Generated by Django 3.2.20 on 2023-09-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migmig', '0005_auto_20230909_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdetails',
            name='destination',
            field=models.CharField(blank=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='flightdetails',
            name='origin',
            field=models.CharField(blank=None, max_length=200),
        ),
    ]
