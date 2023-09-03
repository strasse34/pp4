from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.edit import CreateView
from django.views import generic, View
from .forms import AddFlightForm
from .models import FlightDetails
from django.urls import reverse_lazy


class HomeView(generic.ListView):
    model = FlightDetails  
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username  
        return context


class AddFlightView(LoginRequiredMixin, CreateView):
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.traveler = self.request.user  
        form.save()
        return super(AddFlightView, self).form_valid(form)
        

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
        queryset = FlightDetails.objects.all(status=1)
        flightinfo = get_object_or_404(queryset, slug=slug)

        return render(request, "traveler_contact.html", {"flightinfo": flightinfo})

    