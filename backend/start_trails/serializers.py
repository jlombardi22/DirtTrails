from rest_framework import serializers
from .models import StartTrail


class StartTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartTrail
        fields = ['id', 'start_lat', 'start_lng']
        depth = 1
