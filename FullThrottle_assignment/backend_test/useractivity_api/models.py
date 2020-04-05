from django.db import models


# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=300)


class ActivityPeriods(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
