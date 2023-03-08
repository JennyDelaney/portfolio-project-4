from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookAppointment(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-date_requested')
    template_name = 'booking_app/book_appt.html'
    paginate_by = 6

# def enter_booking(request):
#     return render(request, 'booking_app/book_appt.html')
