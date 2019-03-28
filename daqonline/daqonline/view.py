#!/usr/bin/python3  
#-*-coding:utf-8-*-
# view.py --- 
# 
# Description: 
# Author: Hongyi Wu(吴鸿毅)
# Email: wuhongyi@qq.com 
# Created: 二 3月 19 03:38:58 2019 (+0800)
# Last-Updated: 二 3月 19 03:54:01 2019 (+0800)
#           By: Hongyi Wu(吴鸿毅)
#     Update #: 2
# URL: http://wuhongyi.cn 

# from django.http import HttpResponse
 
# def hello(request):
#     return HttpResponse("Hello world ! ")



from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)



# 
# view.py ends here
