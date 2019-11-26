#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import create_table
from funktion import drop_table
from funktion import insert_table
from funktion import create_table1
from funktion import query_table
from funktion import creat_insert_table
server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"

mssql = main(server, user, password, database)

baum = {'tag_id': 'id00000',
        'device_id': '23did1204',
        'GPS': 'w1820w',
        'date': '56756'
}

baum3 = {'tag_id': 'id00003',
        'device_id': '23did1204',
        'GPS': 'gps333',
        'date': '123456'
}

creat_insert_table(baum3)
query_table(baum3)





# 插值
# key值不存在怎么办

# table_name = 'hallo666'
# create_table(baum)
#
# insert_table(baum)





