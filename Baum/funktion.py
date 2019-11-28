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
        tag_id VARCHAR(10) NOT NULL,
        device_id VARCHAR(10),
        GPS varchar(10),
        date varchar(10))
    """.format(table_name)
    mssql.exec_non_query(sql)


# def create_table1(baum):        # 根据字典创建列表
#     li=['tag_id', 'device_id', 'GPS', 'date']       # 事先约定好表格的列名
#     sql = """
#     IF OBJECT_ID('{table_name}', 'U') IS NOT NULL
#         DROP TABLE {table_name}
#     CREATE TABLE {table_name} (
#         Num int identity(1,1),
#         {K[0]} VARCHAR(10) NOT NULL,
#         {K[1]} VARCHAR(10),
#         {K[2]} VARCHAR(10),
#         {K[3]} varchar(10))
#     """.format(table_name=baum['tag_id'], K=li)
#     mssql.exec_non_query(sql)


def drop_table(baum):       # 删除整个列表
    #  complete delete
    sql = "drop table {table_name}" .format(table_name=baum['tag_id'])
    mssql.exec_non_query(sql)


# def insert_table(baum):     # 向列表插入值 列表名为tag_id
#     sql = """
#     insert into {D[tag_id]}(tag_id, device_id, GPS, date)
#     select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
#     """.format(D=baum)
#     mssql.exec_non_query(sql)


def insert_table_baum_test(baum, table_name='baum_test'):     # 向默认baum_test表插值
    sql = """
    insert into {table_name}(tag_id, device_id, GPS, date) 
    select '{D[tag_id]}', ' {D[device_id]}', ' {D[GPS]}', '{D[date]}'
    """.format(D=baum, table_name=table_name)
    mssql.exec_non_query(sql)


def insert_table_batch(baum_list, table_name='baum_test'):              # 批量向固定表格插入固定格式数据数据
    for baum in baum_list:
        insert_table_baum_test(baum, table_name)



def query_table(baum):
    sql = "select * from {D[tag_id]}".format(D=baum)
    result=mssql.exec_query(sql)
    print(result)


def query_table1(table_name):
    sql = "select * from {table_name}".format(table_name=table_name)
    result=mssql.exec_query(sql)
    print(result)


def query_table_id(tag_id):     # 按tag_id筛选并按日期排序
    sql = """
        select * from baum_test 
        where tag_id = '{0}' 
        order by date""" .format(tag_id)
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




