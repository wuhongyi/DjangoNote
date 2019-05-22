#!/usr/bin/python3  
#-*-coding:utf-8-*-
# readds.py --- 
# 
# Description: 
# Author: Hongyi Wu(吴鸿毅)
# Email: wuhongyi@qq.com 
# Created: 三 5月 22 22:25:46 2019 (+0800)
# Last-Updated: 三 5月 22 22:29:09 2019 (+0800)
#           By: Hongyi Wu(吴鸿毅)
#     Update #: 2
# URL: http://wuhongyi.cn 

import MySQLdb

#连接
cxn = MySQLdb.Connect(host = '222.29.111.176', user = 'data', passwd = '123456')
#游标
cur = cxn.cursor()

# try:
#     cur.execute("DROP DATABASE PyTest")
# except Exception as e:
#     print(e)
# finally:
#     pass

#创建数据库
# cur.execute("CREATE DATABASE PyTest")
cur.execute("USE monitor")

#创建表
# cur.execute("CREATE TABLE users (id INT, name VARCHAR(8))")

#插入
# cur.execute("INSERT INTO users VALUES(1, 'Tina'),(2, 'Tom'),(3, 'Tony'),(4, 'sala')")

#查询
cur.execute("select * from cool order by ts desc limit 1000")
for row in cur.fetchall():
    print('%s\t%s\t%s' %row)

#关闭
cur.close()
cxn.commit()
cxn.close()


# 
# readds.py ends here
