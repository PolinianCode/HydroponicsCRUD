from django.db import models
from hydroponic_system.models import HydroponicSystem

# Create your models here.


class Measures(models.Model):
    hydroponic_system = models.ForeignKey(
        HydroponicSystem, on_delete=models.CASCADE)
    ph = models.FloatField()
    water_temperature = models.FloatField()
    tds = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hydroponic_system.name} - {self.time}'
