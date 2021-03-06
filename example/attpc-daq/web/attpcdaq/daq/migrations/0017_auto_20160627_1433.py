# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daq', '0016_auto_20160620_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datasource',
            name='data_router',
        ),
        migrations.AddField(
            model_name='datasource',
            name='data_router_ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1', verbose_name='Data router IP address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datasource',
            name='data_router_port',
            field=models.PositiveIntegerField(default=46005, verbose_name='Data router port'),
        ),
        migrations.AddField(
            model_name='datasource',
            name='data_router_type',
            field=models.CharField(choices=[('ICE', 'ICE'), ('TCP', 'TCP'), ('FDT', 'FDT'), ('ZBUF', 'ZBUF')], default='TCP', max_length=4),
        ),
        migrations.DeleteModel(
            name='DataRouter',
        ),
    ]
