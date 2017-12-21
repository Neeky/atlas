from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View

class UserRegister(View):
    """
    用户注册功能
    """
    def get(self,request):
        """
        url: /users/sign_up/
        引导用户去注册界面
        """
        return render(request,'users/users-sign-up.html',context=None,content_type="text/html")

    def post(self,request):
        """
        url: /users/sign_up/
        用户注册表单数据提交接口、如果成功了把用户引导到“”，
        """
        #print(request.POST)
        return HttpResponse("成功了...")
