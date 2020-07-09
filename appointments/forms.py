__author__ = 'Kayla'

from django.forms import ModelForm, widgets
from django import forms
from .models import *
# from bootstrap3_datetime.widgets import DateTimePicker
from datetime import datetime
from django.utils import timezone
from registration.models import Patient
from registration.models import Doctor


class AppointmentForm(forms.ModelForm):

    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form_datetime form-control', 'required':False}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form_datetime form-control', 'required':False}))
    class Meta:
        model = Appointment
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'description' : forms.TextInput(attrs={'class':'form-control', 'required':True}),
            # 'doctor': forms.Select(attrs={'class':'form-control', 'required':True, 'obj': Doctor.objects.all()}),
        }
        fields = ["title", "description", "start_time", "end_time"]
        # I added in start and end time into the fields

    def clean_start_time(self):
        start = self.cleaned_data['start_time']
        if start <= timezone.now() :
            raise forms.ValidationError('Invalid start time')
        return start

    def clean_end_time(self):
        start = self.cleaned_data['start_time']
        end = self.cleaned_data['end_time']
        if end <= start:
            raise forms.ValidationError('Invalid end time')
        return end

"""
    def set_query_sets(self, user):
        if is_patient(user):
            self.fields["patient"].queryset = Patient.objects.filter(patient = user)
            self.fields["doctor"].queryset = user.patient.doctors

            if is_doctor(user):
                self.fields["doctor"].queryset = Doctor.objects.filter(doctor = user)
                self.fields["patient"].queryset = user.employee.doctor.patient_set
                print("doctor")
            else:
                pass

        else:
            pass
"""