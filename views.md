<!-- views.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:51:57 2019 (+0800)
;; Last-Updated: 四 5月 16 21:22:14 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 6
;; URL: http://wuhongyi.cn -->

# views

```python
from django.shortcuts import render

def student(request):
    """
    读取student.csv信息，然后展示在页面中
    :param request: 
    :return: 
    """
    # 获取学生信息
    students = read_from_file(r"D:\python\project\Dj010301\student.csv")
    # 携带数据去加载HTML
    return render(request,"index.html", context={"allstudent":students})
```


## 页面跳转

```python
from django.shortcuts import render
from django.shortcuts import redirect

def index(request): # 首页
    # url记录登录名 --- ? username=alice
    username = request.GET.get("username")
    # 如果获取到username值，直接显示首页，获取不到；调到登录页
    if username:
        return render(request, 'index.html')
    else:
        # 跳转到登录页
        return redirect("/login/")
```

## NAME

```python
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse

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

def zy(request):
    username = request.GET.get('username')
    if username:
        return render(request, 'zy.html')
    else:
        return redirect(reverse('login'))


def denglu(request):
    return render(request, 'denglu.html')
```

```python
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

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
```


## DTL使用变量传值

```python
from django.shortcuts import render
from django.http import HttpResponse

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
```




<!-- views.md ends here -->
