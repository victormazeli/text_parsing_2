# Generated by Django 3.1 on 2021-09-06 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textparse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 18, 5, 41162)),
        ),
        migrations.AlterField(
            model_name='data',
            name='endTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 18, 5, 41153)),
        ),
        migrations.AlterField(
            model_name='data',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 18, 5, 41135)),
        ),
        migrations.AlterField(
            model_name='data',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 18, 5, 41174)),
        ),
    ]
