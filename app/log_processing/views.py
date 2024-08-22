from rest_framework import viewsets

from .models import LogData
from .serializers import LogDataSerializer


class LogDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для отображения всех логов
    """
    queryset = LogData.objects.all()
    serializer_class = LogDataSerializer