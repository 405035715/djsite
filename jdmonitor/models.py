# coding = utf-8

from django.db import models
import datetime
import json


class MonitorTime(models.Model):
    """
    监控时间
    """
    def __str__(self):
        return self.monitor_time.strftime('%H:%M')

    monitor_time = models.TimeField(verbose_name='监控时间')

    class Meta:
        verbose_name = '监控医院数据的时间'


class ExceptionInterval(models.Model):
    """
    医院在一定的时间内没有数据，即为上传影响异常
    """
    def __str__(self):
        return str(self.exception_interval)

    exception_interval = models.IntegerField(verbose_name='n时间内没有数据为异常', null=False, default=60*60)

    class Meta:
        verbose_name = '医院在一定的时间内没有数据，即为上传影响异常'


class Hospital(models.Model):
    """
    医院
    """
    def __str__(self):
        return self.hospital_name

    hospital_name = models.CharField(max_length=40, default='', verbose_name="医院名称")
    hospital_id = models.IntegerField(verbose_name="医院id")
    hospital_pacs_hid = models.CharField(max_length=10, default='', verbose_name="医院的pacs_hid")
    last_update_datetime = models.DateTimeField(default=datetime.datetime.strptime(
        '1970-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'), verbose_name='time of the last update data')
    monitortimes = models.ManyToManyField(MonitorTime, verbose_name='监控时间')
    exceptioninterval = models.ForeignKey(ExceptionInterval, verbose_name='监控医院n秒内没有数据为异常')

    class Meta:
        verbose_name = '医院'


class Engineer(models.Model):
    """
    工程师
    """
    def __str__(self):
        return self.engineer_name

    engineer_name = models.CharField(max_length=10, verbose_name="工程师名字")
    engineer_phone = models.CharField(max_length=11, verbose_name="工程师电话")
    engineer_email = models.CharField(max_length=40, verbose_name="工程师邮箱")
    hospitals = models.ManyToManyField(Hospital, verbose_name='负责的医院')

    class Meta:
        verbose_name = '工程师'


class Mails(models.Model):
    """
    邮件发送记录
    """
    def __str__(self):
        return self.mail_receiver

    mail_receiver = models.CharField(max_length=30, verbose_name="邮件接收者")
    mail_datetime = models.DateTimeField(verbose_name="邮件发送时间")
    mail_type = models.IntegerField(verbose_name="邮件类型：医院上传0；app监控：1")
    mail_content = models.CharField(max_length=300, verbose_name="邮件内容")


class MonitorInterval(models.Model):
    """
    监控的间隔时间(秒)
    """
    def __str__(self):
        return self.monitor_interval

    monitor_interval = models.IntegerField(verbose_name='监控的间隔时间')

    class Meta:
        verbose_name = '监控APP的间隔时间(秒)'