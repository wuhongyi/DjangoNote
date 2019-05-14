from django.shortcuts import render
from django.http import HttpResponse
import pymysql  # 导入pymysql包
from Dj020601.settings import *

# Create your views here.

# ============== 从文件读取学员信息 ========
# 读取文件数据
def read_student_from_file(path:str):
    """
    从文件中读取学生信息
    数据如下： [{}{}{}{}{}]
    :return: 
    """
    # 定义集合存储数据
    students = []
    infos = ['sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address']
    # 读取
    try:
        with open(path, mode='r', encoding='utf-8-sig') as fd:
            current_line = fd.readline()
            while current_line:
                # 切分属性信息
                student = current_line.strip().replace("\n","").split(",")
                # 定义临时集合
                temp_student = {}
                for index in range(len(infos)):
                    temp_student[infos[index]] = student[index]
                # 附加到集合中
                students.append(temp_student)
                # 读取下一行
                current_line = fd.readline()
            # 返回
            return students

    except Exception as e:
        print("读取文件出现异常，具体为：" + str(e))

def index(request):
    """
    调用数据库
    :param request: 
    :return: 
    """
    # python访问MySQL流程
    # 1. 打开数据库连接 -- 服务地址（名称），用户名， 密码， 数据库
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 2. 为连接的对象创建一个游标
    cursor = mysqldb.cursor()
    # 3. 执行一个SQL语句
    sql = "Select Version()"
    cursor.execute(sql)
    # 4. 获取执行的结果
    data = cursor.fetchone()
    # 5. 展示结果
    return HttpResponse("Mysql的版本为：%s" % data)

def create_table(request):
    """
    创建表 
    :param request: 
    :return: 
    """
    # 创建一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 创建一个数据库连接的操作指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = """
          Create Table Student(
          SNO int,
          SName varchar(20) NOT Null,
          Gender varchar(20) NOT Null,
          Birthday date,
          Mobile varchar(20),
          Email varchar(100),
          Address varchar(200),
          CONSTRAINT PK_SNO PRIMARY Key (SNO),
          CONSTRAINT UQ_Mobile UNIQUE (Mobile),
          CONSTRAINT UQ_Email UNIQUE (Email)
          )
          """
    # 执行
    try:
        cursor.execute(sql)
        # 如果没问题，提交
        mysqldb.commit()
        # 成功的提示
        return HttpResponse("创建表成功完成！")
    except Exception as e:
        return HttpResponse("创建表出现异常，具体原因：" + str(e))
    finally:
        # 关闭连接
        mysqldb.close()

def insert01(request):
    """
    向表中写入数据
    :param request: 
    :return: 
    """
    # 创建一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 创建一个数据库连接的操作指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = """
            Insert into Student(SNO,SName,Gender,Birthday,Mobile,Email,Address) VALUES 
            ('95088','陈晓明','男','1990-10-10','13909871234','xiaoming@163.com','上海市闵行区春申路1299号')
          """
    # 执行SQL语句
    try:
        cursor.execute(sql)
        # 如果成功就提交
        mysqldb.commit()
        # 给用户一个反馈
        return HttpResponse("数据插入成功！")
    except Exception as e:
        # 撤销操作
        mysqldb.rollback()
        # 给用户提示
        return HttpResponse("数据插入失败！具体原因：" + str(e))
    finally:
        mysqldb.close()

def insert02(request):

    # 获取文件中的数据
    path = r"D:\Python\Project\Dj020601\app01\static\files\Student.txt"
    students = read_student_from_file(path)

    # 创建一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 创建一个数据库连接的操作指针
    cursor = mysqldb.cursor()

    # 遍历集合
    for student in students:
        # 准备SQL语句
        sql = "Insert into Student (SNO,SName,Gender,Birthday,Mobile,Email,Address) VALUES " \
              "(%s,'%s','%s','%s','%s','%s','%s')" % (student['sno'], student['name'], student['gender'], student['birthday'],
                                                      student['mobile'], student['email'],student['address'])
        # 执行
        try:
            cursor.execute(sql)
            mysqldb.commit()
        except Exception as e:
            mysqldb.rollback()
            return HttpResponse("数据插入失败！具体原因：" + str(e))


    # 反馈
    return HttpResponse("读取文件写入到数据库已完成！")

def update(request):
    """
    修改记录
    :param request: 
    :return: 
    """
    # 创建一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 创建一个数据库连接的操作指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = """
            update Student Set Birthday='1998-08-08' where SNO=95021
          """
    # 执行
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到mysql数据库
        mysqldb.commit()
        # 给用户反馈
        return HttpResponse("修改成功！")
    except Exception as e:
        # 回滚
        mysqldb.rollback()
        # 给用户提示
        return HttpResponse("修改失败，具体原因为：" + str(e))
    finally:
        mysqldb.close()

def delete(request):
    """
    删除表中的某一行记录
    :param request: 
    :return: 
    """
    # 创建一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 创建一个数据库连接的操作指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = """
          Delete from Student Where SNO='95022'
          """
    # 执行
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到mysql数据库
        mysqldb.commit()
        # 给用户反馈
        return HttpResponse("删除成功！")
    except Exception as e:
        # 回滚
        mysqldb.rollback()
        # 给用户提示
        return HttpResponse("删除失败，具体原因为：" + str(e))
    finally:
        mysqldb.close()

def select_all(request):
    """
    获取多条数据 ---- Fetchall
    :param request: 
    :return: 
    """
    # 实例化一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 为连接创建一个操作的指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = "select SNO,SName,Gender,Birthday,Mobile,Email,Address from Student " \
          " where SNO>95015 "
    # 执行
    try:
        # 执行
        cursor.execute(sql)
        # 获取执行的结果
        students = cursor.fetchall() # 返回结果集 （（），（），（），（），）
        # 返回到页面
        return HttpResponse(str(students))
    except Exception as e:
        return HttpResponse("获取数据失败！具体原因：" + str(e))
    finally:
        mysqldb.close()

def select_one(request):
    """
    获取一条数据 --- fetchone
    :param request: 
    :return: 
    """
    # 实例化一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 为连接创建一个操作的指针
    cursor = mysqldb.cursor()
    # 准备SQL语句
    sql = "select SNO,SName,Gender,Birthday,Mobile,Email,Address from Student " \
          " where SNO=95021 "
    # 执行
    try:
        # 执行
        cursor.execute(sql)
        # 获取执行的结果
        student = cursor.fetchone() # 返回结果集 （）
        # 返回到页面
        return HttpResponse(str(student))
    except Exception as e:
        return HttpResponse("获取数据失败！具体原因：" + str(e))
    finally:
        mysqldb.close()




