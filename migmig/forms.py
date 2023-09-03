from django import forms
from .models import FlightDetails

class AddFlightForm(forms.ModelForm):
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


