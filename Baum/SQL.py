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
# -----------------creat table ---------------------
sql = """
IF OBJECT_ID('{0}', 'U') IS NOT NULL
    DROP TABLE {0}
CREATE TABLE {0} (
    tag_id VARCHAR(10) NOT NULL,
    device_id VARCHAR(10),
    GPS varchar(10),
    date varchar(10))
""".format("hallo")

# create_sqli = "create table hello (id int, name varchar(30));"
cursor.execute(sql)

conn.commit()
#--------------- insert table ---------------------

sql1 = """
insert into hallo(tag_id, device_id, GPS, date) 
select '12314',' sf3424',' 201918' ,'1234'union 
select '34556', 'sdj134', '1238074','asdl'
"""
cursor.execute(sql1)
conn.commit()

#-------------- quuery table ----------------------
sql3 = "select * from hallo"
cursor.execute(sql3)
table = cursor.fetchall()
print(table)


