from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_page

#缓存一小时
@cache_page(60 * 60 * 1)
def main_page(request):
    return render(request,'atlas/atlas.html',context=None,content_type="text/html")