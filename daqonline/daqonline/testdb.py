#!/usr/bin/python  
#-*-coding:utf-8-*-
# testdb.py --- 
# 
# Description: 
# Author: Hongyi Wu(吴鸿毅)
# Email: wuhongyi@qq.com 
# Created: 四 3月 21 06:43:53 2019 (+0800)
# Last-Updated: 四 3月 21 06:48:20 2019 (+0800)
#           By: Hongyi Wu(吴鸿毅)
#     Update #: 2
# URL: http://wuhongyi.cn 

from django.http import HttpResponse
from TestModel.models import Test
 

# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 
# testdb.py ends here
