from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # 获取登录的用户名
    username = request.GET.get('username')
    if username:
        # 如果想把值传到Templates中， 必须传递字典类型
        # {‘user’:username}  -- user: 在模板中通过这个名称访问， username： 具体传过去的值
        content = {'user': username}
        return render(request, 'index.html', context=content)
    else:
        return HttpResponse("没有用户登录！！！")


def index02(request):

    # 传多个值：学号，姓名，性别，出生日期
    sno = '95001'
    name = '张三'
    gender = '男'
    birthday = '1990-10-10'
    # 把多个值拼接成字典类型
    content = {'sno': sno,'name':name, 'gender': gender, 'birthday':birthday}

    # 加载HTML时候附带数据
    return render(request, 'index02.html',context=content)


def index03(request):
    # 传递List集合
    alice = ['95001', 'alice', '女', '1990-10-10']

    return render(request,'index03.html', context={'student':alice})

def index04(request):
    # 传递的是字典类型
    alice = {'sno':'95001', 'name':'alice', 'gender':'女', 'birthday':'1990-10-10'}
    return render(request, 'index04.html', context={'student': alice})


# 定义个类
class Student:
    def __init__(self,sno,name,gender,birthday):
        self.sno = sno
        self.name = name
        self.gender = gender
        self.birthday = birthday

def index05(request):
    # 传递一个对象
    alice = Student('98008','张三','男','1998-9-8')
    return render(request, 'index05.html', context={'student': alice})