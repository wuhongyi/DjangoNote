# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-22 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'verbose_name_plural': 'Log entries'},
        ),
        migrations.RenameField(
            model_name='logentry',
            old_name='name',
            new_name='logger_name',
        ),
    ]