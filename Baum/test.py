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
        'GPS': '50.783067, 6.045786',
        'date': '20191127'
}
baum2 = {'tag_id': 'id00001',
        'device_id': 'rgs23451',
        'GPS': '50.783067, 6.047786',
        'date': '20191128'
}
baum3 = {'tag_id': 'id00001',
        'device_id': '23did1204',
        'GPS': '50.783067, 6.049786',
        'date': '20191128'
}
baum4 = {'tag_id': 'id00001',
        'device_id': '34523',
        'GPS': '50.783067, 6.055786',
        'date': '20191127'
}

baum_list=[]
baum_list.extend([baum, baum2, baum3, baum4])

tag_id = 'id00001'
tag_id1 = 'id00002'
tag_id2 = 'id00003'
tag_id3 = 'id00004'
delete_table_id(tag_id)
delete_table_id(tag_id1)
delete_table_id(tag_id2)
delete_table_id(tag_id3)


insert_table_batch(baum_list)
print(query_table_id(tag_id))
print(query_table(table_name))
print(query_table_ele('device_id', 'rgs23451'))




