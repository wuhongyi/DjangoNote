# Generated by Django 2.0.13 on 2019-03-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elog', '0007_auto_20190311_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='fc73',
            new_name='fc73_begin',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='fc74',
            new_name='fc73_end',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='fc75',
            new_name='fc74_begin',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='ic_gas_pressure',
            new_name='fc74_end',
        ),
        migrations.AddField(
            model_name='log',
            name='fc75_begin',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='fc75_end',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='ic_gas_pressure_begin',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='ic_gas_pressure_end',
            field=models.FloatField(default=0),
        ),
    ]