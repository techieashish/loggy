from django.test import TestCase


class LogsTest(TestCase):

    def test_details(self):
        response = self.client.get('/logs/')
        self.assertEqual(response.status_code, 200)

