from django.contrib import admin
from .models import *


class MonitorTimeAdmin(admin.ModelAdmin):
    list_display = ['monitor_time']
    fieldsets = [(None, {'fields': ['monitor_time']})]


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hospital_id', 'hospital_name', 'hospital_pacs_hid', 'exceptioninterval']
    fieldsets = [(None, {'fields': ['hospital_id', 'hospital_name', 'hospital_pacs_hid', 'monitortimes', 'exceptioninterval']})]


class ExceptionIntervalAdmin(admin.ModelAdmin):
    list_display = ['exception_interval']
    fieldsets = [(None, {'fields': ['exception_interval']})]


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['engineer_name', 'engineer_phone', 'engineer_email']
    fieldsets = [(None, {'fields': ['engineer_name', 'engineer_phone', 'engineer_email', 'hospitals']})]


admin.site.register(MonitorTime, MonitorTimeAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Engineer, EngineerAdmin)
admin.site.register(ExceptionInterval, ExceptionIntervalAdmin)