__author__ = 'Kayla'

from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^$', views.appointment_form, name='calendar'),


]