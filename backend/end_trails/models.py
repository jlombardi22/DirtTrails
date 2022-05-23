from django.db import models

# Create your models here.


class EndTrail(models.Model):
    end_lat = models.FloatField()
    end_lng = models.FloatField()
