from django.http import HttpResponse
from django.shortcuts import render,redirect

def main_page(request):
    return render(request,'atlas/atlas.html',context=None,content_type="text/html")