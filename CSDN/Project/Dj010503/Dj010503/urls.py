"""Dj010503 URL Configuration

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
from youku import views as youku_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', youku_views.index, name='home'),
    # URL传值
    path('movie_detail01/<movie_id>/', youku_views.movie_detail01, name='movie_detail01'),
    # URL查询字符串传值
    path('movie_detail02/', youku_views.movie_detail02, name='movie_detail02'),
    # 登录的URL
    path('login/<username>/<password>/', youku_views.login, name='login'),
    # 带有模板的首页
    path('index01/', youku_views.index01, name='index01')

]
