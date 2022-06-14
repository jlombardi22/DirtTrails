from rest_framework import serializers
from .models import Campsite


class CampsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campsite
        fields = ['id', 'campsite_name']
        depth = 1
    user_id = serializers.IntegerField(write_only=True)
