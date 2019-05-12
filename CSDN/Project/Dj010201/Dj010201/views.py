from django.http import HttpResponse


def index(request):
    """
    View中函数
    :param request: 
    :return: 
    """
    return HttpResponse("优酷首页！")

def movie(request):
    return HttpResponse("优酷电影页面！")

def tv(request):
    return HttpResponse("优酷电视剧页面！")

def yl(request):
    return HttpResponse("优酷娱乐页面！")
