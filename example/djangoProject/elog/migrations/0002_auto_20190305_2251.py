# Generated by Django 2.0.13 on 2019-03-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='run_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='stop_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
