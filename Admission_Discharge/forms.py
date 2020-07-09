__author__ = 'Carlton M'

from django.forms import Textarea
from django import forms
from django.contrib.auth.models import User
from .models import *

class Admission_DischargeForm(forms.ModelForm):

    class Meta:
        model = Admission_Discharge
        widgets = {
            'reason': Textarea(attrs={'cols': 30, 'rows': 10}),
            }
        fields= [
            #"date_admitted", "date_discharged",
            "reason"
        ]


class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital
        fields = [
            "name", "location"
        ]