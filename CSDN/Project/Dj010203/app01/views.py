from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("优酷首页！")


def movie(request):
    return HttpResponse("优酷电影首页！")


def movie_detail(request, movie_id):
    return HttpResponse("正在播放编号为：%s电影！" % movie_id)