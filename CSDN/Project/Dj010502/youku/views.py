from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

# Create your views here.


def index(request):
    """
    优酷首页
    :param request: 
    :return: 
    """
    return render(request, 'index.html')


def tv(request):
    return render(request, 'tv.html')


def movie(request):
    return render(request, 'movie.html')


def zy(request):
    return render(request, 'zy.html')


def denglu(request):
    return render(request, 'denglu.html')

