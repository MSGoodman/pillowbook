# Generated by Django 2.0.7 on 2018-08-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20180807_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulebutton',
            name='background_color_complete',
            field=models.TextField(default='#6e8a99'),
        ),
    ]
