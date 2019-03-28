#!/usr/bin/python  
#-*-coding:utf-8-*-
# search.py --- 
# 
# Description: 
# Author: Hongyi Wu(吴鸿毅)
# Email: wuhongyi@qq.com 
# Created: 四 3月 21 06:50:50 2019 (+0800)
# Last-Updated: 四 3月 21 06:51:09 2019 (+0800)
#           By: Hongyi Wu(吴鸿毅)
#     Update #: 1
# URL: http://wuhongyi.cn 

from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# 
# search.py ends here
