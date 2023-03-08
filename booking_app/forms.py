from django.forms import ModelForm
from django.core import validators
from django import forms
from .models import Booking


class OnlineForm(ModelForm):
    """
    This form is connected to the view
    in order to provide users with the necessary
    fields to make a booking.
    It also provides the labels and placeholder
    text for each field, as well as the widgets and
    handles validation where required.
    """
    name = forms.CharField(
        label='Patients Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Patients Name'}),
    )

    email_address = forms.EmailField(
        label='Email Address of Patient',
        required=True,
        validators=[validators.EmailValidator(message="Invalid Email")],
        widget=forms.TextInput(attrs={'placeholder': 'Email Address'}),
    )

    phone = forms.IntegerField(
        label='Contact Number of Patient',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Contact Number'}),
    )


class Meta:
    """
    Defines which model to pull the fields from
    """
    model = Booking
    fields = '__all__'
    exclude = ('user', )
