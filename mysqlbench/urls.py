from django.conf.urls import url
from .views import HostInfoAddition,BenchCaseAddition,BenchCaseInstanceAddition,BenchCaseJsonApi,BenchCaseReport,MultiWorkerJsonApi,BenchCaseMultiReport

from django.http import HttpResponse

def index(request,variable_name):
    return HttpResponse("hello {0}".format(variable_name))

urlpatterns = [
    url(r'add/host/info/$', HostInfoAddition.as_view() ,name="add-host-info"),
    url(r'add/bench/case/instance/$',BenchCaseInstanceAddition.as_view(),name='add-bench-case-instance'),
    url(r'add/bench/case/$', BenchCaseAddition.as_view() ,name='add-bench-case'),
    url(r'bench/case/json/data/$',BenchCaseJsonApi.as_view(),name='bench-case-data-api'),
    url(r'bench/case/parallel/json/data/$',MultiWorkerJsonApi.as_view(),name='bench-case-parallel-data-api'),
    url(r'bench/case/report/$',BenchCaseReport.as_view(),name='bench-case-report'),
    url(r'bench/case/parallel/report/$',BenchCaseMultiReport.as_view(),name='bench-case-parallel-report'),

    url(r'report/(?P<variable_name>\w*)/(?P<workers>\d*)/$',BenchCaseReport.as_view()),
    url(r'thread/(?P<variable_name>\w*)/(?P<variable_value>\w*)/',BenchCaseMultiReport.as_view()),
    #url(r'report/')
]