from films.models import Films
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Films
        # Поля, которые мы сериализуем
        fields = '__all__'