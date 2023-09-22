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
from django.db.models import Q


class ContextMixin:
    """
    Class for retrieving username and converting status
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

    def status_convertor(self):
        """
        Converting status of the cards from 1 to 0
        """
        current_date = timezone.now().date()
        outdated_flight = FlightDetails.objects.filter(status=1)
        
        for flight in outdated_flight:
            formatted_flight_date = flight.flight_date.strftime('%d-%m-%Y')
            
            if formatted_flight_date == current_date.strftime('%d-%m-%Y'):
                flight.status = 0
                flight.save()
                
                


class HomeView(ContextMixin, generic.ListView):
    """
    Class for displaying flight information to the public site visitor
    """
    model = FlightDetails
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6

    def get_queryset(self):
        queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
        airport_list = self.request.GET.get('origin')  

        if airport_list:
            queryset = queryset.filter(origin=airport_list)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Retrieving airports' choices from form for displaying in the search bar dropdown list 
        """
        context = super().get_context_data(**kwargs)
        context['choices'] = AddFlightForm.CHOICES_ORIGIN[1:]  
        return context



class AddFlightView(LoginRequiredMixin, ContextMixin, CreateView):
    """
    Class for posting travelers infor and flight details to the database
    """
    model = FlightDetails
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    queryset = FlightDetails.objects.all()
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Check if a flight with the same attributes already exists
        """
        form.instance.traveler = self.request.user
        existing_flight = FlightDetails.objects.filter(
            traveler=form.instance.traveler,
            fname=form.cleaned_data['fname'],
            lname=form.cleaned_data['lname'],
            origin=form.cleaned_data['origin'],
            destination=form.cleaned_data['destination'],
            flight_date=form.cleaned_data['flight_date'],
        ).first()

        if existing_flight:
            messages.error(self.request, "You have already posted this flight.")
            return self.form_invalid(form)

        flight_date = form.cleaned_data['flight_date']

        if flight_date > timezone.now().date():
            if form.cleaned_data['origin'] != form.cleaned_data['destination']:
                return super(AddFlightView, self).form_valid(form)
            else:
                messages.error(self.request, "Origin airport and destination airport cannot be the same.")
                return self.form_invalid(form)
        else:
            messages.error(self.request, "Flight date must be in the future.")
            return self.form_invalid(form)

        

class MyFlightsView(LoginRequiredMixin, ContextMixin, generic.ListView):
    """
    Class to retrive all the user's flight details which have been already recorded in the database
    including active and archived cards
    """
    model = FlightDetails  
    template_name = 'my_flight.html'  
    queryset = FlightDetails.objects.all().order_by("-created_on")
    paginate_by = 6

    def get_queryset(self):
        queryset = FlightDetails.objects.filter(
            traveler__id=self.request.user.id).order_by('-created_on')
        return queryset
    


class TravelerContactView(LoginRequiredMixin, ContextMixin, View):
    """
    Class to show all traveler info and flight details to requesters
    """
    def get(self, request, slug, *arg, **kwargs):
        queryset = FlightDetails.objects.filter(status=1)
        flightinfo = get_object_or_404(queryset, slug=slug)
        return render(request, "traveler_contact.html", {"flightinfo": flightinfo})


class EditFlightView(LoginRequiredMixin, ContextMixin, UpdateView):
    """
    Class to edit traveler info and flight details and save them to database
    """
    model = FlightDetails
    form_class = AddFlightForm
    success_url = reverse_lazy('my_flights')
    
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        form = self.form_class(instance=flight_details)
        return render(request, 'edit_flight.html', {'flight_details': flight_details, 'form': form})

    def form_valid(self, form):
        form.instance.traveler = self.request.user
        flight_details = self.object 
        flight_details.is_updated = True
        flight_details.save()
        form.save()
        messages.success(self.request, "Your flight details were updated successfully")
        return super().form_valid(form)



class DeleteFlightView(LoginRequiredMixin, ContextMixin, View):
    """
    Class to delete traveler info and flight details from database
    """
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'delete_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.delete()
        messages.success(request, "Flight details deleted successfully")
        return redirect('my_flights')



class ArchiveFlightView(LoginRequiredMixin, ContextMixin, View):
    """
    Class to archive traveler info and flight details
    """
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'archive_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.status = 0
        flight_details.save()
        messages.success(request, "Flight details archived successfully")
        return redirect('my_flights')


 