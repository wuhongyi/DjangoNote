# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daq', '0025_auto_20161206_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='observable',
            name='units',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
