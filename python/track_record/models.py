from django.db import models

class Track_record(models.Model):
    date_of_activity = models.DateField()
    activity_name = models.TextField()
    time_duration = models.IntegerField()
    distance = models.FloatField()