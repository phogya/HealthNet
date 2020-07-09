from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = patterns('',
    url(r'^$', views.editInfos_home, name='editInfos_home'),
    url(r'^editInfos2/$', views.editInfos2, name='editInfos2'),
    url(r'^editInfos3/$', views.editInfos3, name='editInfos3'),
    url(r'^editInfos_for_patient/$', views.editInfos_for_patient, name='editInfos_for_patient'),
    url(r'^editInfos_for_patient2/$', views.editInfos_for_patient2, name='editInfos_for_patient2'),
    url(r'^editInfos_for_doctor/$', views.editInfos_for_doctor, name='editInfos_for_doctor'),
    url(r'^editInfos_for_doctor2/$', views.editInfos_for_doctor2, name='editInfos_for_doctor2'),
    url(r'^editInfos_for_nurse/$', views.editInfos_for_nurse, name='editInfos_for_nurse'),
    url(r'^editInfos_for_nurse2/$', views.editInfos_for_nurse2, name='editInfos_for_nurse2'),
    url(r'^editInfos_for_admin/$', views.editInfos_for_admin, name='editInfos_for_admin'),
    url(r'^editInfos_for_admin2/$', views.editInfos_for_admin2, name='editInfos_for_admin2'),
    url(r'^allInfo_home/$', views.allInfo_home, name='allInfo_home'),
    url(r'^patientSelect/$', views.patientSelect, name='patientSelect'),
    url(r'^patientView/$', views.patientView, name='patientView'),
    url(r'^patientView_patient/$', views.patientView_patient, name='patientView_patient'),
    url(r'^releaseTest/$', views.releaseTest, name='releaseTest'),
)