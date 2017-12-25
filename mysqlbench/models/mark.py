from django.db import models
from .host import HostInfo

class TaskInfo(models.Model):
    name = models.CharField('测试任务的名称',max_length=24,default='')
    detail = models.CharField('测试任务的详细内容',max_length=256,default='')

class TestItem(models.Model):
    mysql_version           = models.CharField('mysql版号',max_length=16,default='')
    variable_name           = models.CharField('variable名',max_length=24,default='')
    variable_value          = models.CharField('variable值',max_length=16,default='')
    truncations_per_seconde = models.FloatField('每秒执行完成多少事务',default=0)
    duration                = models.FloatField('执行完所有事务所用的总时间',default=0)
    task_info               = models.ForeignKey(TaskInfo,verbose_name='任务类型')
    host_info               = models.ForeignKey(HostInfo,verbose_name='主机配置')

    class Meta(object):
        unique_together=(
            ('mysql_version','variable_name','variable_value')
        )

        indexes = [
            models.Index(fields=['variable_name','variable_value'],
                                    name='ix_variable_name_value')
        ]

class ParraleTestItem(models.Model):
    workers                = models.PositiveIntegerField('并行度',default=0)
    truncations_per_seconde = models.FloatField('每秒执行完成多少事务',default=0)
    duration                = models.FloatField('执行完所有事务所用的总时间',default=0)
    test_item                = models.ForeignKey(TestItem,verbose_name='测试项')
    


