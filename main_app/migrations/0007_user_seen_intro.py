# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-08 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20180803_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seen_intro',
            field=models.BooleanField(default=False),
        ),
    ]
