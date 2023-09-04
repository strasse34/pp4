from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views import generic, View
from .forms import AddFlightForm
from .models import FlightDetails
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages


class HomeView(generic.ListView):
    model = FlightDetails  
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username  
        return context

    def status_changer(self, flight_date):
        current_date = datetime.now().strftime("%Y-%m-%d")
        flight_date = flight_date.strftime("%Y-%m-%d")
        if current_date >= flight_date:
            status=0
        return status


class AddFlightView(LoginRequiredMixin, CreateView):
    model = FlightDetails
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    queryset = FlightDetails.objects.all()
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.traveler = self.request.user  
        form.save()
        return super(AddFlightView, self).form_valid(form)

    def invalid_date(self, flight_date):
        current_date = datetime.now().strftime("%Y-%m-%d")
        flight_date = flight_date.strftime("%Y-%m-%d")
        if current_date >= flight_date:
            msg = "Invalid Flight Date"
            messages.add_message(self.request, messages.WARNING, msg)
        return self.template_name
        

class MyFlightsView(generic.ListView):
    model = FlightDetails  
    template_name = 'my_flight.html'  
    queryset = FlightDetails.objects.all().order_by("-created_on")
    paginate_by = 6

    def get_queryset(self):
        queryset = FlightDetails.objects.filter(
            traveler__id=self.request.user.id).order_by('-created_on')
        return queryset


class TravelerContactView(View):
   
    def get(self, request, slug, *arg, **kwargs):
        queryset = FlightDetails.objects.filter(status=1)
        flightinfo = get_object_or_404(queryset, slug=slug)

        return render(request, "traveler_contact.html", {"flightinfo": flightinfo})

    