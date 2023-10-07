from django import forms
from .models import FlightDetails


class AddFlightForm(forms.ModelForm):
    """
    Class for posting traveler and flight details
    """

    # source for adding dropdown list to the form: \
    # http://www.learningaboutelectronics.com/Articles/\
    # How-to-create-a-drop-down-list-in-a-Django-form.php
    CHOICES_ORIGIN = [
        ("", "Select origin airport"),
        ("Germany International Airport 1", "Germany International Airport 1"),
        ("England International Airport 2", "England International Airport 2"),
        ("France International Airport 3", "France International Airport 3"),
        ("USA International Airport 3", "USA International Airport 3"),
        ("China International Airport 3", "China International Airport 3"),
        ("Australia International Airport 3",) * 2,
        ("Brazil International Airport 1", "Brazil International Airport 1"),
        (
            "South Africa International Airport 2",
            "South Africa International Airport 2",
        ),
        ("Nigeria International Airport 3", "Nigeria International Airport 3"),
    ]

    CHOICES_DESTINATION = [
        ("", "Select destination airport"),
        ("Germany International Airport 1", "Germany International Airport 1"),
        ("England International Airport 2", "England International Airport 2"),
        ("France International Airport 3", "France International Airport 3"),
        ("USA International Airport 3", "USA International Airport 3"),
        ("China International Airport 3", "China International Airport 3"),
        ("Australia International Airport 3",) * 2,
        ("Brazil International Airport 1", "Brazil International Airport 1"),
        (
            "South Africa International Airport 2",
            "South Africa International Airport 2",
        ),
        ("Nigeria International Airport 3", "Nigeria International Airport 3"),
    ]

    origin = forms.ChoiceField(
        choices=CHOICES_ORIGIN,
        label="From",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    destination = forms.ChoiceField(
        choices=CHOICES_DESTINATION,
        label="To",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = FlightDetails
        fields = [
            "origin",
            "destination",
            "flight_date",
            "weight_capacity",
            "fname",
            "lname",
            "address",
            "mobile_number",
            "email",
            "traveler_image",
        ]
        labels = {
            "fname": "Traveler's First Name",
            "lname": "Traveler's Last Name",
            "address": "Address",
            "mobile_number": "Mobile Number",
            "email": "Email",
            "traveler_image": "Traveler's Image",
            "flight_date": "Flight Date",
            "weight_capacity": "Weight Capacity",
        }
        widgets = {
            "fname": forms.TextInput(attrs={"placeholder": "First Name"}),
            "lname": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "address": forms.TextInput(attrs={"placeholder": "Address"}),
            "mobile_number": forms.TextInput(
                attrs={"placeholder": "Mobile Number"}
                ),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "origin": forms.TextInput(),
            "destination": forms.TextInput(),
            "flight_date": forms.DateInput(attrs={"type": "date"}),
            "weight_capacity": forms.NumberInput(
                attrs={"placeholder": "Weight Capacity (kg)"}
            ),
        }
