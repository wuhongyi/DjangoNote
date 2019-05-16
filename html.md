<!-- html.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:55:18 2019 (+0800)
;; Last-Updated: 四 5月 16 22:06:24 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 13
;; URL: http://wuhongyi.cn -->

# HTML

在文件的第一行添加以下内容
```html
{% load staticfiles %}
```

模板语言两种重要符号：
```
{{{   }}}

{%    %}
```


----

## 添加图片等
```html
<div><img src="{% static "imgs/stu04.jpg" %}"></div>
```


```html
<!--加载外部的CSS文件-->
<link type="text/css" rel="stylesheet" href="{% static "css/bootstrap.min.css" %}">
<link type="text/css" rel="stylesheet" href="{% static "css/basic.css" %}">
<!--加载外部的js文件-->
<script src="{% static "js/jquery.min.js" %}"></script>
<script src="{% static "js/login.js" %}"></script>



<link type="text/css" rel="stylesheet"  href="{% static 'css/bootstrap.min.css' %}">
<!-- 导入DataTable的CSS文件 -->
<link type="text/css" rel="stylesheet"  href="{% static 'extranal/datatables/css/jquery.dataTables.css' %}">
<!-- 导入DataTable的js文件 -->
<script src="{% static 'extranal/datatables/js/jquery.js' %}"></script>
<script src="{% static 'extranal/datatables/js/jquery.dataTables.js' %}"></script>
```

## if判断

```html
{% if type == '1' %}
    欢迎您！{{ user }}[普通会员]
{% elif type == '2' %}
    欢迎您！{{ user }}[高级会员]
{% elif type == '3' %}
    欢迎您！{{ user }}[管理员]
{% else %}
     <a href = "{% url 'login' %}">登录</a>
{% endif %}
```



## for循环

```html
<tbody>
    {% for student in allstudent %}
    <tr>
        <td>{{ student.0 }}</td>
        <td>{{ student.1 }}</td>
        <td>{{ student.2 }}</td>
        <td>{{ student.3 }}</td>
        <td>{{ student.4 }}</td>
        <td>{{ student.5 }}</td>
        <td>{{ student.6 }}</td>
    </tr>
    {% endfor %}
</tbody>
```


表格美化

```html
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>学生信息</title>
    <link type="text/css" rel="stylesheet"  href="{% static 'css/bootstrap.min.css' %}">
    <style>
        body{
            margin: 0px;
            padding: 0px;
        }
        #title{
            width:100%;
            height: 100px;
            background-color: yellowgreen;
            font-size:36px;
            line-height: 100px;
            padding-left: 50px;
        }
        #content{
            width:1200px;
            height: 800px;
            margin:10px auto;
            background-color: lightcyan;

        }
        table>thead>tr{
            background-color: #d58512;
        }
    </style>
</head>
<body>
    <div id="title">学员信息</div>
    <div id="content">
        <table class="table table-striped table-bordered table-hover">
            <thead>
                <tr>
                    <th>序号</th>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>性别</th>
                    <th>出生日期</th>
                    <th>手机号码</th>
                    <th>邮箱地址</th>
                    <th>家庭住址</th>
                </tr>
            </thead>
            <tbody>
                {% for student in students %}
                    <tr>
                        <td style="background-color: navy;color:#FFF">{{ forloop.counter }}</td>
                        <td>{{ student.sno }}</td>
                        <td>{{ student.name }}</td>
                        <td>{{ student.gender }}</td>
                        <td>{{ student.birthday }}</td>
                        <td>{{ student.mobile }}</td>
                        <td>{{ student.email }}</td>
                        <td>{{ student.address }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```


