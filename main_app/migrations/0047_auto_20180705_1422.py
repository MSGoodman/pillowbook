# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-05 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0046_auto_20180703_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
