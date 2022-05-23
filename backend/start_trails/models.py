from django.db import models

# Create your models here.


class StartTrail(models.Model):
    start_lat = models.FloatField()
    start_lng = models.FloatField()
