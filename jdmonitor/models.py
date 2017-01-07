# coding = utf-8

from django.db import models
import datetime

class Hospital(models.Model):

    def __str__(self):
        return self.hospital_name

    hospital_name = models.CharField(max_length=40, default='', verbose_name="医院名称")
    hospital_id = models.IntegerField(verbose_name="医院id")
    hospital_pacs_hid = models.CharField(max_length=10, default='', verbose_name="医院的pacs_hid")
    last_update_datetime = models.DateTimeField(default=datetime.datetime.strptime(
        '1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'), verbose_name='time of the last update data')


class Engineer(models.Model):

    def __str__(self):
        return self.engineer_name

    engineer_name = models.CharField(max_length=10, verbose_name="工程师名字")
    engineer_phone = models.CharField(max_length=11, verbose_name="工程师电话")
    engineer_email = models.CharField(max_length=40, verbose_name="工程师邮箱")
    hospitals = models.ManyToManyField(Hospital, verbose_name='负责的医院')