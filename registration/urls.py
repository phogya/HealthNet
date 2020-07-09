__author__ = 'Melissa'

from django.conf.urls import url
from . import views

urlpatterns = [

    #url(r'^homepage/$', views.homepage, name='homepage'),
    url(r'^$', views.index, name='index'),
    url(r'^chooseregistration/$', views.chooseregistration, name='choose registration'),
    url(r'^otherregistration/$', views.otherregistration, name='other registration'),
    url(r'^docregistration/$', views.docregistration, name='doctor registration'),
    url(r'^adminregistration/$', views.adminregistration, name='admin registration'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.logIn, name='login'),
    url(r'^login/auth/$', views.auth_view, name ='auth_view'),
    url(r'^logout/$', views.logout, name ='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register_user, name= 'register'),
    url(r'^reg1/$', views.personal_info_reg, name='reg1'),
    url(r'^reg2/$', views.med_info_reg, name='reg2'),
    url(r'^invalid/$', views.invalid_login, name='invalid login'),
    url(r'^authentication', views.choose_auth, name='choose auth'),
    url(r'^nurseauth', views.authnurse, name='nurse auth'),
    url(r'^docauth', views.authdoc, name='doc auth'),
    url(r'^adminauth', views.authadmin, name='admin auth'),
    url(r'^auth_success', views.auth_success, name='auth success'),
    #make a tutorial page for new users


]