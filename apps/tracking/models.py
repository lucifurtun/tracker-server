from django.conf import settings
from django.db import models


class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    serial_number = models.CharField(max_length=100)

    @property
    def latest_position(self):
        try:
            return self.positions.order_by('-time_received')[0]
        except IndexError:
            return None


class Position(models.Model):
    device = models.ForeignKey(Device, related_name='positions')

    time_sent = models.DateTimeField(null=True, blank=True)
    time_received = models.DateTimeField(auto_now_add=True)

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
