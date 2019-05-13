<!-- code.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 一 5月 13 09:52:37 2019 (+0800)
;; Last-Updated: 一 5月 13 09:58:22 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 1
;; URL: http://wuhongyi.cn -->

# CODE

```python
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
```










<!-- code.md ends here -->
