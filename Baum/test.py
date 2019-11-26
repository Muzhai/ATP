#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from funktion import main
from funktion import create_table
from funktion import drop_table
from funktion import insert_table
from funktion import create_table1
server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"

mssql = main(server, user, password, database)

baum = {'tag_id': 'idt091230',
        'device_id': 'did120401824',
        'GPS': 'w1820w21049e244',
        'date': '56756',
        'sdfs': '1231',
        '234325': '461412'
}
print(list(baum.keys()))
# create_table1(baum)
li=['tag_id', 'device_id', 'GPS', 'date']

# 插值
# key值不存在怎么办
sql = """
        insert into {D[tag_id]}(tag_id, device_id, GPS, date) 
        select {D[tag_id]}, {D[device_id]}, {D[GPS]}, {D[date]} 
        """.format(D=baum)
print(sql)
# table_name = 'hallo666'
# create_table(table_name)
#
# insert_table(table_name, '12313', 'gps', '12345')

print(baum.get('tag_id',0))




