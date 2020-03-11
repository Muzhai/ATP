#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from funktion import main
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id

mssql = main()
baums=[
    {'device_id': '11111', 'tag_id': 'tagid:28984', 'date': '2019', 'GPS': '50.783667, 6.046786, 23, 2' }, 
    {'device_id': '22222', 'tag_id': 'tagid:28984', 'date': '2019', 'GPS': '50.783667, 6.046786, 23, 2'}, 
    {'device_id': '3333', 'tag_id': 'tagid:28984', 'date': '2019', 'GPS': '50.783667, 6.046786, 23, 2'}, 
    {'device_id': '4444', 'tag_id': 'tagid:28984', 'date': '2019', 'GPS': '50.783667, 6.046786, 23, 2'}
    ]


tag_id = 'tagid:28984'
delete_table_id(tag_id)

insert_table_batch(baums)
i = query_table_id(tag_id)
for ii in i:
    print(ii)

