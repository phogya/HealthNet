from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^prescription/$', views.prescription, name='prescription'),
    url(r'^$', views.prescription_home, name='index'),
    url(r'^create/$', views.prescription_create, name='prescription_create'),
    url(r'^view/$', views.prescription_view, name='prescription_view'),
    url(r'^success/$', views.prescription_add, name='prescription_add'),
    url(r'^remove/$', views.prescription_remove, name='prescription_remove'),
    url(r'^removed/$', views.prescription_removed, name='prescription_removed'),
    url(r'^edit/$', views.prescription_edit, name='prescription_edit'),
    url(r'^edited/$', views.prescription_edited, name='prescription_edited'),
    url(r'^save/$', views.prescription_save, name='prescription_save'),
    url(r'^patient/$', views.patient_home, name='patient_home'),
    url(r'^select/$', views.select_prescription, name='select_prescription')
    #url(r'^$', views.detail, name='detail'),
]