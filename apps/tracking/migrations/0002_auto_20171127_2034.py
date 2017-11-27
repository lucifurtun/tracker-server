# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='tracking.Device'),
        ),
    ]
