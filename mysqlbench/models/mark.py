from django.db import models
from .host import HostInfo

__all__=['BenchCase','BenchCaseInstance']


class BenchCase(models.Model):
    """
    一个BenchCase对应一个测试项
    """
    host_info               = models.ForeignKey(HostInfo,verbose_name='主机配置',related_name='cases',on_delete=models.CASCADE)
    mysql_version           = models.CharField('所测试的mysql版号',max_length=16,default='')
    variable_name           = models.CharField('测试项具体的variable名称',max_length=64,default='')
    bench_type              = models.CharField('测试类型:oltp_insert,oltp_delete ...',max_length=24,default='')
    detail                  = models.CharField('测试项的详细说明',max_length=256,default='')

    class Meta(object):
        unique_together=(
            ('host_info','mysql_version','variable_name','bench_type')
        )

    def __str__(self):
        return "{0}    {1}".format(self.mysql_version,self.variable_name)
 

class BenchCaseInstance(models.Model):
    """
    BenchCaseInstance的每一次测试都对应BenchInstance中的一行
    """
    bench_case              = models.ForeignKey(BenchCase,verbose_name='任务类型',related_name='instances',on_delete=models.CASCADE)
    workers                 = models.PositiveIntegerField('并行度',default=1)
    variable_value          = models.CharField('variable值',max_length=16,default='')
    truncations_per_seconde = models.FloatField('每秒执行完成多少事务',default=0)
    query_per_seconde       = models.FloatField('每秒执行完成多少查询',default=0)
    duration                = models.FloatField('执行完所有事务所用的总时间',default=0)

    class Meta(object):
        unique_together=(
            ('bench_case','variable_value','workers')
        ) 

    def __str__(self):
        return "{0} = {1} workers={2} tps={3}".format(self.bench_case,self.variable_value,self.workers,self.truncations_per_seconde) 

     


