#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker

server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"
mssql = main(server, user, password, database)
table_name= 'baum_test'
tag_id = 'tagid:28984'
i = query_table_id(tag_id)

for ii in i:
    print(ii)

gps_map_marker(i)




