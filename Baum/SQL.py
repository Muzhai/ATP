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

baum = {'tag_id': 'idt091230',
        'device_id': 'did1204',
        'GPS': 'w1820w21',
        'date': '56756'
}
print(list(baum.keys()))
# create_table1(baum)
li=['tag_id', 'device_id', 'GPS', 'date']

sql = """
insert into {D[tag_id]}(tag_id, device_id, GPS, date) 
select '{D[tag_id]}', '{D[device_id]}', '{D[GPS]}', '{D[date]}' 
""".format(D=baum)
print(sql)
cursor.execute(sql)  # 执行Sql语句
conn.commit()





# resList = cursor.fetchall()  # 获得所有的查询结果
# print(resList)


# sql1 = "\"create table halloopp ( id varchar(10), GPS varchar(5))\" "
# print(sql1)

# cursor.execute(sql1)
# conn.commit()
