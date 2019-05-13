# Generated by Django 2.0.13 on 2019-03-06 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_number', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('note', models.TextField()),
            ],
        ),
    ]