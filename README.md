<!-- README.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 3月 19 03:27:05 2019 (+0800)
;; Last-Updated: 六 5月 11 21:53:06 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 7
;; URL: http://wuhongyi.cn -->

# README


## install

pip3 install Django


## setting

django-admin startproject daqonline


## superuser

通过命令 python manage.py createw 来创建超级用户

python manage.py createsuperuser


## 开启

python manage.py

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





<!-- README.md ends here -->
