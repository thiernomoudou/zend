# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 13:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverybookingmodel',
            name='pickupDetail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pickup_detail', to='api.DeliveryBookingLocationModel'),
            preserve_default=False,
        ),
    ]
