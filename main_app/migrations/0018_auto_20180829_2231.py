# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-30 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_literature_up_to_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='creator',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardioexercise',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cardioexercise',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='learning',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='eat_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='episode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pursuitprogress',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='television',
            name='episode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=13, max_digits=16, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='console',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='developer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weightexercise',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weightexercise',
            name='reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weightexercise',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weightexercise',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
