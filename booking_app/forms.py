from django import forms
from .models import Booking


class DateInput(forms.DateInput):
    """
    This class provides a widget for use in the
    booking form. It provides a calendar for users
    to pick the booking date from
    """
    input_type = 'date'


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
        fields = [
            'name',
            'email_address',
            'phone',
            'date_requested',
            'time_requested',]
        widgets = {'date_requested': DateInput()}
