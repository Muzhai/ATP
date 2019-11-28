#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import create_table
from funktion import drop_table

from funktion import insert_table_baum_test

from funktion import query_table
from funktion import query_table1
from funktion import creat_insert_table
from funktion import insert_table_batch
from funktion import query_table_id
server = "127.0.0.1"
user = "ATPbaum"
password = "ATPbaum"
database = "Baum"

mssql = main(server, user, password, database)

table_name= 'baum_test'
create_table(table_name)

baum = {'tag_id': 'id00000',
        'device_id': '23did1204',
        'GPS': 'w1820w',
        'date': '20191127'
}
baum2 = {'tag_id': 'id00000',
        'device_id': 'rgs23451',
        'GPS': 'ry23536',
        'date': '20191128'
}
baum3 = {'tag_id': 'id00003',
        'device_id': '23did1204',
        'GPS': 'gps333',
        'date': '20191128'
}
baum4 = {'tag_id': 'id00003',
        'device_id': '345',
        'GPS': 'gps335436',
        'date': '20191127'
}

baum_list=[]
baum_list.extend([baum, baum2, baum3, baum4])
print(baum_list)

insert_table_batch(baum_list)

query_table1(table_name)
tag_id = 'id00003'
query_table_id(tag_id)                # 默认在表Baum_test里查询

insert_table_batch(baum_list, table_name='hallo')
# 插值
# key值不存在怎么办

# table_name = 'hallo666'
# create_table(baum)
#
# insert_table(baum)


sql6 = """
insert into {baum_test}(tag_id, device_id, GPS, date) 
select '{D[tag_id]}', ' {D[device_id]}', ' {D[GPS]}', '{D[date]}'
""".format(D=baum, baum_test=table_name)

print(sql6)

