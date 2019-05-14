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
    # 在url中获取学号
    sno = request.GET.get("sno", None)
    print("学号为：",sno)
    # 判断学号如果有值，执行查询
    if sno:
        results = get_student_by_sno(sno)
        # 展示在页面
        return render(request, 'index.html', context={'students': results})
    # 没有值，返回所有学生信息
    else:
        # 读取文件信息
        path = r"D:\Python\Project\Dj010801\student\static\files\Student.txt"
        students = read_student_from_file(path)
        # 加载HTML页面
        return render(request, 'index.html', context={'students': students})


