from django.conf.urls import url
from .views import HostInfoAddition,BenchCaseAddition,BenchCaseInstanceAddition

urlpatterns = [
    url(r'add/host/info/$', HostInfoAddition.as_view() ,name="add-host-info"),
    url(r'add/bench/case/instance/$',BenchCaseInstanceAddition.as_view(),name='add-bench-case-instance'),
    url(r'add/bench/case/$', BenchCaseAddition.as_view() ,name='add-bench-case'),
]