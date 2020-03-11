#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import query_table_ele


server = "LAPTOP-7SRV1LGC"
username = 'ATPbaum'
key = 'ATPbaum'
database = "Baum"
mssql = main(server, username, key, database)
query_table_ele('device_id', 'rgs23451')

