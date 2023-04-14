from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


class Home(generic.DetailView):
    """
    Renders the Index page in the browser
    """
    template_name = 'index.html'

    def get(self, request):
        return render(request, 'index.html')


class ApptList(generic.DetailView):
    """
    This is the view that will bring up the
    list of appoinments for a particular user
    so that they can be edited or deleted
    """
    model = Booking
    template_name = 'booking_app/appt_list.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user).order_by('-date_requested')

            return render(request, 'booking_app/appt_list.html', {
                'bookings': bookings
            })
        else:
            return redirect('account_login')


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
            booking.user = request.user
            form.save()
            return render(request, 'booking_app/thank_you.html')
        else:
            message.error(request, 'You appointment is not completed, please check the appointment information')

        return render(request, template_name, {'form': form})


class ThankYou(generic.DetailView):
    """
    Renders the Thank You page in the browser
    """
    template_name = 'booking_app/thank_you.html'

    def get(self, request):
        return render(request, 'booking_app/thank_you.html')


@login_required
def edit_appt(request, booking_id):
    """
    When a user is on the My Appointments page
    which can only be accessed if you are
    logged in, they can click on the edit button.
    This will bring them to a new page, where the booking
    they wish to edit, located using the appointment id,
    appears, prepopulated with the current information.
    Once the user clicks on the submit changes button
    they will be redirected to the home page and a
    confimation message will appear.
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            if request.method == 'POST':
                form = BookingForm(data=request.POST, instance=booking)
                if form.is_valid():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    form.save()
                    messages.success(request, 'Your appointment has been updated')
                    return redirect('/appt_list')
        else:
            messages.error(request, 'You do not have the authority to access this page!')
            return redirect('/')

    form = BookingForm(instance=booking)

    return render(request, 'booking_app/edit_appt.html', {
        'form': form
        })


@login_required
def delete_appt(request, booking_id):
    """
    When a user is on the My Appointments page
    which can only be accessed if you are
    logged in, they can click on the edit button.
    This will bring them to a new page, where the booking
    they wish to edit, located using the appointment id,
    appears, prepopulated with the current information.
    Once the user clicks on the submit changes button
    they will be redirected to the home page and a
    confimation message will appear.
    """
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.user == request.user:
            booking.delete()
            # Pops up a message to the user when a bookings is cancelled
            messages.success(request, 'Your appointment has been cancelled')
            return redirect('/appt_list')
        else:
            messages.error(request, 'You do not have the authority to access this page!')
            return redirect('/')
