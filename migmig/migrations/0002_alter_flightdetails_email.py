# Generated by Django 3.2.20 on 2023-09-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("migmig", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flightdetails",
            name="email",
            field=models.EmailField(blank=None, max_length=254),
        ),
    ]
