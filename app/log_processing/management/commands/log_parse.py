import json
import requests
from django.core.management import BaseCommand

from ...models import LogData


class Command(BaseCommand):
    """
    Команда для парсинга логов и с последующим сохранением данных в базу
    """
    help = 'Parse log file and save data to database'

    def add_arguments(self, parser):
        """
        Добавление аргумента для командной строки
            url_log_file : str -> Путь к файлу лога
        """
        parser.add_argument('url_log_file', type=str)

    def handle(self, *args, **options):
        """
        Основной метод выполнения команды
        Читает файл и парсит строки, сохраняя данные в базу
        """
        log_file = options['url_log_file']
        response = requests.get(log_file)

        if response.status_code != 200:
            self.stderr.write(self.style.ERROR('Error. Failed to open log file. Please check the URL.'))
            return

        lines = response.text.strip().split('\n')

        for line in lines:
            data = json.loads(line)
            request = data['request']
            method, url, _ = request.split(maxsplit=2)

            LogData.objects.create(
                time=data['time'],
                remote_ip=data['remote_ip'],
                remote_user=data['remote_ip'],
                method=method,
                url=url,
                response_code=data['response'],
                response_size=data['bytes'],
                referrer=data['referrer'],
                agent=data['agent'],
            )

        self.stdout.write(self.style.SUCCESS('Log parsed and data saved to database'))
