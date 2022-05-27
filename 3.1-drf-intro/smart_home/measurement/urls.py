from django.urls import path

from .views import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

urlpatterns = [
    path('sensors/', ListCreateAPIView.as_view()),
    path('sensors/<int:id>/', ListCreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('measurements/', CreateAPIView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
