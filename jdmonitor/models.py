from django.db import models


class JdMonitor(models.Model):

    def __str__(self):
        return self.hospital_name

    hospital_name = models.CharField(max_length=40, verbose_name="医院名称")
    last_update_datetime = models.DateTimeField(verbose_name='time of the last update data')
