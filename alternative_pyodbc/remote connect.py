#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker

server = "LAPTOP-7SRV1LGC"
username = 'ATPbaum'
key = 'ATPbaum'
database = "Baum"
mssql = main(server, username, key, database)
query_table_ele('device_id', 'rgs23451')

