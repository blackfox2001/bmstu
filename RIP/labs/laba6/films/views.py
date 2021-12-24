from rest_framework import viewsets
from films.serializer import FilmSerializer
from films.models import Films


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать акции компаний
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Films.objects.all()
    serializer_class = FilmSerializer  # Сериализатор для модели