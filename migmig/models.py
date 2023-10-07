from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
import datetime
from decimal import Decimal

STATUS = ((1, "Active"), (0, "Archived"))


class FlightDetails(models.Model):
    """
    Class for recording flight details in database
    """

    traveler = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="traveler"
    )
    traveler_image = CloudinaryField("image")
    origin = models.CharField(max_length=200, blank=None)
    destination = models.CharField(max_length=200, blank=None)
    flight_date = models.DateField()
    weight_capacity = models.DecimalField(
        max_digits=4, decimal_places=2, blank=None
        )
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=1)
    fname = models.CharField(max_length=50, blank=None)
    lname = models.CharField(max_length=50, blank=None)
    mobile_number = models.CharField(max_length=14, blank=None)
    address = models.CharField(max_length=200, blank=None)
    email = models.EmailField(blank=None)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f" from {self.origin} to {self.destination}"

    # Source: https://studygyaan.com/django/
    # how-to-create-a-unique-slug-in-django
    def save(self, *args, **kwargs):
        part_1 = f"{self.traveler}-{self.fname}-{self.lname}"
        part_2 = f"{self.origin}-{self.destination}-{self.flight_date}"
        slug_source = part_1 + part_2
        self.slug = slugify(slug_source)
        super(FlightDetails, self).save(*args, **kwargs)
