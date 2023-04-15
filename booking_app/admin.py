from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_filter = ('status', 'time_requested')
    list_display = ('user',
                    'name',
                    'status',
                    'date_requested',
                    'time_requested',
                    'email_address',
                    'phone',)
    search_fields = ['email_address', 'name']
    actions = ['confirm_appointment']

    def confirm_appointment(self, request, queryset):
        queryset.update(approved=True)
