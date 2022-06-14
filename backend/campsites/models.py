from django.db import models
from authentication.models import User
# Create your models here.


class Campsite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campsite_name = models.CharField(max_length=100)
