from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.views import generic, View
from .forms import AddFlightForm
from .models import FlightDetails

class AddFlightView(LoginRequiredMixin, FormView):
    model = FlightDetails
    template_name = 'add_flight.html'  
    form_class = AddFlightForm
    success_url = 'home'  

    def form_valid(self, form):
        form.instance.traveler = self.request.user  
        form.save()
        return super().form_valid(form)




class HomeView(generic.ListView):
    model = FlightDetails  
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username  
        return context