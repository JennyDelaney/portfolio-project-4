from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_filter = ('status', 'time_requested')
    list_display = ('name', 'status', 'date_requested', 'time_requested')
    search_fields = ['email_address', 'name']
