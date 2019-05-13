# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_auto_20160822_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='level_name',
        ),
        migrations.RemoveField(
            model_name='logentry',
            name='level_number',
        ),
        migrations.AddField(
            model_name='logentry',
            name='level',
            field=models.IntegerField(choices=[(10, 'Debug'), (20, 'Info'), (30, 'Warning'), (40, 'Error'), (50, 'Critical')], default=30),
            preserve_default=False,
        ),
    ]