from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):
    ID_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.FloatField()
    measurement_date = models.DateTimeField(auto_now_add=True)
