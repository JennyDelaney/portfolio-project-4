from django.shortcuts import render
from django.views import generic
from .models import Booking

def enter_booking(request):
    return render(request, 'booking_app/booking_appointment.html')
