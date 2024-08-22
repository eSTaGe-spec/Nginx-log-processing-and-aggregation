from rest_framework import serializers

from .models import LogData


class LogDataSerializer(serializers.ModelSerializer):
    """
    Сериализатор логов
    """
    class Meta:
        model = LogData
        fields = '__all__'
