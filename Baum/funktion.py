#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 新建表
# 先创建光标


def create_table(table_name, cursor):
    sql = """
    IF OBJECT_ID('%s', 'U') IS NOT NULL
        DROP TABLE %s
    CREATE TABLE %s (
        index VARCHAR(10) NOT NULL,
        GPS VARCHAR(10),
        date varchar(10),
        PRIMARY KEY(N))
    """ %(table_name, table_name, table_name)

    cursor.execute(sql)


def insert_table(table_name, cursor, index, GPS, date):
    sql = "insert into %s values('%s', '%s', '%s')" %(table_name, index, GPS , date )
    cursor.execute(sql)


def drop_table(table_name, cursor):
    #  complete delete
    sql = "drop table %s" %(table_name)
    cursor.execute(sql)
    conn.commit()


def delete_row(table_name, cursor, row_number='' )
    if row_number is NULL
        sql = "delete Nr=max(Nr) from %s where Nr=max(Nr)" % (table_name)






