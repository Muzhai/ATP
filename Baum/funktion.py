#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# 创建一个数据库连接
def main(server, user, password, database):
    try:
        import Class
        global mssql
        mssql = Class.MSSQL(server, user, password, database)
    except Exception as e:
        print("Connect to the database unsuccessful:", e)
    else:
        print("Connect to the database successful!")
        return mssql


# 创建一个定值表
def create_table(table_name):
    try:
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
    except Exception as e:
        print("Create table unsuccessful:", e)
    else:
        print("Create table successful!")


# 删除整个列表
def drop_table(table_name):
    #  complete delete
    sql = "drop table {table_name}" .format(table_name=table_name)
    mssql.exec_non_query(sql)


# 向默认baum_test表插值，输入格式为一个字典
def insert_table_baum_test(baum, table_name='baum_test'):
    try:
        sql = """
        insert into {table_name}(tag_id, device_id, GPS, date) 
        select '{D[tag_id]}', ' {D[device_id]}', ' {D[GPS]}', '{D[date]}'
        """.format(D=baum, table_name=table_name)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Insert unsuccessful:", e)
    else:
        print("Insert successful!")


# 批量向固定表格插入固定格式数据数据 输入参数为列表格式
def insert_table_batch(baum_list, table_name='baum_test'):
    for baum in baum_list:
        insert_table_baum_test(baum, table_name)


# 输出整个表
def query_table(table_name):
    try:
        sql = "select * from {table_name}".format(table_name=table_name)
        result=mssql.exec_query(sql)
    except Exception as e:
        print("Query unsuccessful:", e)
    else:
        print("Query successful:")
        print(result)


# 按tag_id筛选并按日期排序
def query_table_id(tag_id):
    try:
        sql = """
            select * from baum_test 
            where tag_id = '{0}' 
            order by date""" .format(tag_id)
        result = mssql.exec_query(sql)
    except Exception as e:
        print("Query unsuccessful:", e)
    else:
        print(result)


# 删除某id下的全部行
def delete_table_id(tag_id):
    try:
        sql = """
        delete from baum_test 
        where tag_id ='{0}'
        """ .format(tag_id)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Delete unsuccessful:", e)
    else:
        print("Delete successful!")


# 创建服务器登陆名，用户, 指定默认数据库Baum, 只读
# 前提在数据库中提前创建用户角色
def creat_login_r(username, password):
    sql = """
        EXEC sp_addlogin '{0}','{1}','Baum'
        EXEC sp_adduser '{0}','{0}','Role_r' 
        """.format(username, password)
    mssql.exec_non_query(sql)


# 创建服务器登陆名，用户, 指定默认数据库Baum, 读写
def creat_login_rw(username, password):
    sql = """
        EXEC sp_addlogin '{0}','{1}','Baum'
        EXEC sp_adduser '{0}','{0}','Role_rw' 
        """.format(username, password)
    mssql.exec_non_query(sql)


# # 初始化用户角色 创建只读，读写权限用户角色 Role_rw 和 Role_r
# def creat_user_role():
#     sql="""
#     EXEC sp_addrole 'Role_rw'
#     GRANT SELECT,INSERT ON baum_test TO Role_rw
#     EXEC sp_addrole 'Role_r'
#     GRANT SELECT ON baum_test TO Role_r
#     """
#     mssql.exec_non_query(sql)


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


# def drop_table(baum):       # 删除整个列表
#     #  complete delete
#     sql = "drop table {table_name}" .format(table_name=baum['tag_id'])
#     mssql.exec_non_query(sql)


# def insert_table(baum):     # 向列表插入值 列表名为tag_id
#     sql = """
#     insert into {D[tag_id]}(tag_id, device_id, GPS, date)
#     select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
#     """.format(D=baum)
#     mssql.exec_non_query(sql)



# def query_table(baum):
#     sql = "select * from {D[tag_id]}".format(D=baum)
#     result=mssql.exec_query(sql)
#     print(result)





# def creat_insert_table(baum):       # 根据字典创建并插入值
#     li=['tag_id', 'device_id', 'GPS', 'date']       # 事先约定好表格的列名
#     sql = """
#     IF OBJECT_ID('{D[tag_id]}', 'U') IS NOT NULL
#         insert into {D[tag_id]}(tag_id, device_id, GPS, date)
#         select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
#     ELSE
#         begin
#             CREATE TABLE {D[tag_id]} (
#                 Num int identity(1,1),
#                 {K[0]} VARCHAR(10) NOT NULL,
#                 {K[1]} VARCHAR(10),
#                 {K[2]} VARCHAR(10),
#                 {K[3]} varchar(10))
#             insert into {D[tag_id]}(tag_id, device_id, GPS, date)
#             select '{D[tag_id]}',' {D[device_id]}',' {D[GPS]}', '{D[date]}'
#         end
#     """.format(table_name=baum['tag_id'], K=li, D=baum)
#     mssql.exec_non_query(sql)
#



# def delete_row(table_name, cursor, row_number='' )
#     if row_number is NULL
#         sql = "delete Nr=max(Nr) from %s where Nr=max(Nr)" % (table_name)




