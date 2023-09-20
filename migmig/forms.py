from django import forms
from .models import FlightDetails

class AddFlightForm(forms.ModelForm):
    CHOICES_ORIGIN = [
        ('', 'Select origin airport'),
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

    CHOICES_DESTINATION = [
        ('', 'Select destination airport'),
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

    origin = forms.ChoiceField(choices=CHOICES_ORIGIN, label='', widget=forms.Select(attrs={'class': 'form-control'}))
    destination = forms.ChoiceField(choices=CHOICES_DESTINATION, label='', widget=forms.Select(attrs={'class': 'form-control'}))
    


    class Meta:
        model = FlightDetails
        fields = [
            'origin',
            'destination',
            'flight_date',
            'weight_capacity',
            'fname',
            'lname',
            'address',
            'mobile_number',
            'email',
            'traveler_image',
            
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
            'fname': forms.TextInput(attrs={'placeholder': "Traveler First Name"}),
            'lname': forms.TextInput(attrs={'placeholder': "Traveler Last Name"}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'origin': forms.TextInput(),
            'destination': forms.TextInput(),
            'flight_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Flight Date' }),
            'weight_capacity': forms.NumberInput(attrs={'placeholder': 'Weight Capacity (kg)'}),
        }



