# Generated by Django 3.2.20 on 2023-09-04 07:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("migmig", "0002_alter_flightdetails_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flightdetails",
            name="traveler_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
    ]
