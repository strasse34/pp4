from django.contrib import admin
from .models import FlightDetails

@admin.register(FlightDetails)
class FlightCardAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('traveler', 'origin', 'destination')}
    list_display = ('traveler', 'origin', 'destination', 'created_on', 'updated_on')
    search_fields = ['origin', 'destination']
    list_filter = ('origin', 'destination')