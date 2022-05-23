from rest_framework import serializers
from .models import EndTrail


class EndTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndTrail
        fields = ['id', 'end_lat', 'end_lng']
        depth = 1
