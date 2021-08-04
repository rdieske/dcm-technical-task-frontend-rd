from django.urls import resolve

from django.test import TestCase

from spa.urls import urlpatterns

class TestUrlpatterns(TestCase):

    def test_indexPath(self):
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'index')

    def test_static_attached(self):
        staticpattern = urlpatterns[len(urlpatterns)-1].pattern.regex.pattern
        self.assertEquals(staticpattern, '^static/(?P<path>.*)$')