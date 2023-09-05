from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic, View
from .forms import AddFlightForm
from .models import FlightDetails
from django.urls import reverse_lazy
from datetime import datetime
from django.contrib import messages
from django.utils import timezone


class ContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username  
        return context

    def status_convertor(self):
        current_date = timezone.now().date()
        outdated_flight = FlightDetails.objects.filter(flight_date__lt=current_date, status=1)
        outdated_flight.update(status=0)


class HomeView(ContextMixin, generic.ListView):
    model = FlightDetails  
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6

    def status_convertor(self):
        current_date = timezone.now().date()
        outdated_flight = FlightDetails.objects.filter(flight_date__lt=current_date, status=1)
        outdated_flight.update(status=0)


class AddFlightView(LoginRequiredMixin, ContextMixin, CreateView):
    model = FlightDetails
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    queryset = FlightDetails.objects.all()
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.traveler = self.request.user  
        flight_date = form.cleaned_data['flight_date']
        if flight_date > timezone.now().date():
            return super(AddFlightView, self).form_valid(form)
        else:
            messages.error(self.request, "Flight date must be in the future.")
            return self.form_invalid(form)
        

class MyFlightsView(LoginRequiredMixin, ContextMixin, generic.ListView):
    model = FlightDetails  
    template_name = 'my_flight.html'  
    queryset = FlightDetails.objects.all().order_by("-created_on")
    paginate_by = 6

    def get_queryset(self):
        queryset = FlightDetails.objects.filter(
            traveler__id=self.request.user.id).order_by('-created_on')
        return queryset
    


class TravelerContactView(LoginRequiredMixin, ContextMixin, View):
    def get(self, request, slug, *arg, **kwargs):
        queryset = FlightDetails.objects.filter(status=1)
        flightinfo = get_object_or_404(queryset, slug=slug)

        return render(request, "traveler_contact.html", {"flightinfo": flightinfo})


class EditFlightView(LoginRequiredMixin, ContextMixin, UpdateView):
    
    model = FlightDetails
    form_class = AddFlightForm
    template_name = 'edit_flight.html'
    success_url = reverse_lazy('my_flights')

    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = "Your flight details was updated successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(EditFlightsView, self).form_valid(form)


class DeleteFlightView(LoginRequiredMixin, ContextMixin, DeleteView):
    
    model = FlightDetails
    template_name = 'delete_fight.html'
    success_url = reverse_lazy('my_flights')

    def delete(self, request, *args, **kwargs):
        msg = "Your flight has been deleted"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(DeleteFlightsView, self).delete(request, *args, **kwargs)