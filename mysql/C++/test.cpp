// test.cpp --- 
// 
// Description: 
// Author: Hongyi Wu(吴鸿毅)
// Email: wuhongyi@qq.com 
// Created: 三 5月 22 10:02:01 2019 (+0800)
// Last-Updated: 三 5月 22 22:10:58 2019 (+0800)
//           By: Hongyi Wu(吴鸿毅)
//     Update #: 10
// URL: http://wuhongyi.cn 

// g++ test.cpp `mysql_config --cflags --libs` -o test

#include <stdio.h>
#include <mysql/mysql.h>

int main(int argc,char *argv[])
{
  MYSQL conn;
  int res;
  
  mysql_init(&conn);
  if(mysql_real_connect(&conn,"localhost","data","123456","TestDB",0,NULL,CLIENT_FOUND_ROWS)) //"data":数据库管理员 "12346":root密码 "TestDB":数据库的名字
    {
      printf("connect success!\n");
      res=mysql_query(&conn,"insert into student values(124,'wang wu','male','2017-06-17','14745691234','45746798@qq.com','gfgqwwetryrtyrgfg')");
      if(res)
	{
	  printf("error\n");
	}
      else
	{
	  printf("OK\n");
	}
      mysql_close(&conn);
    }
  return 0;
}

// 
// test.cpp ends here
