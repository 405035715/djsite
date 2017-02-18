from django.conf.urls import url
from . import views

app_name = 'jdmonitor'

urlpatterns = [
    url(r'hospitals/$', views.hospitals_from_jdimage, name='hospitals_from_jdimage'),
    url(r'api/hospital_engineers', views.hospital_engineers_api, name='hospital_engineers_api'),
    url(r'api/monitor_time_hospitals', views.monitor_time_hospitals_api, name='monitor_time_hospitals_api'),
    url(r'api/all_monitor_time', views.all_monitor_time_api, name='hospitals_all_monitor_time_api'),
]