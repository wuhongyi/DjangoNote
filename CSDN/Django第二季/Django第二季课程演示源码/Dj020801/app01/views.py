from django.shortcuts import render
import pymysql
from django.http import HttpResponse
from django.db import transaction

# Create your views here.

def index(request):
    """
    批量插入数据
    :param request: 
    :return: 
    """
    mysqldb = pymysql.connect('192.168.182.10', 'root', '1234.Com','TestDB')
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql01 = "Insert into DemoStudent(SNO,SName) Values (95003,'Allen');"
    sql02 = "Insert into DemoStudent(SNO,SName) Values (95004,'Peter');"
    sql03 = "Insert into DemoStudent(SNO,SName Values (95005,'Steven');"

    try:
        # 执行
        cursor.execute(sql01)
        cursor.execute(sql02)
        cursor.execute(sql03)
        # 如果三条都正常执行 ,提交 -- 手工控制
        mysqldb.commit()
        # 返回
        return HttpResponse("添加成功！")
    except Exception as e:
        # 撤销当前进程对数据库的修改
        mysqldb.rollback()
        #
        return HttpResponse("添加学员信息出现异常，具体：" + str(e))
    finally:
        mysqldb.close()

def index01(request):
    """
    批量插入数据
    :param request: 
    :return: 
    """
    mysqldb = pymysql.connect('192.168.182.10', 'root', '1234.Com','TestDB')
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql01 = "Insert into DemoStudent(SNO,SName) Values (95003,'Allen');"
    sql02 = "Insert into DemoStudent(SNO,SName) Values (95004,'Peter');"
    sql03 = "Insert into DemoStudent(SNO,SName Values (95005,'Steven');"

    try:
        # 执行
        with transaction.atomic():
            cursor.execute(sql01)
            cursor.execute(sql02)
            cursor.execute(sql03)
            # 返回
            return HttpResponse("添加成功！")
    except Exception as e:
        return HttpResponse("添加学员信息出现异常，具体：" + str(e))
    finally:
        mysqldb.close()

@transaction.atomic()
def index02(request):
    """
    批量插入数据
    :param request: 
    :return: 
    """
    mysqldb = pymysql.connect('192.168.182.10', 'root', '1234.Com','TestDB')
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql01 = "Insert into DemoStudent(SNO,SName) Values (95003,'Allen');"
    sql02 = "Insert into DemoStudent(SNO,SName) Values (95004,'Peter');"
    sql03 = "Insert into DemoStudent(SNO,SName Values (95005,'Steven');"

    try:
        # 执行
        cursor.execute(sql01)
        cursor.execute(sql02)
        cursor.execute(sql03)
        # 返回
        return HttpResponse("添加成功！")
    except Exception as e:

        return HttpResponse("添加学员信息出现异常，具体：" + str(e))
    finally:
        mysqldb.close()

"""
事务的控制在Django中有两种 
 1. 手工控制 
 2. 自动控制 【写法上有2种】
     commit  rollback  -- 不需要人为写，系统自动控制

"""
