# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField(blank=True, null=True)),
                ('time_received', models.DateTimeField(auto_now_add=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracking.Device')),
            ],
        ),
    ]
