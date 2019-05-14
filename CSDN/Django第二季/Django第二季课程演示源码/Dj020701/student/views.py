from django.shortcuts import render,redirect,reverse
import pymysql
from Dj020701.settings import *
from django.http import HttpResponse
from django.db import transaction
# Create your views here.


# ============== 从文件读取学员信息 ========
FILE_STU_NUMBER = [] # 比如：【30,17,13】
FILE_STUS = []  # 所有学生明细

# 读取文件数据
def read_student_from_file(path:str):
    """
    从文件中读取学生信息
    数据如下： [{}{}{}{}{}]
    :return: 
    """
    # 清空变量
    FILE_STUS.clear()
    # 定义男女生变量
    male_number = 0
    female_number = 0

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
                FILE_STUS.append(temp_student)
                # 判断是男生还是女生
                if  "男" in temp_student["gender"]:
                    male_number += 1
                else:
                    female_number += 1
                # 读取下一行
                current_line = fd.readline()

            # 返回
            # return students
            student_number = len(FILE_STUS)

            # 写入到全局变量中
            FILE_STU_NUMBER.clear()
            FILE_STU_NUMBER.append(student_number)
            FILE_STU_NUMBER.append(male_number)
            FILE_STU_NUMBER.append(female_number)

    except Exception as e:
        print("读取文件出现异常，具体为：" + str(e))

def index(request):
    """
    展示所有的学生数据  --- Fetchall()
    :param request: 
    :return: 
    """
    # 实例化一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 为数据库连接新建一个指针
    cursor = mysqldb.cursor()
    # 定义传递变量
    sno=" "
    sname=" "
    mobile=" "
    email=" "
    # 定义一个sql
    sql = ""
    if request.method == "GET":
        # 准备要执行的sql语句
        sql =   """
                Select SNO,SName,Gender,Birthday,Mobile,Email,Address
                from Student
                """
    elif request.method == "POST":
        # 接受填入的值
        sno = request.POST.get("sno")
        sname = request.POST.get("name")
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        # 准备sql语句
        sql =  "Select SNO,SName,Gender,Birthday,Mobile,Email,Address from Student " \
                "where SNO Like '%s' And SName like '%s' And Mobile like '%s' and " \
               " email like '%s' " % ("%"+sno+"%", "%"+sname+"%", "%"+mobile+"%", "%"+email+"%")

    # 执行语句并且获得返回结果
    try:
        # 执行语句
        cursor.execute(sql)
        # 获取返回结果
        students = cursor.fetchall()  # 返回的结果（（），（），（））
        # 展示数据
        return render(request, 'index.html', context={"students": students, "sno": sno,
                                                      "sname": sname, 'mobile': mobile,  "email": email})

    except Exception as e:
        return HttpResponse("获取数据出现异常，具体原因：" + str(e))
    finally:
        # 关闭连接
        mysqldb.close()

def view(request):
    """
    查看某一个学生的详情
    :param request: 
    :return: 
    """
    # 获取请求的sno
    sno = request.GET.get("sno")

    # 实例化一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 为数据库连接新建一个指针
    cursor = mysqldb.cursor()
    # 准备要执行的sql语句
    sql = "Select SNO,SName,Gender,Birthday,Mobile,Email,Address from Student" \
          " where SNO = %s" % (sno)

    # 执行语句并且获得返回结果
    try:
        # 执行语句
        cursor.execute(sql)
        # 获取返回结果
        student = cursor.fetchone()  # 返回的结果（）
        # 展示数据
        return render(request, 'view.html', context={"student": student})

    except Exception as e:
        return HttpResponse("获取数据出现异常，具体原因：" + str(e))
    finally:
        # 关闭连接
        mysqldb.close()

