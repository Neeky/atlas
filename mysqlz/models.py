from django.db import models

# Create your models here.

class HostInfo(models.Model):
    name        =models.CharField(max_length=16)
    cpu_core    = models.IntegerField(default=2)
    memory_size = models.FloatField(default=4)
    disk_size   = models.FloatField(default=40)
    mysql_version = models.CharField(max_length=64)

    class Meta(object):
        unique_together=(
            ('name','mysql_version')
        )

    def __str__(self):
        return self.name


class TestItem(models.Model):
    host_info      = models.ForeignKey(HostInfo,on_delete=models.CASCADE)
    variable_name  =models.CharField(max_length=64 , default='')
    variable_value =models.CharField(max_length=64, default='')
    oltp_type      = models.CharField(max_length=24,default='')
    detail         =models.CharField(max_length=128,default='')

    def __str__(self):
        return "HostInfo.id = {0} variable_name={1} variable_value={2} oltp_type={3}".format(self.host_info,
                self.variable_name,self.variable_value,self.oltp_type)

    class Meta(object):
        unique_together=(
            ('host_info','variable_name','variable_value','oltp_type')
        )



class TestMark(models.Model):
    test_item=models.ForeignKey(TestItem,on_delete=models.CASCADE)
    parallelism=models.IntegerField(default=1)
    tps=models.FloatField(default=0)
    qps=models.FloatField(default=0)

    def __str__(self):
        return "TestItem.id = {0} parallelism = {1} tps = {2} qps ={3} ".format(self.test_item,
                self.parallelism,self.tps,self.qps)

    class Meta(object):
        unique_together=(
            ('test_item','parallelism')
        )




