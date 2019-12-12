#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele

server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"
mssql = main(server, user, password, database)


table_name= 'baum_test'

baum = {'tag_id': 'id00001',
        'device_id': '23did1204',
        'GPS': 'w1820w',
        'date': '20191127'
}
baum2 = {'tag_id': 'id00002',
        'device_id': 'rgs23451',
        'GPS': 'ry23536',
        'date': '20191128'
}
baum3 = {'tag_id': 'id00004',
        'device_id': '23did1204',
        'GPS': 'gps333',
        'date': '20191128'
}
baum4 = {'tag_id': 'id00003',
        'device_id': '34523',
        'GPS': 'gps335436',
        'date': '20191127'
}

baum_list=[]
baum_list.extend([baum, baum2, baum3, baum4])

tag_id = 'id00004'
tag_id1 = 'id00001'
tag_id2 = 'id00002'
tag_id3 = 'id00003'
delete_table_id(tag_id)
delete_table_id(tag_id1)
delete_table_id(tag_id2)
delete_table_id(tag_id3)


insert_table_batch(baum_list)
query_table_id(tag_id1)
query_table(table_name)
query_table_ele('device_id', 'rgs23451')




