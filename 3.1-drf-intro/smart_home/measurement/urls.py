from django.urls import path

from .views import SensorAPIView, SensorDetailAPIView, MeasurementAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('sensors/<id>/', SensorAPIView.as_view()),
    path('sensors/<pk>/', SensorDetailAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
