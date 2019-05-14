/* 基本数据准备 */
Select * from Author
Select * from Book
Select * from BookType
Select * from BorrowBook
Select * from Press
Select * from Student 


#  SQL查询基础练习--上 
-- 查询出姓名为“陈鹏”的学号、手机号码和邮箱地址
Select SNO As '学号',MobileNO As '手机号码',StuEmail As'邮箱地址'  # 列筛选
from Student 
Where SName = "陈鹏"  #行筛选， Mysql判断相等一个等号
# Where SName in ("陈鹏")


-- 查询出姓名不是“陈鹏”的学生的所有信息
Select SNO,SName,Sage,Sex,MobileNo,StuEmail
from Student 
Where SName != '陈鹏'
# Where SName <> '陈鹏'
# Where SName Not In ('陈鹏')

-- 查询出学生年龄介于20到30间的学生学号和姓名
Select SNo As '学号', SName As '姓名'
from Student 
Where Sage BETWEEN 20 AND 30
# Where Sage>=20 And Sage<=30

-- 查询哪些学生没有填写“年龄"信息
Select SNo,SName 
from Student 
Where Sage is null 

-- 查询出“陈鹏”,”Alice”,”Bob”的学号，年龄
Select SNO As '学号',Sage As '年龄'
from Student 
Where SName in ('陈鹏','Alice','Bob')
# Where SName='陈鹏' Or SName='Alice' Or SName='Bob'



#  SQL查询基础练习--下
-- 查询出所有姓“陈”的学生
Select SNO As '学号', SName As '姓名'
from Student
where SName Like '陈%'
/*
Mysql中的通配符：
表示任意一个字符：_
表示任意多个字符：%
*/


-- 查询出手机号码134或者135开头，倒数第四位不是8或者9的学生姓名 --- 正则表达式 REGEXP
Select SName As '学生姓名', MobileNo As '手机号码'
from Student 
Where MobileNo REGEXP '^[1][3][45][0-9]{4}[^89][0-9]{3}$'

-- 查询出借过书的同学的学号 --BorrowBook
Select DISTINCT SNO As '借过书的学号'  -- DISTINCT -- 去重功能
from BorrowBook

-- 对Student表按照年龄升序排序，如果年龄一样，女生排在男生前面   --- Order by
Select SNO,SName,Sage,Sex,MobileNO,StuEmail 
from Student 
Order by Sage ASC, Sex ASC  #  ASC--升序  DESC---降序

-- 查询出Student表中的前5行记录 ---Limit 
Select SNO,SName,Sage,Sex,MobileNO,StuEmail 
from Student 
Limit 5

-- # 前五行， 从第三行开始
Select SNO,SName,Sage,Sex,MobileNO,StuEmail 
from Student 
Limit 5 offset 2

-- 在表中任意取五行 --- rand()
Select SNO,SName,Sage,Sex,MobileNO,StuEmail 
from Student 
order by Rand()
LIMIT 5


# =====聚合函数  =========
-- 1.   查询出年龄最大的学生的学号和姓名  (max)
# 错误写法01：
Select SNO,SName 
from Student 
where Sage = max(Sage) # max() 必须要扫描完所有的行才能出结果， 聚合函数不能出现在where

# 错误写法02： 如果结果不止一个，那就出问题 
Select SNO,SName
from Student 
Order by Sage DESC 
LIMIT 1

# 正确写法：
Select SNO,SName 
from  Student
Where Sage =    # 先通过内查询查询出最大的年龄，然后在外面每条记录和这个年龄比较
(
	Select max(Sage)
	from Student
)

-- 2.   查询出男生的平均年龄
Select Avg(Sage) As '男生平均年龄'
from Student 
Where Sex='男'

-- 3.   查询出有多少位学生借书
Select Count(DISTINCT SNO) AS '借书学生人数'  # count--记录的行数
from BorrowBook 


-- 4.   查询出计算机类的图书总共有多少本---   入库量--Book， 类别信息--BookType
Select SUM(BookSumNo) As '计算机类图书量'  # Sum -- 求和
from Book 
where BookTypeId=
(
	Select ID 
	from BookType
	Where TypeName='计算机'
)


#  分组查询 --- Group by -----

-- 统计出男女生的人数
性别  人数
男     10
女     20

