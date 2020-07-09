from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = [
    url(r'^$', views.add_appt_home, name='add_appt_home'),
    url(r'^add_appt_patient/$', views.add_appt_patient, name='add_appt_patient'),
    url(r'^add_appt_doctor/$', views.add_appt_doctor, name='add_appt_doctor'),
    url(r'^add_appt_nurse/$', views.add_appt_nurse, name='add_appt_nurse'),
    url(r'^view_cal/$', views.view_cal, name='view cal'),
    url(r'^view_appt/$', views.view_appt, name='view appt'),
    url(r'^choose_appt/$', views.choose_appt, name='choose_appt'),
]