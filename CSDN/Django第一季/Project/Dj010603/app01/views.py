from django.shortcuts import render

# Create your views here.
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
    # 获取文件数据
    path = r"D:\Python\Project\Dj010603\app01\static\files\Student.txt"
    students = read_student_from_file(path)
    # 加载HTML页面
    return render(request,'index.html', context={'students':students})

def dt(request):
    # 获取文件数据
    path = r"D:\Python\Project\Dj010603\app01\static\files\Student.txt"
    students = read_student_from_file(path)
    # 加载HTML页面
    return render(request,'dt.html', context={'students':students})





