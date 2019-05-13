<!-- views.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:51:57 2019 (+0800)
;; Last-Updated: 一 5月 13 10:10:12 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
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



<!-- views.md ends here -->
