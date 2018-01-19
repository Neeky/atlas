from django.http import HttpResponse,JsonResponse
from django.http.request import QueryDict
from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q

from mysqlbench.models import HostInfo,BenchCase,BenchCaseInstance

from mysqlbench.forms import HostInfoForm,BenchCaseForm,BenchCaseInstanceForm

__all__=['HostInfoAddition','BenchCaseAddition','BenchCaseInstanceAddition','BenchCaseReport','MultiWorkerJsonApi','BenchCaseMultiReport']


class HostInfoAddition(View):
    """
    录入主机信息
    """
    def get(self,request):
        """
        如果是get 方法就引导用户到增加测试结果的页面
        add/host/info/
        """
        return render(request,'mysqlbench/add-host-info.html',context=None,content_type="text/html")

    def post(self,request):
        """
        """
        form = HostInfoForm(request.POST)
        print(request.POST)
        #print(form.cleaned_data['name'])
        if form.is_valid():
            form.save()
            return render(request,'mysqlbench/add-host-info-success.html',context=None,content_type="text/html")
        #return HttpResponse("sucess ...")
        else:
            return HttpResponse(form.cleaned_data)


class BenchCaseAddition(View):
    """
    add/bench/case/
    """
    def get(self,request):
        """
        """
        return render(request,'mysqlbench/add-bench-case.html',context=None,content_type="text/html")

    def post(self,request):
        """
        增加测试用例信息
        1、由request.POST.get('host_info') 得到HostInfo对象
        """
        name = request.POST.get('host_info',None)
        if name != None:
            """
            说明有提交host_info信息、可以进行一下步的处理
            """
            try:
                host_info = HostInfo.objects.get(name=name)
            except HostInfo.DoesNotExist:
                return HttpResponse('HostInfo.name={0} 的主机不存在'.format(name))
            id = host_info.id
            query_dict = request.POST.copy()
            query_dict.setlist('host_info',[id,])
            request.POST=query_dict

        form = BenchCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'mysqlbench/add-bench-case-success.html',context=None,content_type="text/html")
        else:
            print(form.errors)
            return render(request,'mysqlbench/add-bench-case.html',context={'form':form},content_type="text/html")
        

class BenchCaseInstanceAddition(View):
    """
    增加测试用例实例
    """
    def get(self,request):
        """
        """
        return render(request,'mysqlbench/add-bench-case-instance.html',context=None,content_type="text/html")

    def post(self,request):
        """
        录入测试用例实例
        1:由post中的host_info来确认主机的id
        2:加上mysql_version、variable_name、bench_type 来确认benchCase
        3:增加测试用例的实例
        """
        #由主机名转换到id值
        host_info_name = request.POST.get('host_info',None)
        #让request.POST支持读写
        post_data = request.POST.copy()
        request.POST=post_data
        request.POST.pop('host_info')
        #说明host_info是存在的、那么就要从host_info中解析出id值
        if host_info_name != None:
            try:
                host_info=HostInfo.objects.get(name=host_info_name)
            except HostInfo.DoesNotExist:
                return HttpResponse('HostInfo.name={0} 的主机不存在'.format(name))
            host_info_id = host_info.id
            #通过host_info_id,mysql_version,variable_name,bench_type确定bench-case-instance对应的bench-case
            mysql_version=request.POST.get('mysql_version',None)
            request.POST.pop('mysql_version')
            variable_name=request.POST.get('variable_name',None)
            request.POST.pop('variable_name')
            bench_type   = request.POST.get('bench_type',None)
            request.POST.pop('bench_type')
            #获取bench-case
            try:
                bench_case = BenchCase.objects.get(Q(host_info=host_info_id),
                                        Q(mysql_version=mysql_version),Q(variable_name=variable_name),Q(bench_type=bench_type))
            except BenchCase.DoesNotExist:
                return HttpResponse('benchcase 不存在')
            #设置bench-case的值
            request.POST.setlist('bench_case',[bench_case.id])
            form = BenchCaseInstanceForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponse("the end")
            
class BenchCaseReport(View):
    def get(self,request):
        """
        """
        print(request.GET)
        variable_name=request.GET.get('variable_name','test_in_BenchCaseReport(View)')
        return render(request,'mysqlbench/bench-case-report.html',context={ 'variable_name':variable_name},content_type="text/html")

class BenchCaseMultiReport(View):
    def get(self,request):
        """
        """
        print(request.GET)
        variable_name=request.GET.get('variable_name','test_in_BenchCaseReport(View)')
        variable_value=request.GET.get('variable_value','test_in_BenchCaseMultiReport(View)')
        return render(request,'mysqlbench/bench-case-parallel-report.html',context={ 'variable_name':variable_name,'variable_value':variable_value},content_type="text/html")

class BenchCaseJsonApi(View):
    def get(self,request):
        """
        生成报表页面
        """
        result={}
        #先从请求的报文中解析出mysql_version,variable_name
        mysql_version = request.GET.get('mysql_version','mysql-5.7.21')
        variable_name = request.GET.get('variable_name','log_bin')
        #找到对应的benchcase select_related().
        bench_cases = BenchCase.objects.filter(Q(mysql_version=mysql_version),Q(variable_name=variable_name))
        #缓存
        [bc for bc in bench_cases]
        bench_types = [bc.bench_type for bc in bench_cases]
        #填充标题、填充图例
        result['legend1']=bench_types
        result['title1'] ="{0} 各取值对性能的影响程度".format(variable_name)
        #
        variable_values = []
        tpss=[]
        series=[]
        for bc in bench_cases:
            s={}
            s['name']=bc.bench_type
            s['type']='bar'
            s['barMaxWidth']=20
            instance = bc.instances.filter(workers=1)
            variable_values=[i.variable_value for i in instance]
            tpss = [i.truncations_per_seconde for i in instance]
            s['data']=tpss
            series.append(s)
        result['series1']=series
        result['xdata1']=variable_values
        result['ydata1']=tpss
        
        return JsonResponse(result)
        

class MultiWorkerJsonApi(View):
    def get(self,request):
        """
        从get中得到的参数有variable_name,variable_value
        
        """
        result={} 
        variable_name=request.GET.get('variable_name','log_bin')
        variable_value = request.GET.get('variable_value',None) 
        if variable_value == None:
            print('variable_value=None      ----   will set it to off')
            variable_value='off'
        print('this is 1 ------')
        bcs = BenchCase.objects.filter(variable_name=variable_name)
        bench_types = [x.bench_type for x in bcs]
        result['legend']=bench_types
        result['title']="{0}={1} 多线程下的tps表现".format(variable_name,variable_value)
        result['series']=[]
        print('this is 2 ------')
        for bc in bcs:
            serie={'name':bc.bench_type,'type':'line',}
            print('this is 3 ------')
            bcis = BenchCaseInstance.objects.filter(bench_case=bc,variable_value=variable_value).order_by('workers')
            workers = [bci.workers for bci in bcis]
            tps = [bci.truncations_per_seconde for bci in bcis]
            result['workers']=workers
            serie['data']=tps
            result['series'].append(serie)
        print(result)
        return JsonResponse(result)





            





        
        




        

        