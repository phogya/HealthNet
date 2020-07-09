__author__ = 'Nathan'

from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = patterns('',
    url(r'^stats/$', views.statistics, name='stats'),
    url(r'^log/$', views.log, name='log'),
    url(r'^logfilter/$', views.logfilter, name='logfilter')
)