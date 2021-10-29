import datetime

from django.db import models


class Topic(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)
    full_name = models.CharField(max_length=25)
    roll_number = models.CharField(max_length=25)


class Record(models.Model):
    id = models.AutoField(db_column='_id', primary_key=True)
    topic_name = models.CharField(max_length=25)
    start_time = models.CharField(max_length=25)
    end_time = models.CharField(max_length=25,null=True)
    duration = models.FloatField(null=True)

