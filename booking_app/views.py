from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView
from .models import Booking
from .forms import BookingForm


class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    template_name = 'index.html'

    def get(self, request):
        return render(request, 'index.html')


class ApptList(generic.ListView):
    """
    This is the view that will bring up the
    list of appoinments for a particular user
    so that they can be edited or deleted
    """
    model = Booking
    queryset = Booking.objects.filter(status=1).order_by('-date_requested')
    template_name = 'booking_app/appt_list.html'
    paginate_by = 9


class AddAppt(FormView):
    """
    Renders the Appt Booking form page in the browser
    Using the OnlineForm created in the forms.py file
    When the booking form is completed and submitted
    the user is redirect to a thank you for booking
    message page.
    """
    form_class = BookingForm
    template_name = 'booking_app/add_appt.html'
    success_url = '/thank_you/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            form.save()
            return render(request, 'thank_you.html')
        else:
            message.error(request, 'Appointment is not completed, please check the appointment information')

        return render(request, template_name, {'form': form})

class ThankYou(generic.DetailView):
    """
    Renders the Thank You page in the browser
    """
    template_name = 'thank_you.html'

    def get(self, request):
        return render(request, 'thank_you.html')