Select Sex As '性别', Count(SNO) As '人数'
from Student
Group By Sex

-- 统计出每一类书中的最高的价格
图书类别   最高价格 （Max）
=========================
计算机          56.5
法律            45.2
#  类别名称 ---> BookType    价格 ----》Book
Select BookType.TypeName As '类别名称', T1.maxprice As '最高价格' 
From BookType,
(
		Select BookTypeId, max(BookPrice) AS maxprice
		from Book
		Group By BookTypeId
) As T1
Where BookType.ID = T1.BookTypeId

-- 查询出借的最多的书的ID号 --> 名称
Select BookName AS '借的最多的书的ID号'
From Book 
Where BookId in 
(
  # 获取哪些书借的最多的BooKID
	Select BookId
	from BorrowBook 
	Group By BookId
	Having count(*) = 
	(   # 获取最多借的人数
			Select  Count(*)
			from BorrowBook 
			Group By BookId
			order by Count(*) DESC
			LIMIT 1
	)
)

-- 统计出借书多于两本的学生姓名以及数量，按照数量的降序排列

Select Student.SName AS '学生姓名',T1.BorrowNumber AS'借书数量'
from Student,
	(
		Select SNO,Count(*) As BorrowNumber
		from BorrowBook 
		Group by SNO
		Having Count(*) > 2   # 对分组后的结果进行筛选
		
	) As T1
Where Student.SNO = T1.SNO
Order By T1.BorrowNumber DESC   # Order by 放到查询最外面


# ===== 嵌套查询 ======= 
关键---》每一层只是传递条件或者传递某一个值

-- 查询出陈鹏借了哪些书
# 分析： Student --SNO -->BorrowBook --BookID----> Book
Select BookName As '陈鹏借的书'
From Book 
Where BookId In 
(
	  Select BookId from BorrowBook Where SNO = 
		(
			Select SNO from Student Where SName='陈鹏'
		)
)


-- 查询出借的最多的那本书的作者

# 分析：BorrowBook --BookId ---> Book---AuthorID --> author 
Select AuthorName As '借的最多的书的作者'
from Author
Where AuthorId  in
(
	Select BookAuthor 
	from Book 
	Where BookId in 
	(
		Select BookId 
		from BorrowBook 
		Group By BookId
		Having count(*) = 
		(
			Select Count(*)
			From BorrowBook 
			Group By BookId
			Order By count(*) DESC
			LIMIT 1
		)
	)
)


-- 统计出被借过超过3本（包含3本）的书的名称

Select BookName AS '借的超过三本的书名称'
from Book
Where BookId = any
(
	Select BookId
	from BorrowBook 
	Group by BookId
	Having Count(*)>=3
)

# in  等价于 =any  等价于=some
# any = All 
any --- 在一组数据中只要满足一个就是True 
All --- 在一组数据中必须要满足所有的才是True


Select * 
from Student  
where Sex = '男' And Sage > all
(
	select Sage from Student where Sex='女' and sage is not null
)


# ==================连接查询=================
# 查询出所有图书的ID，图书名称，作者，出版社，价格 
-- 图书ID -- Book    图书名称--> Book  价格-->Book
-- 作者 -- Author 
-- 出版社 --> Press 

Select * from Book ;
Select * from Press ;
Select * from Author ;

Select Book.BookId As '图书编号',Book.BookName As '图书名称', Author.AuthorName As '作者',
			Press.PressName AS '出版社',Book.BookPrice As '价格'
from Book,Press,Author 
Where Book.BookPressId = Press.PressId And Book.BookAuthor = Author.AuthorID

-- 嵌套查询 演示： 查询“陈鹏”借了那些书（BookID， BookName）
# 分析：SNO--->BorrowBook --->Book 
Select BookId,BookName 
from Book 
where BookId in 
(
	Select BookId from BorrowBook  where SNO =
	(
		Select SNO from Student Where SName='陈鹏'
	)
)

-- 使用连接完成
Select Book.BookId As '图书编号', BookName As '图书名称'
from Student,BorrowBook,Book 
Where Student.SNO = BorrowBook.SNO and BorrowBook.BookId=Book.BookID 
			And SName='陈鹏'


