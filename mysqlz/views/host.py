from django.shortcuts import render
from mysqlz.models import Host,Mark


def fun_get_host(request,host_id):
    """
    根据host_id找到对应的Host实例
    """
    
