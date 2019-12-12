#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main

from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import create_login_rw

#----------------------------------1
# create login name with admin_right
# server = "127.0.0.1"
# user = "ATPbaum"
# password = "ATPbaum"
# database = "Baum"
# mssql = main(server, user, password, database)
#
# server = "127.0.0.1"
# username='halloworld'
# key = '123456'
# database = "Baum"
# create_login_rw(username, key)

#-----------------------------------------------2
# remote connect to SQL Server
server = "LAPTOP-7SRV1LGC"
username='halloworld'
key = '123456'
database = "Baum"
mssql = main(server, username, key, database)
query_table_ele('device_id', 'rgs23451')





