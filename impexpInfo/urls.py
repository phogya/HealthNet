from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = patterns('',
    url(r'^$', views.privacyCheck, name='privacyCheck'),
    url(r'^declineCheck/$', views.declineCheck, name='declineCheck'),
    url(r'^export/$', views.export, name='export'),
    url(r'^get_file_name/$', views.get_file_name, name='get_file_name'),
    url(r'^importCSV/$', views.importCSV, name='importCSV'),
)