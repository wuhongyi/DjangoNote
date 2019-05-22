// readds.cc --- 
// 
// Description: 
// Author: Hongyi Wu(吴鸿毅)
// Email: wuhongyi@qq.com 
// Created: 三 5月 22 22:12:14 2019 (+0800)
// Last-Updated: 三 5月 22 22:18:46 2019 (+0800)
//           By: Hongyi Wu(吴鸿毅)
//     Update #: 4
// URL: http://wuhongyi.cn 

// g++ readds.cc `mysql_config --cflags --libs` -o readds

#include <mysql/mysql.h>
#include <stdio.h>
#include <iostream> 
int main()
{
  MYSQL       *conn;
  MYSQL_RES   *result;
  MYSQL_ROW    row;
  char        *w;
 
  conn = mysql_init(NULL);
  mysql_real_connect(conn, "222.29.111.176", "data", "123456", "monitor", 3306, NULL, 0);
 
  mysql_query(conn, "select * from cool order by ts desc limit 1000");
 
  result = mysql_store_result(conn);
  if (result == NULL) {
    printf("%d:%s\n", mysql_errno(conn), mysql_error(conn));
    goto out;
  }
 
  while ((row = mysql_fetch_row(result))) {
    w = row[0];
    std::cout<<row[0]<<"  "<<row[1]<<"  "<<row[2]<<std::endl;
  }
 
 out:
  mysql_free_result(result);
  mysql_close(conn);
  mysql_library_end();
  // This function finalizes the MySQL library.
  // Call it when you are done using the library (for example, after disconnecting from the server).
  // The action taken by the call depends on whether your application is linked to the MySQL client library or the MySQL embedded server library.
  // For a client program linked against the libmysqlclient library by using the -lmysqlclient flag, mysql_library_end() performs some memory management to clean up.
  
  return 0;
}

// 
// readds.cc ends here
