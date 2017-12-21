from django.db import models
from django.utils import timezone

class User(models.Model):
    #属性定义
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=16,default='')         #真实姓名
    nick_name           = models.CharField(max_length=16,default='')         #昵称
    id_card_number      = models.CharField(max_length=18,default='')         #身份证号
    email_addr          = models.EmailField()                                #邮件地址
    mobile_phone        = models.CharField(max_length=11)                    #手机号
    wechat              = models.CharField(max_length=24,default='')         #微信号
    qq                  = models.BigIntegerField(default=0)                  #QQ号
    last_login_datetime = models.DateTimeField(default=timezone.now)         #最近一次登录的日期-时间
    last_ip             = models.GenericIPAddressField (default='0.0.0.0')   #最近一次登录的ip地址
    password            = models.CharField(max_length=24,default='')         #密码
    actived             = models.BooleanField(default=False)                 #是否已经激活

    class Meta(object):
        db_table       = 'user'
        index_together = ['email_addr','password']

    def __str__(self):
        return "user id ={0} ".format(self.id)




