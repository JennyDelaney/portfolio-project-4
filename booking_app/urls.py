from . import views
from django.urls import path


urlpatterns = [
    path('', views.index.as_views(), name='home'),
    path('enter_booking/', views.enter_booking, name='enter_booking'),
]