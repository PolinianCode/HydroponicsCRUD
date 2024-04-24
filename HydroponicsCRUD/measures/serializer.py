from rest_framework import serializers
from .models import Measures


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measures
        fields = ['id', 'hydroponic_system', 'ph',
                  'water_temperature', 'tds', 'time']
