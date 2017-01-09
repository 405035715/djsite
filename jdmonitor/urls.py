from django.conf.urls import url
from . import views

app_name = 'jdmonitor'

urlpatterns = [
    url(r'hospitals/$', views.hospitals_from_jdimage, name='hospitals_from_jdimage'),
]