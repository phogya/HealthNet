__author__ = 'nathan'

from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = patterns('',
    url(r'^send/$', views.sendNew, name='sendNew'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^sentbox/$',views.sentBox,name='sentBox'),
    url(r'^reply/$',views.reply,name='reply'),
    url(r'^delete/$',views.deleteMessage,name='delete')
)