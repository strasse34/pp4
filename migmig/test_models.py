from django.test import TestCase
from django.contrib.auth.models import User
from .models import FlightDetails

class FlightDetailsModelTestCase(TestCase):
    """
    Class for testing FlightDetailModel to get flight and travelers' details
    """
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_flight_details_creation(self):
        # Create a FlightDetails object
        flight = FlightDetails.objects.create(
            traveler=self.user,
            origin='Origin Airport',
            destination='Destination Airport',
            flight_date='2023-09-10',
            weight_capacity=25.00,
            slug='testuser-reza-mirzaie-origin-airport-destination-airport-2023-09-10',
            fname='reza',
            lname='mirzaie',
            mobile_number='123-456-7890',
            address='123 Main St',
            email='test@example.com'
        )

        # Retrieve the flight details from the database
        saved_flight = FlightDetails.objects.get(pk=flight.pk)

        # Check if the retrieved object matches the created object
        self.assertEqual(saved_flight.traveler, self.user)
        self.assertEqual(saved_flight.origin, 'Origin Airport')
        self.assertEqual(saved_flight.destination, 'Destination Airport')
        self.assertEqual(str(saved_flight.flight_date), '2023-09-10')
        self.assertEqual(saved_flight.weight_capacity, 25.00)
        self.assertEqual(saved_flight.slug, 'testuser-reza-mirzaie-origin-airport-destination-airport-2023-09-10')
        self.assertEqual(saved_flight.fname, 'reza')
        self.assertEqual(saved_flight.lname, 'mirzaie')
        self.assertEqual(saved_flight.mobile_number, '123-456-7890')
        self.assertEqual(saved_flight.address, '123 Main St')
        self.assertEqual(saved_flight.email, 'test@example.com')
