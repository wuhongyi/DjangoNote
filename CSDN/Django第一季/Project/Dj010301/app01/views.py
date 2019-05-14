
# 方式01使用的加载
from django.template.loader import render_to_string
from django.http import HttpResponse
# 方式02使用的加载
from django.shortcuts import render


def read_from_file(path:str):
    """
    # 读取文件信息存储到List中
    ---【【】，【】，【】，。。。】
    :param path: 
    :return: 
    """
    # 定义一个集合
    students = []

    try:
        with open(path, mode="r", encoding="utf-8-sig") as fd:
            # 读取第一行
            current_line = fd.readline()
            # 判断数据是否存在
            while current_line:
                # 分割数据
                student_info = current_line.strip().replace("\n","").split(",")
                # 附加到集合中
                students.append(student_info)
                # 读取下一行
                current_line = fd.readline()
    except Exception as e:
        print("读取文件出现异常！具体原因：" + str(e))

    # 返回数据
    return students

# Create your views here.

# 返回HTML给用户两种方式
# 方式01： 使用 render_to_string
# 方式02： 使用 render
def index(request):
    """
    方式01：
    html = render_to_string("index.html")
    return HttpResponse(html)
    """
    # 方式02：
    return render(request, "index.html")

def student(request):
    """
    读取student.csv信息，然后展示在页面中
    :param request: 
    :return: 
    """
    # 获取学生信息
    students = read_from_file(r"D:\python\project\Dj010301\student.csv")
    # 携带数据去加载HTML
    return render(request,"index.html", context={"allstudent":students})


