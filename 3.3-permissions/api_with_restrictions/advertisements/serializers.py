from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementFavorites


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        advertisement = Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')
        if self.context["request"].method == 'POST' and advertisement.count() >= 10:
            raise serializers.ValidationError('У вас больше 10 открытых объявлений.')
        if self.context["request"].method == 'PATCH' and advertisement.count() >= 10 and data["status"] == "OPEN":
            raise serializers.ValidationError('У вас больше 10 открытых объявлений.')
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию

        return data


class AdvertisementFavoritesSerializer(serializers.ModelSerializer):
    """Избранные объявления"""
    class Meta:
        model = AdvertisementFavorites
        fields = ['id', 'user', 'advertisement']
        read_only_fields = ['user']

    def validate(self, data):
        if self.context["request"].method == 'POST' and \
                self.context["request"].user.id == data['advertisement'].creator_id:
            raise serializers.ValidationError('Вы не можете добавлять свое объявление в избранное')
        return data
