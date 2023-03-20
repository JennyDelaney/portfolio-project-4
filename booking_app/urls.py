from . import views
from django.urls import path


urlpatterns = [
    path('appt_list/', views.ApptList.as_view(), name='appt_list'),
]
