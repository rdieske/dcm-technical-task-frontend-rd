from django.test import TestCase
from django.urls import reverse

from rest_framework import status

class TestIndex(TestCase):
        
    def test_index(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'spa/index.html')
