<!-- mysql.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 5月 14 22:24:21 2019 (+0800)
;; Last-Updated: 日 5月 19 15:06:08 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 8
;; URL: http://wuhongyi.cn -->

# MySQL

> https://www.runoob.com/mysql/mysql-tutorial.html   
> https://www.cnblogs.com/adjk/p/6660453.html  
> https://www.runoob.com/mysql/mysql-administration.html


----

```bash
mysql -u root -p

#输入root密码
```

```
#创建一个普通用户 data ，密码是 123456
CREATE USER 'data'@'%' IDENTIFIED BY '123456';

#给这个用户授予 SELECT,INSERT,UPDATE,DELETE 的远程访问的权限，这个账号一般用于提供给实施的系统访问
GRANT SELECT,INSERT,UPDATE,DELETE  ON *.* TO 'data'@'%';


#创建一个管理员用户 admin 账号 ，密码是 123456
CREATE USER 'admin'@'%' IDENTIFIED BY '123456';

#给这个用户授予所有的远程访问的权限。这个用户主要用于管理整个数据库、备份、还原等操作。
GRANT ALL  ON *.* TO 'admin'@'%';


#使授权立刻生效
flush privileges;
```

**创建数据库\创建数据表需要 admin 帐号**


## 创建数据库

```
create database TestDB;  #默认的方式创建数据库
create database TestDB default character set utf8; #默认的方式创建数据库 使用utf8
create database if not exists TestDB;  #如果TestDB不存在就创建
create database if not exists TestDB default character set utf8;
```


```
# 查看所有数据库
SHOW DATABASES;

#选择要操作的Mysql数据库，使用该命令后所有Mysql命令都只针对该数据库。
USE 数据库名

#例如 use TestDB;
```


## 创建表

```
create table student
(
sno int,
name varchar(20),
gender varchar(10),
birthday date,
mobile varchar(20),
email varchar(50),
homeaddress varchar(100)
);
```

```
#显示指定数据库的所有表，使用该命令前需要使用 use 命令来选择要操作的数据库。
SHOW TABLES;


#显示数据表的属性，属性类型，主键信息 ，是否为 NULL，默认值等其他信息。
SHOW COLUMNS FROM 数据表;


#显示数据表的详细索引信息，包括PRIMARY KEY（主键）。
SHOW INDEX FROM 数据表;
```

## 数据类型





<!-- mysql.md ends here -->
