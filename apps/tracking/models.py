import json

from channels import Group
from django.conf import settings
from django.db import models


class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    serial_number = models.CharField(max_length=100)

    @property
    def last_position(self):
        try:
            return self.positions.order_by('-time_received')[0]
        except IndexError:
            return None

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        Group("tracking").send({"text": json.dumps({'lat': 11, 'lng': 22})})
        super().save(force_insert, force_update, using, update_fields)


class Position(models.Model):
    device = models.ForeignKey(Device, related_name='positions')

    time_sent = models.DateTimeField(null=True, blank=True)
    time_received = models.DateTimeField(auto_now_add=True)

    lat = models.DecimalField(max_digits=16, decimal_places=14)
    lng = models.DecimalField(max_digits=16, decimal_places=14)
