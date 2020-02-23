#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker
from funktion import create_table
host = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"
mssql = main(host, user, password, database, default_table='hallo_baum2')
create_table('hallo_baum2')
# baums=[
# #     {'device_id': '11111', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.783667', '6.046786', '23', '2'],
# #     {'device_id': '22222', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.784667', '6.042786', '23', '2'],
# #     {'device_id': '3333', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.786667', '6.049786', '23', '2'],
# #     {'device_id': '4444', 'tag_id': 'tagid:28984', 'date': '2019'}, ['50.781667', '6.048786', '23', '2']
#    ]
baums = [
    {'device_id': 'Pi111111', 'tag_id': 'TId:000001', 'date': '2020.03.11 08:32:08', 'GPS': '50.782114, 6.043487, 23, 2'},
    {'device_id': 'Pi222222', 'tag_id': 'TId:000001', 'date': '2020.03.11 09:32:08', 'GPS': '50.783074, 6.044120, 23, 2'},
    {'device_id': 'Pi333333', 'tag_id': 'TId:000001', 'date': '2020.03.11 10:32:08', 'GPS': '50.783392, 6.046476, 23, 2'},
    {'device_id': 'Pi444444', 'tag_id': 'TId:000001', 'date': '2020.03.11 11:32:08', 'GPS': '50.783075, 6.046414, 23, 2'}
        ]
tag_id = 'TId:000001'
delete_table_id(tag_id)
print(baums)
insert_table_batch(baums)
i = query_table_id(tag_id)

for ii in i:
    print(ii)

g = query_table_ele('GPS', '50.783392, 6.046476, 23, 2')
print(g)
gps_map_marker(i)
