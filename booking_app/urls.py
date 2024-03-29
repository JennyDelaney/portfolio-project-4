from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('appt_list/', views.ApptList.as_view(), name='appt_list'),
    path('add_appt/', views.AddAppt.as_view(), name='add_appt'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'),
    path('edit_appt/<booking_id>', views.edit_appt, name='edit_appt'),
    path('delete_appt/<booking_id>', views.delete_appt, name='delete_appt'),
]
