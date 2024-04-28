from rest_framework import serializers
from .models import Measures


class MeasurementSerializer(serializers.ModelSerializer): \

    """
        Serializer for measures model.
    """

    class Meta:
        model = Measures
        fields = ['id', 'hydroponic_system', 'ph',
                  'water_temperature', 'tds', 'time']
