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

baum = {'tag_id': 'id00001',
        'device_id': '23did1204',
        'GPS': '50.783067, 6.045786',
        'date': '20191126'
}
baum2 = {'tag_id': 'id00001',
        'device_id': 'rgs23451',
        'GPS': '50.785067, 6.047786',
        'date': '20191128'
}
baum3 = {'tag_id': 'id00001',
        'device_id': '23did1204',
        'GPS': '50.783667, 6.049786',
        'date': '20191129'
}
baum4 = {'tag_id': 'id00001',
        'device_id': '34523',
        'GPS': '50.783067, 6.055786',
        'date': '20191127'
}

baum_list = []
baum_list.extend([baum, baum2, baum3, baum4])

tag_id = 'id00001'
delete_table_id(tag_id)

insert_table_batch(baum_list)

print(query_table(table_name))
print(query_table_ele('device_id', 'rgs23451'))

i = query_table_id(tag_id)
gps_map_marker(i)


