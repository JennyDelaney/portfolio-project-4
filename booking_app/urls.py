from . import views
from django.urls import path


urlpatterns = [
    path('book_appt/', views.BookAppointment.as_view(), name='book_appointment'),
]
