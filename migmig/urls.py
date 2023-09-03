from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('add_flight/', views.AddFlightView.as_view(), name='add_flight'),
    path('my_flight/', views.MyFlightsView.as_view(), name='my_flights'),
    path('<slug:slug>/', views.TravelerContactView.as_view(), name='traveler_contact'),
]