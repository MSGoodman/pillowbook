# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-04 18:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20180604_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overview',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
