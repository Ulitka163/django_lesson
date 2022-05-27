# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerialize, MeasurementSerializer, SensorDetailSerializer


class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialize

    def post(self, request):
        serializer = SensorSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK'})
        return Response({'status': 'wrong parameters'})

    def patch(self, request, id):
        sensor = Sensor.objects.get(pk=id)
        serializer = SensorSerialize(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK'})
        return Response({'status': 'wrong parameters'})


class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateAPIView(APIView):
    # def get(self, request):
    #     sensors = Sensor.objects.all()
    #     ser = SensorSerialize(sensors, many=True)
    #     return Response(ser.data)

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'OK'})
        return Response({'status': 'wrong parameters'})

    # def patch(self, request, id):
    #     sensor = Sensor.objects.get(pk=id)
    #     serializer = SensorSerialize(sensor, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'OK'})
    #     return Response({'status': 'wrong parameters'})


