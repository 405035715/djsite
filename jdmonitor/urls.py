from django.conf.urls import url
from . import views

app_name = 'jdmonitor'

urlpatterns = [
    url(r'hospitals/$', views.hospitals_from_jdimage, name='hospitals_from_jdimage'),
    # url(r'update_monitor_data', views.update_monitor_data, name='update_monitor_data')
]