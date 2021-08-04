from django import forms
from django.core.exceptions import ValidationError

from api.models import TestRunRequest

class TestRunRequestForm(forms.ModelForm):
    class Meta:
        model = TestRunRequest
        fields = ['requested_by', 'env', 'path']
        
    def __init__(self, *args, **kwargs):
        super(TestRunRequestForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'form-control'