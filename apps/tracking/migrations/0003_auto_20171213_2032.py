# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20171127_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='lat',
            field=models.DecimalField(decimal_places=14, max_digits=16),
        ),
        migrations.AlterField(
            model_name='position',
            name='lng',
            field=models.DecimalField(decimal_places=14, max_digits=16),
        ),
    ]
