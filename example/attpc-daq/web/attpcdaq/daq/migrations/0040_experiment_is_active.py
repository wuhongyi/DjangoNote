# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daq', '0039_auto_20170227_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
