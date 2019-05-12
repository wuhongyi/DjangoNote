from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.


def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse("====优酷首页=====")
    else:
        return redirect(reverse('login', kwargs={'password': 'P@ssw0rd', 'username': 'Alice'}))

    """
    方式01：使用tuple传参数
    return redirect(reverse('login', args=('Alice', 'P@ssw0rd')))
    方式02：使用dict传参数
    return redirect(reverse('login', kwargs={'username':'Alice', 'password':'P@ssw0rd'}))
    """


def login(request, username, password):
    return HttpResponse("用户名：%s \t 密码：%s" % (username, password))


def index01(request):
    return render(request,'index.html')

# URL传值对应的view
def movie_detail01(request, movie_id):
    return HttpResponse("====优酷电影明细:%s=====" % movie_id)


# URL查询字符串传值对应的view
def movie_detail02(request):
    movie_id = request.GET.get('movie_id')
    return HttpResponse("====优酷电影明细:%s=====" % movie_id )
