from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import FlightDetails

class FlightDetailsViewTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test flight
        self.flight = FlightDetails.objects.create(
            traveler=self.user,
            origin='Origin Airport',
            destination='Destination Airport',
            flight_date='2023-09-10',
            weight_capacity=25.00,
            fname='John',
            lname='Doe',
            mobile_number='1234567890',
            address='Test Address',
            email='test@example.com'
        )

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.flight = FlightDetails.objects.create(
        traveler=self.user,
        origin='Origin Value',  
        destination='Destination Value',  
        flight_date='2023-09-10', 
        fname='First Name',  
        lname='Last Name',  
        weight_capacity=42.0,
        address= 'Berlin Street 23',  
    )
        self.client.login(username='testuser', password='testpassword')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        

    def test_add_flight_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_flight'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_flight.html')
        

    def test_my_flights_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('my_flights'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_flight.html')
        

    def test_traveler_contact_view(self):
        response = self.client.get(reverse('traveler_contact', args=[self.flight.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'traveler_contact.html')
        

    