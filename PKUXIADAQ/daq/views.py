from django.shortcuts import render, redirect, reverse

# Create your views here.

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
    path = r"daq/static/files/user.txt"
    users = read_users_from_file(path)
    # 定义一个返回的结果
    result_dict = {"result":1, 'msg':None}
    # 开始身份验证
    for index in range(len(users)):
        # 判断用户名
        if str(users[index]["username"]).strip().upper() ==  username.strip().upper():
            if users[index]['status'] == '0':
                result_dict["result"] = 0
                result_dict["msg"] = "Account is disabled !"
                break
            elif users[index]["password"] == password:
                break
            else:
                result_dict["result"] = 0
                result_dict["msg"] = "Wrong password !"
                break

        # 如果最后一个都验证完了，都没有一样的用户名，返回用户不存在
        if index == len(users) - 1:
            result_dict["result"] = 0
            result_dict["msg"] = "Username does not exist !"

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
    return render(request, 'index.html', context={'pageindex':'-1'})

def user_index(request,username):
    # 登陆后转到首页
    if request.method == "GET":
        return render(request, 'index.html', context={'username': username,'pageindex':'-1'})
    elif request.method == "POST":
    # 提交之后转到
        # sno = request.POST.get("sno")
        return render(request, 'index.html', context={'username': username,'pageindex':'-1'})
        
def control(request):
    return render(request, 'control.html', context={'pageindex':'0'})

def offline(request):
    return render(request, 'offline.html', context={'pageindex':'1'})

def online(request):
    return render(request, 'online.html', context={'pageindex':'2'})

def others(request):
    return render(request, 'others.html', context={'pageindex':'3'})
    



    
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

