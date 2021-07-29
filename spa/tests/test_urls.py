from django.test import TestCase
from django.urls import reverse

from rest_framework import status

class TestUrlpatterns(TestCase):
        
    def test_indexPath(self):
        response = self.client.get('')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
