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
    paginate_by = 8

    def get_queryset(self):
        queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
        airport_list = self.request.GET.get('origin')  # Use airport_list consistently

        if airport_list:
            queryset = queryset.filter(origin=airport_list)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = AddFlightForm.CHOICES[1:]  # Exclude the 'Placeholder' choice
        return context



class AddFlightView(LoginRequiredMixin, ContextMixin, CreateView):
    model = FlightDetails
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    queryset = FlightDetails.objects.all()
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Check if a flight with the same attributes already exists
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
    success_url = reverse_lazy('my_flights')
    
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        form = self.form_class(instance=flight_details)
        return render(request, 'edit_flight.html', {'flight_details': flight_details, 'form': form})

    def form_valid(self, form):
        form.instance.traveler = self.request.user
        form.save()
        messages.success(self.request, "Your flight details were updated successfully")
        return super().form_valid(form)



class DeleteFlightView(LoginRequiredMixin, ContextMixin, View):
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'delete_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.delete()
        messages.success(request, "Flight details deleted successfully")
        return redirect('my_flights')



class ArchiveFlightView(LoginRequiredMixin, ContextMixin, View):
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'archive_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.status = 0
        flight_details.save()
        messages.success(request, "Flight details archived successfully")
        return redirect('my_flights')


 