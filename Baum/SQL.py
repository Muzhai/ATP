#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymssql

host='127.0.0.1'        #defaul IP adress
user='ATPbaum'
password='ATPbaum'
database='Baum'
# creat a connection to the database
conn = pymssql.connect(host, user, password, database, charset='utf8')
cursor = conn.cursor()

table_name='hallo675'
sql = "create table %s ( index varchar(10), GPS varchar(10))" %(table_name)

print(sql)
cursor.execute(sql)

# sql1 = "create table %s ( id varchar(10), GPS varchar(5))" %(table_name)
# print(sql1)
# cursor.execute(sql1)  # 执行Sql语句



# resList = cursor.fetchall()  # 获得所有的查询结果
# print(resList)


# sql1 = "\"create table halloopp ( id varchar(10), GPS varchar(5))\" "
# print(sql1)

# cursor.execute(sql1)
# conn.commit()
