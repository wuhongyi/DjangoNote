# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daq', '0033_eccserver_config_backup_root'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='user',
        ),
    ]