def modify(request):
    """
    修改学生信息
    :param request: 
    :return: 
    """
    if request.method == "GET":
        # 获取请求的sno
        sno = request.GET.get("sno")

        # 实例化一个数据库连接
        mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
        # 为数据库连接新建一个指针
        cursor = mysqldb.cursor()
        # 准备要执行的sql语句
        sql = "Select SNO,SName,Gender,Birthday,Mobile,Email,Address from Student" \
              " where SNO = %s" % (sno)

        # 执行语句并且获得返回结果
        try:
            # 执行语句
            cursor.execute(sql)
            # 获取返回结果
            student = cursor.fetchone()  # 返回的结果（）
            # 展示数据
            return render(request, 'modify.html', context={"student": student})

        except Exception as e:
            return HttpResponse("获取数据出现异常，具体原因：" + str(e))
        finally:
            # 关闭连接
            mysqldb.close()

    elif request.method == "POST":
        # 取出提交的值
        sno = request.POST.get("sno")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        birthday = request.POST.get("birthday")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("address")

        # 实例化一个数据库连接
        mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
        # 为数据库连接新建一个指针
        cursor = mysqldb.cursor()
        # 准备要执行的sql语句
        sql = "update Student set SName='%s', Gender='%s', Birthday='%s',Mobile='%s',Email='%s',Address='%s'  " \
              "where SNO = %s" % (name, gender, birthday, mobile, email, address, sno)

        # 执行语句并且获得返回结果
        try:
            # 执行语句
            cursor.execute(sql)
            # 写入到数据库
            mysqldb.commit()
            # 返回首页
            return redirect(reverse("index"))
        except Exception as e:
            mysqldb.rollback()
            return HttpResponse("修改出现异常，具体原因：" + str(e))

        finally:
            # 关闭连接
            mysqldb.close()

def add(request):
    """
    添加学生信息
    :param request: 
    :return: 
    """
    #如果页面请求是GET ---> 打开添加学生页面
    if request.method == "GET":
        return render(request, 'add.html')
    # 如果页面为POST---> 是提交学生信息
    elif request.method == "POST":
        # 获取提交的数据
        sno = request.POST.get("sno")
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        birthday = request.POST.get("birthday")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        address = request.POST.get("address")
        # 连接数据库
        # 实例化一个数据库连接
        mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
        # 为数据库连接新建一个指针
        cursor = mysqldb.cursor()
        # 准备要执行的sql语句
        sql = "Insert into Student(SNO,SName,Gender,Birthday,Mobile,Email,Address) Values " \
              "(%s,'%s','%s','%s','%s','%s','%s')" % (sno, name, gender, birthday, mobile, email, address)

        # 执行语句并且获得返回结果
        try:
            # 执行语句
            cursor.execute(sql)
            # 写入到数据库
            mysqldb.commit()
            # 返回首页
            return redirect(reverse("index"))
        except Exception as e:
            mysqldb.rollback()
            return HttpResponse("添加出现异常，具体原因：" + str(e))

        finally:
            # 关闭连接
            mysqldb.close()

def add_many(request):
    """
    批量添加学生
    :param request: 
    :return: 
    """
    if request.method == "GET":
        return render(request, 'addmany.html', context={'info':""})
    if request.method == "POST":
        # 定义一个集合存储sql语句
        sql_list = []
        # 准备SQL语句
        for student in FILE_STUS:
            sql_list.append("Insert into Student(SNO,SName,Gender,Birthday,Mobile,Email,Address)"
                            " Values(%s,'%s','%s','%s','%s','%s','%s')" % (student['sno'], student['name'],
                                                                           student['gender'], student['birthday'],
                                                                           student['mobile'], student['email'],
                                                                           student['address']))
        # 实例化一个数据库连接
        mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
        # 为数据库连接新建一个指针
        cursor = mysqldb.cursor()
        # 执行
        try:

            # 依次执行SQL语句
            for sql in sql_list:
                cursor.execute(sql)

            # 提交
            mysqldb.commit()
            # 跳转到首页
            return redirect(reverse('index'))
        except Exception as e:
            mysqldb.rollback()
            return HttpResponse("添加学生出现异常，具体原因：" + str(e))
        finally:
            mysqldb.close()


def delete(request):
    """
    删除学生信息
    :param request: 
    :return: 
    """
    # 获取删除学生的ID
    sno = request.GET.get("sno")
    # 实例化一个数据库连接
    mysqldb = pymysql.connect(HOST, USER, PASSWORD, DB)
    # 为数据库连接新建一个指针
    cursor = mysqldb.cursor()
    # 准备要执行的sql语句
    sql = "Delete from Student where SNO = %s" %(sno)

    # 执行语句并且获得返回结果
    try:
        # 执行语句
        cursor.execute(sql)
        # 写入到数据库
        mysqldb.commit()
        # 返回首页
        return redirect(reverse("index"))
    except Exception as e:
        mysqldb.rollback()
        return HttpResponse("删除出现异常，具体原因：" + str(e))
    finally:
        # 关闭连接
        mysqldb.close()

def read(request):
    """
    读取文件 
    :param request: 
    :return: 
    """
    # 接受传递的path
    path = request.GET.get('path')
    # 执行文件的读取
    read_student_from_file(path)
    # 展示数据
    return render(request, 'addmany.html' , context={'info':FILE_STU_NUMBER})
