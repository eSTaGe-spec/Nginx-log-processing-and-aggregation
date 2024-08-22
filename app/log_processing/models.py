from django.db import models


class LogData(models.Model):
    """
    Модель логов
    """
    time = models.CharField(max_length=50)
    remote_ip = models.CharField(max_length=20)
    remote_user = models.CharField(max_length=100, blank=True, null=True)
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=100)
    response_code = models.CharField(max_length=100)
    response_size = models.IntegerField()
    referrer = models.CharField(max_length=100, blank=True, null=True)
    agent = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Магический метод для отображения записей в админ панели
        """
        return f'LogData №{self.id} url -> {self.url}'
