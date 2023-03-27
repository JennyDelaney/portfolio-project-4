from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    This form is connected to the view
    in order to provide users with the necessary
    fields to make a booking.
    It also provides the labels and placeholder
    text for each field, as well as the widgets and
    handles validation where required.
    """
    class Meta:
        model = Booking
        fields = ['name', 'email_address', 'phone', 'date_requested', 'time_requested',]
