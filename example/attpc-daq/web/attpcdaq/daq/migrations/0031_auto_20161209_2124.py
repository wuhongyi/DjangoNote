# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daq', '0030_auto_20161207_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='observable',
            options={'ordering': ('order', 'pk')},
        ),
        migrations.AddField(
            model_name='observable',
            name='order',
            field=models.IntegerField(default=1000),
        ),
    ]
