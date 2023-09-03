from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path('add_flight/', views.AddFlightView.as_view(), name='add_flight'),
]