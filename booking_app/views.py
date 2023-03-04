from django.shortcuts import render


def enter_booking(request):
    return render(request, 'booking_app/booking_appointment.html')
