# Generated by Django 3.1 on 2021-09-07 05:46

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
                ('topic_name', models.CharField(max_length=25)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('duration', models.FloatField()),
            ],
            options={
                'db_table': 'Records',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(db_column='_id', primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=25)),
                ('roll_number', models.CharField(max_length=25)),
            ],
        ),
    ]
