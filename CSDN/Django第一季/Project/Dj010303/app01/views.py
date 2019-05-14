from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request): # 首页
    # url记录登录名 --- ? username=alice
    username = request.GET.get("username")
    # 如果获取到username值，直接显示首页，获取不到；调到登录页
    if username:
        return render(request, 'index.html')
    else:
        # 跳转到登录页
        return redirect("/login/")


def tv(request): # 电视剧
    return render(request,'tv.html')


def movie(request): # 电影
    return render(request,'movie.html')


def zy(request): # 综艺
    return render(request,'zy.html')


def login(request): # 登录
    return render(request,'login.html')