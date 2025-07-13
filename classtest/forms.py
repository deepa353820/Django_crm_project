from .models import*
from django import forms

class test_forms(forms.ModelForm):
    class Meta:
        model = tests
        fields = '__all__'

        