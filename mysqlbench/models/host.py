from django.db import models

class HostInfo(models.Model):
    name     = models.CharField('主机名(阿里云最小配置)',max_length=24,default='',unique=True)
    os       = models.CharField(max_length=16,default='')
    cores    = models.PositiveIntegerField('cpu 核心数',default=0)
    memorys = models.PositiveIntegerField('内存大小 MB',default=0)
    disks    = models.PositiveIntegerField('数据盘大小 MB',default=0)
    is_log_ssd  = models.BooleanField('日志盘是否是ssd',default=False)
    is_data_ssd = models.BooleanField('数据盘是否是ssd',default=False)

    class Meta(object):
        unique_together=(
            ('os','cores','memorys','disks','is_log_ssd','is_data_ssd')
        )

    def __str__(self):
        return "{0}".format(self.name)