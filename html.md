<!-- html.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:55:18 2019 (+0800)
;; Last-Updated: 一 5月 13 13:29:35 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 5
;; URL: http://wuhongyi.cn -->

# HTML

在文件的第一行添加以下内容
```html
{% load staticfiles %}
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
```



## 循环显示数据

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




<!-- html.md ends here -->
