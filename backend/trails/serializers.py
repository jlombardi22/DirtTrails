from rest_framework import serializers
from .models import Trail


class TrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ['id', 'trail_name', 'difficulty',
                  'trail_start_id', 'trail_end_id', 'user_id']
        depth = 1
    user_id = serializers.IntegerField(write_only=True)
    trail_start_id = serializers.IntegerField(write_only=True)
    trail_end_id = serializers.IntegerField(write_only=True)
