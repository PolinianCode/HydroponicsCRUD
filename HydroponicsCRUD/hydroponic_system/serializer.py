from rest_framework import serializers
from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'owner', 'name']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short")
        return value
