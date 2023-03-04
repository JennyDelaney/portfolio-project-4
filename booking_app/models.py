from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Pending"), (1, "Confirmed"))

TIME_CHOICE = (
    ('AM', 'AM'),
    ('PM', 'PM'),
)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_appointments")
    name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    date_requested = models.DateField()
    time_requested = models.CharField(max_length=50, choices=TIME_CHOICE, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_requested']

    def __str__(self):
        return self.name