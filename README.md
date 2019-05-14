<!-- README.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 3月 19 03:27:05 2019 (+0800)
;; Last-Updated: 一 5月 13 21:24:40 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 15
;; URL: http://wuhongyi.cn -->

# README


## install

```bash
pip3 install Django
```

查看安装版本：
```bash
python3 -m django --version
```

## 开发设置

创建项目:
```bash
django-admin startproject xxxxxx
```

确认 Django 项目是否真的创建成功:
```bash
python3 manage.py runserver
#更改监听端口
python manage.py runserver 8080
```

服务器正在运行，浏览器访问 https://127.0.0.1:8000/  
你将会看到一个“祝贺”页面，随着一只火箭发射，服务器已经运行了。

用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍 Python 代码。所以你不需要为了让修改的代码生效而频繁的重新启动服务器。然而，一些动作，比如添加新文件，将不会触发自动重新加载，这时你得自己手动重启服务器。

## 数据库配置

打开 mysite/settings.py 。这是个包含了 Django 项目设置的 Python 模块。

通常，这个配置文件使用 SQLite 作为默认数据库。如果你不熟悉数据库，或者只是想尝试下 Django，这是最简单的选择。Python 内置 SQLite，所以你无需安装额外东西来使用它。

编辑 mysite/settings.py 文件前，先设置 TIME_ZONE 为你自己时区。

此外，关注一下文件头部的 INSTALLED_APPS 设置项。这里包括了会在项目中启用的所有 Django 应用。应用能在多个项目中使用，也可以打包并且发布应用，让别人使用它们。

通常， INSTALLED_APPS 默认包括了以下 Django 的自带应用：
- django.contrib.admin -- 管理员站点， 你很快就会使用它。
- django.contrib.auth -- 认证授权系统。
- django.contrib.contenttypes -- 内容类型框架。
- django.contrib.sessions -- 会话框架。
- django.contrib.messages -- 消息框架。
- django.contrib.staticfiles -- 管理静态文件的框架。
这些应用被默认启用是为了给常规项目提供方便。

默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。请执行以下命令：

```bash
python3 manage.py migrate
```


## superuser

通过命令 python manage.py createw 来创建超级用户

python manage.py createsuperuser



## 介绍

- urls.py
	- 网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。
- views.py
	- 处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
- models.py
	- 与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。
- forms.py
	- 表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作，当然你也可以不使用。	
	
	
- templates 文件夹
- views.py 
	- 中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度。
- admin.py
	- 后台，可以用很少量的代码就拥有一个强大的后台。
- settings.py
	- Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。


- manage.py
	- 项目的交互、管理的文件
- __init__.py
	- 项目运行时自动加载的模块
- settings.py
	- 对项目的配置文件
- urls.py
	- 用来配置URL路由
- wsgi.py
	- 项目部署时候使用


----

## 创建APP

```bash
python3 manage.py startapp  app01
```






<!-- README.md ends here -->
