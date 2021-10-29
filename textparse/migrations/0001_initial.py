# Generated by Django 3.1 on 2021-09-06 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 76157))),
                ('updatedAt', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 76180))),
            ],
            options={
                'db_table': 'Records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=90)),
                ('body', models.CharField(max_length=900)),
                ('parsed', models.CharField(max_length=90)),
                ('keys', models.CharField(max_length=1000)),
                ('to', models.CharField(max_length=90)),
                ('startTime', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 74831))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 74857))),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 74873))),
                ('updatedAt', models.DateTimeField(default=datetime.datetime(2021, 9, 6, 7, 17, 43, 74893))),
            ],
            options={
                'db_table': 'textparse_data',
                'managed': True,
            },
        ),
    ]
