# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-23 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_auto_20180623_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerypurchase',
            name='store',
            field=models.TextField(blank=True, null=True),
        ),
    ]
