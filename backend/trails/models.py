from django.db import models
from authentication.models import User
from end_trails.models import EndTrail
from start_trails.models import StartTrail
# Create your models here.


class Trail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trail_name = models.CharField(max_length=70)
    difficulty = models.IntegerField()
    trail_start = models.ForeignKey(
        StartTrail, on_delete=models.CASCADE, null=True)
    trail_end = models.ForeignKey(
        EndTrail, on_delete=models.CASCADE, null=True)
