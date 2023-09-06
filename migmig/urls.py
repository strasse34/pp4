from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('add_flight/', views.AddFlightView.as_view(), name='add_flight'),
    path('my_flight/', views.MyFlightsView.as_view(), name='my_flights'),
    path('edit_flight/<slug>/', views.edit_flight, name='edit_flight'),
    path('delete_flight/<slug:slug>/', views.DeleteFlightView.as_view(), name='delete_flight'),
    path('<slug:slug>/', views.TravelerContactView.as_view(), name='traveler_contact'),
]