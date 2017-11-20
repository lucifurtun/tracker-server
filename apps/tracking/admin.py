from django.contrib import admin

from apps.tracking import models

admin.site.register(models.Device)
admin.site.register(models.Position)
