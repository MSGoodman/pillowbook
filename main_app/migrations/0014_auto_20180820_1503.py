# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-20 19:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20180820_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toilet',
            name='bristol',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)]),
        ),
    ]
