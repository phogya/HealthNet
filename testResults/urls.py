from django.conf.urls import include, url, patterns
from . import views

"""
URL formats go in this file.
"""

urlpatterns = [
    url(r'^$', views.test_home, name='test_home'),
    url(r'^add_test/$', views.add_test, name='add_test'),
    url(r'^view_test/$', views.view_test, name='view_test'),
    url(r'^select_patient/$', views.select_patient, name='select_patient'),
    url(r'^edit_infos_test1/$', views.edit_infos_test1, name='edit_infos_test1'),
    url(r'^edit_infos_test2/$', views.edit_infos_test2, name='edit_infos_test2'),
    url(r'^delete_test1/$', views.delete_test1, name='delete_test1'),
    url(r'^delete_test2/$', views.delete_test2, name='delete_test2'),
    url(r'^patient_test_home/$', views.patient_test_home, name='patient_test_home'),
    url(r'^change_viewable1/$', views.change_viewable1, name='change_viewable1'),
    url(r'^change_viewable2/$', views.change_viewable2, name='change_viewable2'),
    url(r'^change_viewable3/$', views.change_viewable3, name='change_viewable3'),

]
