from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("优酷首页！")


def movie(request):
    return HttpResponse("优酷电影首页！")


def movie_detail(request, movie_id, type):
    type_name = ["喜剧片", "动作片", "爱情片", '纪录片', '历史剧']
    return HttpResponse("正在播放电影编号为：%s的电影！ \n 播放的电影类型：%s" %
                        (movie_id,type_name[int(type)]))