from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, AdvertisementFavorites
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer, AdvertisementFavoritesSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_class = AdvertisementFilter

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated(), IsAdminUser()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly(), IsAdminUser()]

        return []


class AdvertisementFavoritesViewSet(ModelViewSet):
    """Избранные объявления"""
    queryset = AdvertisementFavorites.objects.all()
    serializer_class = AdvertisementFavoritesSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = AdvertisementFavorites.objects.filter(user=self.request.user.id)
        serializer = AdvertisementFavoritesSerializer(queryset, many=True)
        return Response(serializer.data)

