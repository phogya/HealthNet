__author__ = 'Carlton'

from django import forms
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm, Textarea, Select


class PrescriptionForm(ModelForm):


    class Meta:

        model = Prescription
        fields= [
            "medication", "dose", "refill"
        ]
