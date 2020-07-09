__author__ = 'Carlton M'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admit/$', views.admit_patient, name='admit_patient'),
    url(r'^select/$', views.select_patient, name='select_patient'),
    url(r'^view/$', views.patient_view, name='patient_view'),
    url(r'^select2/$', views.discharge_patient, name='discharge_patient'),
    url(r'^discharge/$', views.discharge_patient2, name='discharge_patient2'),
    url(r'^done/$', views.discharge_patient3, name='discharge_patient3')
]