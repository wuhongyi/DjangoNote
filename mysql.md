<!-- mysql.md --- 
;; 
;; Description: 
;; Author: Hongyi Wu(吴鸿毅)
;; Email: wuhongyi@qq.com 
;; Created: 二 5月 14 22:24:21 2019 (+0800)
;; Last-Updated: 日 5月 19 16:18:44 2019 (+0800)
;;           By: Hongyi Wu(吴鸿毅)
;;     Update #: 11
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

**插入数据**

如果数据是字符型，必须使用单引号或者双引号，如："value"。
```
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

**查询数据**

```
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]
```

- ELECT 命令可以读取一条或者多条记录。
- 可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
- 可以使用 WHERE 语句来包含任何条件。
- 可以使用 LIMIT 属性来设定返回的记录数。
- 可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。

**更新数据**

```
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
```

- 可以同时更新一个或多个字段。
- 可以在 WHERE 子句中指定任何条件。
- 可以在一个单独表中同时更新数据。


**删除数据**

```
DELETE FROM table_name [WHERE Clause]
```

- 果没有指定 WHERE 子句，MySQL 表中的所有记录将被删除。
- 可以在 WHERE 子句中指定任何条件
- 可以在单个表中一次性删除记录。



## 数据类型


## 主键 Primary Key

为了保证某一个字段唯一,不能为空,在一个表中,主键只能有一个

```
create table Student01(
SNO int PRIMARY Key,
SName varchar(20)
)


create table Student02(
SNO int,
SName varchar(20),
CONSTRAINT Pk_SNO PRIMARY Key(SNO)
)


#复合主键
create table BorrowBook(
SNO int,
BookId int,
BorrowDate date,
ReturnDate data,
CONSTRAINT Pk_BorrowBook PRIMARY Key(SNO,BookId)
)
```

## 唯一键 Unique



## 外键 Foreign Key






























<!-- mysql.md ends here -->
