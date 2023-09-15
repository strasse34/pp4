from django import forms
from .models import FlightDetails

class AddFlightForm(forms.ModelForm):
    CHOICES = [
        ('', 'Select Airport'),
        ('Germany International Airport 1', 'Germany International Airport 1'),
        ('England International Airport 2', 'England International Airport 2'),
        ('France International Airport 3', 'France International Airport 3'),
        ('USA International Airport 3', 'USA International Airport 3'),
        ('China International Airport 3', 'China International Airport 3'),
        ('Australia International Airport 3', 'Australia International Airport 3'),
        ('Brazil International Airport 1', 'Brazil International Airport 1'),
        ('South Africa International Airport 2', 'South Africa International Airport 2'),
        ('Nigeria International Airport 3', 'Nigeria International Airport 3'),
    ]

    origin = forms.ChoiceField(choices=CHOICES, label='', widget=forms.Select(attrs={'class': 'form-control'}))
    destination = forms.ChoiceField(choices=CHOICES, label='', widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = FlightDetails
        fields = [
            'fname',
            'lname',
            'address',
            'mobile_number',
            'email',
            'traveler_image',
            'origin',
            'destination',
            'flight_date',
            'weight_capacity',
        ]
        labels = {
            'fname': '',  
            'lname': '',
            'address': '',
            'mobile_number': '',
            'email': '',
            'traveler_image': "Traveler's Image",
            'origin': '',
            'destination': '',
            'flight_date': '',
            'weight_capacity': '',
        }
        widgets = {
            'fname': forms.TextInput(attrs={'placeholder': "First Name"}),
            'lname': forms.TextInput(attrs={'placeholder': "Last Name"}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'origin': forms.TextInput(attrs={'placeholder': 'Select Flight Origin'}),
            'destination': forms.TextInput(attrs={'placeholder': 'Select Flight Destination'}),
            'flight_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Flight Date' }),
            'weight_capacity': forms.NumberInput(attrs={'placeholder': 'Weight Capacity (kg)'}),
        }



