<!-- html.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:55:18 2019 (+0800)
;; Last-Updated: 一 5月 13 10:02:28 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 2
;; URL: http://wuhongyi.cn -->

# HTML

在文件的第一行添加以下内容
```html
{% load staticfiles %}
```

----

添加图片
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



循环显示数据
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

<!-- html.md ends here -->
