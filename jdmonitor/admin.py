from django.contrib import admin
from .models import *


class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hospital_id', 'hospital_name', 'hospital_pacs_hid']
    fieldsets = [(None, {'fields': ['hospital_id', 'hospital_name', 'hospital_pacs_hid']})]


# class HospitalInline(admin.StackedInline):
#     model = Hospital
#     extra = 3
#

class EngineerAdmin(admin.ModelAdmin):
    list_display = ['engineer_name', 'engineer_phone', 'engineer_email']
    fieldsets = [(None, {'fields': ['engineer_name', 'engineer_phone', 'engineer_email', 'hospitals']})]


admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Engineer, EngineerAdmin)