from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = patterns('',
    url(r'^$', views.transfer_home, name='transfer_home'),
    url(r'^do_transfer/$', views.do_transfer, name='do_transfer'),
    url(r'^hospital_select/$', views.hospital_select, name='hospital_select'),
    url(r'^do_initial_transfer/$', views.do_initial_transfer, name='do_initial_transfer'),
    url(r'^doctor_select/$', views.doctor_select, name='doctor_select'),
    url(r'^do_doctor_select/$', views.do_doctor_select, name='do_doctor_select'),
)
