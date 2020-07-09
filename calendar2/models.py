from django.core.urlresolvers import reverse
from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, Select
from registration.models import Patient
import datetime

from django.forms import ModelForm, Form
from django.shortcuts import render, redirect, render_to_response


class Appt(models.Model):
    """
    patient can only make appointments with their doctor
    """
    patient = models.CharField(max_length=20,default="default")
    doctor = models.CharField(max_length=20,default="default")
    year = models.CharField(max_length=20,default="default")
    month = models.CharField(max_length=20,default="default")
    day = models.CharField(max_length=20,default="default")
    start_time_hour = models.CharField(max_length=10,default="default")
    start_time_min = models.CharField(max_length=10,default="default")
    start_time_apm = models.CharField(max_length=5,default="default")
    end_time_hour = models.CharField(max_length=10,default="default")
    end_time_min = models.CharField(max_length=10,default="default")
    end_time_apm = models.CharField(max_length=5, default="default")
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    hospital = models.CharField(max_length=100,default="default")

    def get_absolute_url(self):
        return redirect('/calendar2/view_appt/%i' % self.id)

class ApptForm(ModelForm):



    class Meta:
        model = Appt
        widgets = {


        }
        fields =["title", "description"]