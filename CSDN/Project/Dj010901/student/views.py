from django.shortcuts import render, redirect, reverse

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

# 根据提供的sno，筛选出学生
def get_student_by_sno(sno:str):
    # 获取所有学生信息
    path = r"D:\Python\Project\Dj010801\student\static\files\Student.txt"
    students = read_student_from_file(path)
    # 定义和一个集合存储结果
    result = []
    # 遍历所有学生
    for student in students:
        if sno in student['sno']:
            result.append(student)
    # 返回结果
    return result


# ============ 从文件读取用户信息 =============
def read_users_from_file(path:str):
    """
    从文件中读取学生信息
    数据如下： [{}{}{}{}{}]
    :return: 
    """
    # 定义集合存储数据
    users = []
    infos = ['username', 'password', 'status']
    # 读取
    try:
        with open(path, mode='r', encoding='utf-8-sig') as fd:
            current_line = fd.readline()
            while current_line:
                # 切分属性信息
                user = current_line.strip().replace("\n","").split(",")
                # 定义临时集合
                temp_user = {}
                for index in range(len(infos)):
                    temp_user[infos[index]] = user[index]
                # 附加到集合中
                users.append(temp_user)
                # 读取下一行
                current_line = fd.readline()
            # 返回
            return users

    except Exception as e:
        print("读取文件出现异常，具体为：" + str(e))


def user_login(username:str, password:str):
    """
    用户完成身份验证
    :param username: 用户名
    :param password: 密码
    :return: 
    失败：{"result":0, "msg":"用户名不存在！"}
    成功：{"result":1, "msg":null}
    """
    # 读取所有用户
    path = r"D:\Python\Project\Dj010901\student\static\files\user.txt"
    users = read_users_from_file(path)
    # 定义一个返回的结果
    result_dict = {"result":1, 'msg':None}
    # 开始身份验证
    for index in range(len(users)):
        # 判断用户名
        if str(users[index]["username"]).strip().upper() ==  username.strip().upper():
            if users[index]['status'] == '0':
                result_dict["result"] = 0
                result_dict["msg"] = "账号已禁用！"
                break
            elif users[index]["password"] == password:
                break
            else:
                result_dict["result"] = 0
                result_dict["msg"] = "密码错误！"
                break

        # 如果最后一个都验证完了，都没有一样的用户名，返回用户不存在
        if index == len(users) - 1:
            result_dict["result"] = 0
            result_dict["msg"] = "用户名不存在！"

    # 返回
    return result_dict


# ===============Views ================

def index(request):
    """
    展示首页信息
    :param request: 
    :return: 
    """
    # 获取查询字符串内容
    return render(request, 'index.html')

def user_index(request,username):
    # 获取学员信息
    if request.method == "GET":
        path = r"D:\Python\Project\Dj010801\student\static\files\Student.txt"
        students = read_student_from_file(path)
        return render(request, 'index.html', context={'username': username, 'students':students})
    elif request.method == "POST":
        # 获取提交的学号
        sno = request.POST.get("sno")
        print("学号：", sno)
        # 获取查询的结果
        results = get_student_by_sno(sno)
        # 返回
        return render(request, 'index.html', context={
            'username': username, 'students': results, 'querysno':sno})



def detail(request):
    """
    展示学生明细信息
    :param request: 
    :return: 
    """
    # 触发一个查询 --SNo
    sno = request.GET.get('sno')
    username= request.GET.get('username')
    # 查询
    student = get_student_by_sno(sno)

    # 把数据传递到页面
    return render(request, 'detail.html', context={'student': student,'username':username})


def login(request):
    """
    展示登录页面
    :param request: 
    :return: 
    """

    if request.method == "GET":
        # 显示登录页面
        return render(request, 'login.html')

    elif request.method == "POST":
        # 点击登录按钮后执行的事件
        # 获取提交的用户名和密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 进行身份验证
        result = user_login(username,password)
        # 判断,如果失败
        if result['result'] == 0:
            return render(request, 'login.html',
                          context={"msg":result['msg'],"username":username,
                                   'password':password})
        elif result['result'] == 1:
            return redirect(reverse('userindex',kwargs={'username':username}))



