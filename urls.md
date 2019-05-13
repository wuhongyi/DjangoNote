<!-- urls.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:44:51 2019 (+0800)
;; Last-Updated: 一 5月 13 09:50:47 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
;; URL: http://wuhongyi.cn -->

# URLS

```python
from django.contrib import admin
from django.urls import path

#
from app01 import views as app01_views

```


```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app01_views.index),
    path('student/', app01_views.student),
]


```



<!-- urls.md ends here -->
