from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("优酷首页！")


def tv(request):
    return HttpResponse("优酷电视剧首页！")


def movie(request):
    return HttpResponse("优酷电影首页！")


def yl(request):
    return HttpResponse("优酷娱乐首页！")
