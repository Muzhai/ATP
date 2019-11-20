#!/usr/bin/env python
# _*_ coding:utf-8 _*_

host='127.0.0.1'        #defaul IP adress
user='ATPbaum'
password='ATPbaum'
database='Baum'
# creat a connection to the database
conn = pymssql.connect(host, user, password, database, charset='utf8')
cursor = conn.cursor()