DataTables 展示数据
```html
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>学生信息</title>
    <link type="text/css" rel="stylesheet"  href="{% static 'css/bootstrap.min.css' %}">
    <!-- 导入DataTable的CSS文件 -->
    <link type="text/css" rel="stylesheet"  href="{% static 'extranal/datatables/css/jquery.dataTables.css' %}">
    <!-- 导入DataTable的js文件 -->
    <script src="{% static 'extranal/datatables/js/jquery.js' %}"></script>
    <script src="{% static 'extranal/datatables/js/jquery.dataTables.js' %}"></script>

    <style>
        body{
            margin: 0px;
            padding: 0px;
        }
        #title{
            width:100%;
            height: 100px;
            background-color: yellowgreen;
            font-size:36px;
            line-height: 100px;
            padding-left: 50px;
        }
        #content{
            width:1200px;
            height: 800px;
            margin:50px auto;
            background-color: lightcyan;

        }
        table>thead>tr{
            background-color: yellowgreen;
        }
    </style>
    <script>
        $(document).ready( function () {
            $('#student').DataTable({
                language: {
                    "sProcessing": "处理中...",
                    "sLengthMenu": "显示 _MENU_ 项结果",
                    "sZeroRecords": "没有匹配结果",
                    "sInfo": "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
                    "sInfoEmpty": "显示第 0 至 0 项结果，共 0 项",
                    "sInfoFiltered": "(由 _MAX_ 项结果过滤)",
                    "sInfoPostFix": "",
                    "sSearch": "搜索:",
                    "sUrl": "",
                    "sEmptyTable": "表中数据为空",
                    "sLoadingRecords": "载入中...",
                    "sInfoThousands": ",",
                    "oPaginate": {
                        "sFirst": "首页",
                        "sPrevious": "上页",
                        "sNext": "下页",
                        "sLast": "末页"
                    },
                    "oAria": {
                        "sSortAscending": ": 以升序排列此列",
                        "sSortDescending": ": 以降序排列此列"
                    }
                }
            });
        } );
    </script>
</head>
<body>
    <div id="title">使用DataTable展示学员信息</div>
    <div id="content">
        <!--table class="table table-striped table-bordered table-hover"-->
        <table class="table table-striped table-hover table-bordered" id="student">
            <thead>
                <tr>
                    <th>序号</th>
                    <th>学号</th>
                    <th>姓名</th>
                    <th>性别</th>
                    <th>出生日期</th>
                    <th>手机号码</th>
                    <th>邮箱地址</th>
                    <th>家庭住址</th>
                </tr>
            </thead>
            <tbody>
                {% for student in students %}
                    <tr>
                        <td style="background-color: navy;color:#FFF">{{ forloop.counter }}</td>
                        <td>{{ student.sno }}</td>
                        <td>{{ student.name }}</td>
                        <td>{{ student.gender }}</td>
                        <td>{{ student.birthday }}</td>
                        <td>{{ student.mobile }}</td>
                        <td>{{ student.email }}</td>
                        <td>{{ student.address }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```


## 链接跳转

```html
<div id="header_container">
    <div>
        <div><img src="{% static "yk-logo-1220.png" %}"></div>
        <div>
            <ul>
                 <li><a href="/tv/">剧集</a></li>
                 <li><a href="/movie/">电影</a></li>
                 <li><a href="/zy/">综艺</a></li>
            </ul>
        </div>
    </div>
</div>
<div id="content">
    <img src="{% static "index.png" %}">
</div>
```

```html
<div id="header_container">
    <div>
        <div><a href="/"><img src="{% static "yk-logo-1220.png" %}"></a></div>
        <div id="detail">电影首页</div>
    </div>
</div>
<div id="content">
    <img src="{% static "movie.png" %}">
</div>
```

## NAME

```html
{%  load staticfiles %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>youku首页</title>
    <link type="text/css" rel="stylesheet" href="{% static 'css/basic.css' %}">
</head>
<body>
    <div id="title">
        <div>
            <div id="left">优酷首页</div>
            <div id="right"><a href = "{% url 'login' username='Alice' password="88888888" %}">登录</a></div>
        </div>
    </div>
    <div id="bigpic"><img src="{% static "img/index.png" %}"></div>
</body>
</html>
```


## DTL使用变量传值

```html
<body>
    <div id="title">模板语言变量传值</div>
    <div id="div01">当前用户：{{ user }}</div>
    <div id="div02">传递多个值：</div>
</body>


<body>
    <div id="title">模板语言变量传值</div>
    <div id="div01">传递多个值：
        学号：{{ sno }}
        姓名：{{ name }}
        性别：{{ gender }}
        年龄：{{ birthday }}
    </div>
</body>


<body>
    <div id="title">模板语言变量传值</div>
    <div id="div01">传递多个值--- List集合：
        学号：{{ student.0 }}
        姓名：{{ student.1 }}
        年龄：{{ student.2 }}
        生日：{{ student.3 }}
    </div>
</body>


<body>
    <div id="title">模板语言变量传值</div>
    <div id="div01">传递多个值--- dict集合：
        学号：{{ student.sno}}
        姓名：{{ student.name }}
        年龄：{{ student.gender }}
        生日：{{ student.birthday }}
    </div>
</body>


<body>
    <div id="title">模板语言变量传值</div>
    <div id="div01">传递多个值--- 对象：
        学号：{{ student.sno}}
        姓名：{{ student.name }}
        年龄：{{ student.gender }}
        生日：{{ student.birthday }}
    </div>
</body>
```






<!-- html.md ends here -->
