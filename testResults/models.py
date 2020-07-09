from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, Select
from registration.models import Patient

""" Alternate Method 1
class TestF(forms.Form):

    patient_name = forms.CharField(max_length=50)
    test_name = forms.CharField(max_length=100)
    results = forms.CharField(max_length=500)
"""

class TestM(models.Model):

    #patient_name = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=50, default= "default")
    test_name = models.CharField(max_length=50)
    results = models.CharField(max_length=1000)
    viewable = models.CharField(max_length=10)
    #image = models.ImageField(upload_to='images/', null=True, blank=True)


class TestMF(ModelForm):

    class Meta:
        model = TestM
        widgets = {
            'results': Textarea(attrs={'cols': 30, 'rows': 10}),
            }
        fields = ['test_name','results']


