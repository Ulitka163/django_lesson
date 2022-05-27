from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class SensorSerialize(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['ID_sensor', 'temp', 'measurement_date']

    def create(self, validated_data):
        measurement = Measurement.objects.create(**validated_data)
        measurement.save()
        return measurement


class MeasurementAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temp', 'measurement_date']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementAllSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']




