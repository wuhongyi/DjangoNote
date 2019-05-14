from django.shortcuts import render


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


# Create your views here.

def index(request):

    # 判断是否是GET方法
    if request.method == "GET":
        # 读取文件信息
        path = r"D:\Python\Project\Dj010801\student\static\files\Student.txt"
        students = read_student_from_file(path)
        # 加载HTML页面
        return render(request, 'index.html', context={'students': students})

    elif request.method == "POST":
        # 获取提交的学号
        sno = request.POST.get("sno",None)
        print("提交的学号:",sno)
        # 执行查询
        result = get_student_by_sno(sno)
        return render(request, 'index.html', context={'students': result})


