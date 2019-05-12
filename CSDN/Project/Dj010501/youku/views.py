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
    # http://127.0.0.1:8000/?username=alice
    # 获取username
    username = request.GET.get('username')
    if username:
        return render(request, 'index.html')
    else:
        return redirect(reverse('login'))


def tv(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'tv.html')
    else:
        return redirect(reverse('login'))


def movie(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'movie.html')
    else:
        return redirect(reverse('login'))


def zy(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'zy.html')
    else:
        return redirect(reverse('login'))


def denglu(request):
    return render(request, 'denglu.html')

