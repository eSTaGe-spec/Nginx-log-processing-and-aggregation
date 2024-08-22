from django.test import TestCase
from .models import LogData


class LogDataTestCase(TestCase):
    def setUp(self) -> None:
        self.log_data = LogData.objects.create(
            time='17/May/2015:08:05:48 +0000',
            remote_ip='80.91.33.133',
            remote_user='-',
            method='GET',
            url='/downloads/product_1',
            response_code='404',
            response_size=324,
            referrer='-',
            agent='Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)'
        )

    def test_log_save(self):
        self.assertEqual(self.log_data.time, '17/May/2015:08:05:48 +0000')
        self.assertEqual(self.log_data.remote_ip, '80.91.33.133')
        self.assertEqual(self.log_data.remote_user, '-')
        self.assertEqual(self.log_data.method, 'GET')
        self.assertEqual(self.log_data.url, '/downloads/product_1')
        self.assertEqual(self.log_data.response_code, '404')
        self.assertEqual(self.log_data.response_size, 324)
        self.assertEqual(self.log_data.referrer, '-')
        self.assertEqual(self.log_data.agent, 'Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.17)')
