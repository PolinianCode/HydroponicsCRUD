from rest_framework import serializers
from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'owner', 'name']
