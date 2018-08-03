# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20180802_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key',
            field=models.CharField(default='no_activation_key', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]