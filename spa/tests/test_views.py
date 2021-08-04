import operator
from django.urls import reverse
from django.test import TestCase

from api.models import TestEnvironment, TestRunRequest

class TestIndex(TestCase):
    def setUp(self) -> None:
        self.env = TestEnvironment.objects.create(name='my_env')

    def test_indexHasCorrectTemplate(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'spa/index.html')

    def test_contextHasTestRunRequests(self):
        TestRunRequest.objects.create(requested_by='Greg', env=self.env)
        TestRunRequest.objects.create(requested_by='Raffael', env=self.env)
        response = self.client.get('')
        self.assertQuerysetEqual(response.context['TestRunRequests'], TestRunRequest.objects.all().reverse(),ordered=False)

    def test_contextHasTestRunRequestsInCorrectOrder(self):
        testRunRequest1 = TestRunRequest.objects.create(requested_by='Greg', env=self.env)
        testRunRequest2 = TestRunRequest.objects.create(requested_by='Raffael', env=self.env)
        response = self.client.get('')
        self.assertEqual(response.context['TestRunRequests'][0].requested_by, 'Raffael')
        self.assertEqual(response.context['TestRunRequests'][1].requested_by, 'Greg')