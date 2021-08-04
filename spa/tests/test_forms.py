
from django import forms
from django.core.exceptions import ValidationError
from django.test.testcases import TestCase

from api.models import TestRunRequest
from spa.forms import TestRunRequestForm

class TestTestRunRequestForm(TestCase):

    def test_formUsesCorrectModel(self):
        form = TestRunRequestForm()
        self.assertEquals(form._meta.model, TestRunRequest)

    def test_formUsesFields(self):
        form = TestRunRequestForm()
        self.assertEquals(form._meta.fields, ['requested_by', 'env', 'path'])

    def test_formCreationAddClassToVisibleFields(self):
        form = TestRunRequestForm()
        for visible_field in form.visible_fields():
            self.assertEquals(visible_field.field.widget.attrs['class'], 'form-control')