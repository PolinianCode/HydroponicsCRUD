from rest_framework import serializers
from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):

    """
    Serializer for HydroponicSystem model.
    """

    class Meta:
        model = HydroponicSystem
        fields = ['id', 'owner', 'name']

    """
        Validationg the length of the name field

        The name must me at least 3 characters long
    """

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Name is too short")
        return value
