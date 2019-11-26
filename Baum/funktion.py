#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def main(server, user, password, database):
    import Class
    global mssql
    mssql = Class.MSSQL(server, user, password, database)
    return mssql


def create_table(table_name):       # 创建一个定值表

    sql = """
    IF OBJECT_ID('{0}', 'U') IS NOT NULL
        DROP TABLE {0}
    CREATE TABLE {0} (
        id VARCHAR(10) NOT NULL,
        GPS VARCHAR(10),
        date varchar(10),
        PRIMARY KEY(id))
    """.format(table_name)
    mssql.exec_non_query(sql)


def create_table1(baum):        # 根据字典创建列表
    li=['tag_id', 'device_id', 'GPS', 'date']       # 事先约定好表格的列名
    sql = """
    IF OBJECT_ID('{table_name}', 'U') IS NOT NULL
        DROP TABLE {table_name}
    CREATE TABLE {table_name} (
        Num int identity(1,1), 
        {K[0]} VARCHAR(10) NOT NULL,
        {K[1]} VARCHAR(10),
        {K[2]} VARCHAR(10),
        {K[3]} varchar(10))
    """.format(table_name=baum['tag_id'], K=li)
    mssql.exec_non_query(sql)


def drop_table(baum):       # 删除整个列表
    #  complete delete
    sql = "drop table {table_name}" .format(table_name=baum['tag_id'])
    mssql.exec_non_query(sql)


def insert_table(baum):     # 向列表插入值
    sql = """
    insert into {D[tag_id]}(tag_id, device_id, GPS, date) 
    select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
    """.format(D=baum)
    mssql.exec_non_query(sql)


def query_table(baum):
    sql = "select * from {D[tag_id]}".format(D=baum)
    result=mssql.exec_query(sql)
    print(result)


def creat_insert_table(baum):       # 根据字典创建并插入值
    li=['tag_id', 'device_id', 'GPS', 'date']       # 事先约定好表格的列名
    sql = """
    IF OBJECT_ID('{D[tag_id]}', 'U') IS NOT NULL
        insert into {D[tag_id]}(tag_id, device_id, GPS, date) 
        select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
    ELSE
        begin
            CREATE TABLE {D[tag_id]} (
                Num int identity(1,1), 
                {K[0]} VARCHAR(10) NOT NULL,
                {K[1]} VARCHAR(10),
                {K[2]} VARCHAR(10),
                {K[3]} varchar(10))
            insert into {D[tag_id]}(tag_id, device_id, GPS, date) 
            select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
        end
    """.format(table_name=baum['tag_id'], K=li, D=baum)
    mssql.exec_non_query(sql)




# def delete_row(table_name, cursor, row_number='' )
#     if row_number is NULL
#         sql = "delete Nr=max(Nr) from %s where Nr=max(Nr)" % (table_name)




