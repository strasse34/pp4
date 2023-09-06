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
        context['slug'] = self.kwargs.get('slug')  # Retrieve slug from URL
        return context

    def status_convertor(self):
        current_date = timezone.now().date()
        outdated_flight = FlightDetails.objects.filter(flight_date__lt=current_date, status=1)
        outdated_flight.update(status=0)

    def get_flight_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(FlightDetails, slug=slug)



class HomeView(ContextMixin, generic.ListView):
    model = FlightDetails  
    template_name = 'index.html'  
    queryset = FlightDetails.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6


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


# class EditFlightView(LoginRequiredMixin, ContextMixin, UpdateView):
#     model = FlightDetails
#     form_class = AddFlightForm
#     template_name = 'edit_flight.html'
#     success_url = reverse_lazy('my_flights')

#     def get_context_data(self, **kwargs):
#         context = super(EditFlightView, self).get_context_data(**kwargs)
#         context['flight_details'] = self.flight_details
#         return context

#     def form_valid(self, form):
#         form.instance.traveler = self.request.user
#         msg = "Your flight details were updated successfully"
#         messages.add_message(self.request, messages.SUCCESS, msg)
#         slug = self.kwargs['slug']
#         self.flight_details = FlightDetails.objects.get(slug=slug)
#         return super(EditFlightView, self).form_valid(form)
    
    
    
     
def edit_flight(request, slug):
    slug = FlightDetails.objects.get(slug=slug)
    form = AddFlightForm(request.POST or None, instance=slug)
    if form.is_valid():
        form.save()
        msg = "Your flight details were updated successfully"
        messages.success(request, msg)        
        return redirect('my_flights')
    return render(request, 'edit_flight.html', {'form': form, 'slug': slug})
    


class DeleteFlightView(View):
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'delete_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.delete()
        messages.success(request, "Flight details deleted successfully")
        return redirect('my_flights')



class ArchiveFlightView(View):
    def get(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        return render(request, 'archive_flight.html', {'flight_details': flight_details})

    def post(self, request, slug):
        flight_details = FlightDetails.objects.get(slug=slug)
        flight_details.status = 0
        flight_details.save()
        messages.success(request, "Flight details archived successfully")
        return redirect('my_flights')


 