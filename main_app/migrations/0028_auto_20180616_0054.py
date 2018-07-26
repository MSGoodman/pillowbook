# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-16 04:54
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_auto_20180615_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='boardgame',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='food',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='literature',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='music',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='overview',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='television',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='wine',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=3, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
