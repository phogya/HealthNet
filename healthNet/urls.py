"""healthNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^calendar/', include('appointments.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^system/', include('system.urls')),
    url(r'^prescription/', include('prescriptions.urls')),
    url(r'^testResults/', include('testResults.urls')),
    url(r'^patientTransfer/', include('patientTransfer.urls')),
    url(r'^impexpInfo/', include('impexpInfo.urls')),
    url(r'^editInfos/', include('editInfos.urls')),
    url(r'^message/',include('message.urls')),
    url(r'^calendar2/',include('calendar2.urls')),
    url(r'^Admission_Discharge/',include('Admission_Discharge.urls')),
    #url(r'^foo$', TemplateView.as_view(template_name="index.html"), name='index'),


    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