# ======================= 内连接 =================
Create table Demo_Student(SNO tinyint,SName Varchar(10));
Insert into Demo_Student (SNO,SNAME) Values(01,'张三');
Insert into Demo_Student (SNO,SNAME) Values(02,'李四');
Insert into Demo_Student (SNO,SNAME) Values(03,'王五');
Create table Demo_Sorce(SNO tinyint,Score tinyint);
Insert into Demo_Sorce(SNO,Score) Values(01,80);
Insert into Demo_Sorce(SNO,Score) Values(02,98);
Insert into Demo_Sorce(SNO,Score) Values(04,89);
Select * from Demo_Student;
Select * from Demo_Sorce;
# ---- 内连接在MysqL中的几种写法 ----
-- 第一种： SQL 92 --
Select * 
from Demo_Student, Demo_Sorce
Where Demo_Student.SNO = Demo_Sorce.SNO
-- 第二种： SQL 99:  --
Select * 
from Demo_Student As T1 INNER JOIN Demo_Sorce As T2 ON T1.SNO = T2.SNO
-- 第三种：Natual 自然连接 (去重，有相同的字段名） ---
Select * 
from Demo_Student NATURAL JOIN Demo_Sorce

-- 第四种：使用Using关键字 (去重，有相同的字段名)---
Select *
from Demo_Student INNER JOIN Demo_Sorce USING(SNO)


# -- 内连接的演示=---

-- 查询出女生借了哪些书？
女生 ---> Student 
借书---》BorrowBook 
书---》图书ID，图书名称 ---》Book
 
-- 标准写法 
Select DISTINCT T3.BookId As '图书编号', T3.BookName As '图书名称'
from Student As T1 
INNER JOIN BorrowBook As T2 on T1.SNO = T2.SNO 
INNER JOIN Book As T3 on T2.BookId = T3.BookId
Where Sex='女'

-- Natual
Select DISTINCT BookId As '图书编号', BookName As '图书名称'
from Student NATURAL Join BorrowBook NATURAL Join Book 
Where Sex='女'

--Using 
Select DISTINCT BookId As '图书编号', BookName As '图书名称'
from Student Inner JOIN BorrowBook USING(SNO) INNER JOIN Book USING(BookId)
Where Sex='女'


-- 查询出被借的书中是北京作者的
# 借书 ----》 BorrowBook 
# 书 --- Book
# 作者 ---Author 

Select DISTINCT T2.BookId As '图书编号', T2.BookName As '图书名称'
From BorrowBook As T1 
Inner Join Book As T2 On T1.BookId = T2.BookId
INNER JOIN Author As T3 On T2.BookAuthor = T3.AuthorID
Where T3.AuthorCity='北京'


--  外连接 -------
Select * from Demo_Student;
Select * from Demo_Sorce;

# 外连接写法01 -- 标准写法
Select * 
From Demo_Student As T1 Left Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO;

# 外连接写法02-- 使用Natural 
Select * 
From Demo_Student NATURAL LEFT JOIN Demo_Sorce

# 外连接写法03-- 使用Using 
Select * 
from Demo_Student Left Outer Join Demo_Sorce Using(SNO)


-- 左连接 ，右连接， 全连接 
Select * 
From Demo_Student As T1 Left Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO;

Select * 
From Demo_Student As T1 Right Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO;

Select * 
From Demo_Student As T1 Left Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO 
UNION  # 合并两个结果集并且去重
Select * 
From Demo_Student As T1 right Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO 

Select * 
From Demo_Student As T1 Left Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO 
UNION All  # 合并两个结果集不去重
Select * 
From Demo_Student As T1 right Outer JOIN Demo_Sorce As T2 on T1.SNO=T2.SNO 


--  === 外连接的演示 ===
-- 查询出哪些书从来没借过书
结果：BookID ,BookName --->Book 
借书----BorrowBook =---》条件
# 使用嵌套查询
Select BookId,BookName
From Book 
Where BookId Not In
(
	Select DISTINCT BookId
	From BorrowBook 
)

# 连接查询实现 
Book--BookID（全部）
BorrowBook ---Book(已经借的)

Select T1.BookID , BookName
from Book As T1 Left Outer Join BorrowBook As T2 on T1.BookId = T2.BookId
Where BorrowDate is NULL


-- 统计出所有书的库存量
图书ID  图书名称  入库量   被借量    库存量 
============================================
39001   Python入门    10      2         8

# 分析：
/*
39001   Python入门    10   ---> Book表 
被借量  ---》 BorrowBook针对Bookid分组统计，
*/

Select T1.BookId As '图书编号',BookName As '图书名称',BooksumNo As '入库量',
				IFNULL(BorrowEd,0) As '被借量', (BooksumNo-IFNULL(BorrowEd,0)) As '库存量'
from Book As T1 LEFT OUTER JOIN 
	(
			Select BookId, Count(*) As Borrowed
			from BorrowBook 
			Group by BookID
   ) As T2 On T1.BookId = T2.BookId



--  =================交叉连接 cross jon ========

Select * from Demo_Student;
Select * from Demo_Sorce;
Select * from Demo_Student Cross Join Demo_Sorce;


Create Table Cross_Student
( 
	SNO int,
	SName varchar(20)
);
Insert into Cross_Student Values(95001,'李明');
Insert into Cross_Student Values(95002,'沈晓霞');
Insert into Cross_Student Values(95003,'陈鹏');
Insert into Cross_Student Values(95004,'李明');
Insert into Cross_Student Values(95005,'朱成平');

Create Table Cross_Course
( 
	CNO int,
	CName varchar(20)
);
Insert into Cross_Course Values(39001,'语文');
Insert into Cross_Course Values(39002,'数学');
Insert into Cross_Course Values(39003,'英语');
Insert into Cross_Course Values(39004,'物理');
Insert into Cross_Course Values(39005,'化学');

Create Table Cross_Result
( 
	SNO int,
	CNO int,
	Sorce int
);
Insert Into Cross_Result Values(95001,39001,87);
Insert Into Cross_Result Values(95001,39003,67);
Insert Into Cross_Result Values(95001,39004,90);
Insert Into Cross_Result Values(95001,39005,49);
Insert Into Cross_Result Values(95002,39002,75);
Insert Into Cross_Result Values(95002,39003,65);
Insert Into Cross_Result Values(95002,39004,80);
Insert Into Cross_Result Values(95002,39005,91);
Insert Into Cross_Result Values(95003,39001,99);
Insert Into Cross_Result Values(95003,39002,42);
Insert Into Cross_Result Values(95003,39003,76);
Insert Into Cross_Result Values(95003,39004,84);
Insert Into Cross_Result Values(95004,39001,87);
Insert Into Cross_Result Values(95004,39002,65);
Insert Into Cross_Result Values(95004,39003,59);
Insert Into Cross_Result Values(95004,39004,89);
Insert Into Cross_Result Values(95004,39005,94);
Insert Into Cross_Result Values(95005,39001,56);
Insert Into Cross_Result Values(95005,39002,89);
Insert Into Cross_Result Values(95005,39004,80);
Insert Into Cross_Result Values(95005,39005,94);

Select * from Cross_Result

# 交叉连接演示： 查询出哪些学生哪些科目缺考
Select * from Cross_Student;
Select * from Cross_Course;
Select * from Cross_Result;
Select count(*) from Cross_Result;

# 先用交叉连接生成所有的学生所有的科目 

Select SName As '学号',CName  As '科目'
from
	(
		Select SNO,CNO,SName,CName from Cross_Student Cross Join Cross_Course
	) As T1 LEFT OUTER JOIN Cross_Result  AS T2 ON T1.SNO = T2.SNO and T1.CNO = T2.CNO 
Where Sorce is NULL

# ===== 自连接 ======= 
create table Employee (ID int, Name varchar(10),ReportID int);
insert into Employee Values (1,'Alice',null);
insert into Employee Values (2,'Bob',1);
insert into Employee Values (3,'Tomas',1);
insert into Employee Values (4,'Tony',2);
insert into Employee Values (5,'Abby',2);
insert into Employee Values (6,'Steven',2);
insert into Employee Values (7,'Candy',3);
insert into Employee Values (8,'Lily',3);

Select * from Employee;

# 统计出公司员工有多少下属
Select ID As '员工编号',name AS '员工姓名',count(*) AS '下属人数'
from
(
	Select T1.ID,T1.Name
	from  Employee As T1 Inner JOIN Employee As T2 on T1.ID = T2.ReportID
) As T3 
Group by  T3.ID,T3.Name



