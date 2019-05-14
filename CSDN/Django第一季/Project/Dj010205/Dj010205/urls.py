"""Dj010205 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from app01 import views as app01views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app01views.index),
    path('movie/', app01views.movie),
    #path('movie/detail/<int:movie_id>/', app01views.movie_detail),
    re_path('movie/detail/(?P<movie_id>[9][5]\d{4})/(?P<type>[0-4])',app01views.movie_detail)
]

# 编号必须要是6位数字
# 必须要是95开头的6位数字
