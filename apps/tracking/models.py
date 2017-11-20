from django.conf import settings
from django.db import models


class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    serial_number = models.CharField(max_length=100)


class Position(models.Model):
    device = models.ForeignKey(Device)

    time_sent = models.DateTimeField(null=True, blank=True)
    time_received = models.DateTimeField(auto_now_add=True)

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
