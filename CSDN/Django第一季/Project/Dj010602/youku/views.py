from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# TYPES = {"1": "普通会员", "2": "高级会员", "3": "管理员"}

# http://127.0.0.1:8000/?username=Alice&type=2

def index(request):

    # 获取查询字符串的数据
    username = request.GET.get('username')
    type = request.GET.get('type')

    # 准备传入的数据
    content = {'user': username, 'type': type}
    return render(request, 'index.html', context=content)


def login(request):
    return render(request, 'login.html')