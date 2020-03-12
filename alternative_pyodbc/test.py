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
mssql = main(host, user, password, database, default_table='hallo_baum')
create_table('hallo_baum')

baums = [
    {'device_id': 'Pi111111', 'tag_id': 'TId:000001', 'date': '2020.03.04 08:32:08', 'GPS': '50.749797, 6.097067, 23, 2'},
    {'device_id': 'Pi222222', 'tag_id': 'TId:000001', 'date': '2020.03.04 14:32:08', 'GPS': '50.750673, 6.098043, 23, 2'},
    {'device_id': 'Pi333333', 'tag_id': 'TId:000001', 'date': '2020.03.10 10:00:08', 'GPS': '50.7866478, 6.1277060, 23, 2'},
    {'device_id': 'Pi333333', 'tag_id': 'TId:000001', 'date': '2020.03.11 11:00:00',
     'GPS': '50.816026, 6.152972, 23, 2'}

        ]
tag_id = 'TId:000001'
delete_table_id(tag_id)
print(baums)
insert_table_batch(baums)
i = query_table_id(tag_id)

for ii in i:
    print(ii)

# g = query_table_ele('GPS', '50.783392, 6.046476, 23, 2')
# print(g)
gps_map_marker(i)
