from django.db import models

# Create your models here.

class Host(models.Model):
    """
    Host包含主机的信息还包含MYSQL的版本信息
    """
    name          =models.CharField(max_length=16)
    cpu_cores     = models.IntegerField(default=2)
    memory_size   = models.FloatField(default=4)
    disk_size     = models.FloatField(default=40)
    mysql_release = models.CharField(max_length=64)

    class Meta(object):
        unique_together=(
            ('name','mysql_release')
        )

    def __str__(self):
        return "{0} {1}".format(self.name,self.mysql_release)


class Mark(models.Model):
    """
    Mark用于代表一次Sysbench的跑分信息
    """
    OLTP_BENCH_TYPES = (
        ('delete','oltp_delete'),
        ('insert','oltp_insert'),
        ('point_select','oltp_point_select'),
        ('read_only','oltp_read_only'),
        ('read_write','oltp_read_write'),
        ('update_index','oltp_update_index'),
        ('write_only','oltp_write_only')
    )

    host         = models.ForeignKey(Host,on_delete=models.CASCADE,related_name='marks')
    var_name     = models.CharField('MySQL参数(variable)名',max_length=64,default='')
    var_value    = models.CharField('MySQL参数(variable)值',max_length=64,default='')
    oltp_type    = models.CharField('OLTP 测试类型',max_length=64,choices=OLTP_BENCH_TYPES)
    threads      = models.PositiveIntegerField('并发线程数量',default=1)
    tps          = models.FloatField('tps',default=0),
    qps          = models.FloatField('qps',default=0)

    class Meta(object):
        unique_together=(
            ('host','var_name','var_value','oltp_type','threads')
        )

    def __str__(self):
        return "{0} var_name={1} var_value={2} oltp_type={3} threads={4}".format(self.host.name, 
                self.var_name,self.var_value,self.oltp_type,self.threads)

      





