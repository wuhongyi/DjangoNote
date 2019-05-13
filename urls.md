<!-- urls.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:44:51 2019 (+0800)
;; Last-Updated: 一 5月 13 16:26:29 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 4
;; URL: http://wuhongyi.cn -->

# URLS

```python
from django.contrib import admin
from django.urls import path
from app01 import views as app01_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app01_views.index),
    path('student/', app01_views.student),
]
```


## NAME

```python
from django.contrib import admin
from django.urls import path
from youku import views as youku_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', youku_views.index),
    path('tv/', youku_views.tv),
    path('movie/', youku_views.movie),
    path('zy/', youku_views.zy),
    path('signin/', youku_views.denglu, name='login'),
]
```


## 多APP

```python
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('tv/', include("tv.urls")),
    path('movie/', include("movie.urls")),
]
```











<!-- urls.md ends here -->
