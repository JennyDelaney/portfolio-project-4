from django.shortcuts import render
from django.views import generic
from .models import Booking


class ApptList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-date_requested')
    template_name = 'booking_app/appt_list.html'
    paginate_by = 9
