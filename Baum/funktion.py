#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 新建表
# 先创建光标


def create_table(table_name, cursor):
    sql = """
    IF OBJECT_ID('%s', 'U') IS NOT NULL
        DROP TABLE %s
    CREATE TABLE %s (
        N VARCHAR(10) NOT NULL,
        GPS VARCHAR(10),
        date varchar(10),
        PRIMARY KEY(N))
    """ %(table_name, table_name, table_name)

    cursor.execute(sql)


def insert_table(table_name, cursor, n, GPS, date):
    sql = "insert into %s values('%s', '%s', '%s')" %(table_name, n, GPS , date )
    cursor.execute(sql)




