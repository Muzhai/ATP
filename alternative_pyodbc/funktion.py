#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# connect to server
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


# create a table tag_id, device_id, GPS, date
def create_table(table_name):
    try:
        sql = """
        IF OBJECT_ID('{0}', 'U') IS NOT NULL
            DROP TABLE {0}
        CREATE TABLE {0} (
            tag_id VARCHAR(100) NOT NULL,
            device_id VARCHAR(100),
            GPS varchar(100),
            date varchar(100))
        """.format(table_name)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Create table unsuccessful:", e)
    else:
        print("Create table successful!")


# delete table
def drop_table(table_name):
    #  complete delete
    sql = "drop table {table_name}" .format(table_name=table_name)
    mssql.exec_non_query(sql)


# insert to table baum_test; baum_test is a default table; 'baum' is a dictionary
def insert_table(baum, table_name='baum_test'):
    try:
        sql = """
        insert into {table_name}(tag_id, device_id, GPS, date) 
        select '{D[tag_id]}', '{D[device_id]}', '{D[GPS]}', '{D[date]}'
        """.format(D=baum, table_name=table_name)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Insert '{D[tag_id]}' to baum_test unsuccessfully:".format(D=baum), e)
    else:
        print("Insert '{D[tag_id]}' to baum_test successfully!".format(D=baum))


# insert batch data to table; 'baum_list' is a list
def insert_table_batch(baum_list, table_name='baum_test'):
    for baum in baum_list:
        insert_table(baum, table_name)


# read table total
def query_table(table_name):
    try:
        sql = "select * from {table_name}".format(table_name=table_name)
        result=mssql.exec_query(sql)
    except Exception as e:
        print("Query '{table_name}' unsuccessfully:".format(table_name=table_name), e)
    else:
        print("Query '{table_name}' successfully!".format(table_name=table_name))
        return result


# query table with tag_id and order by data
def query_table_id(tag_id):
    try:
        sql = """
            select * from baum_test 
            where tag_id = '{tag_id}' 
            order by date""" .format(tag_id=tag_id)
        result = mssql.exec_query(sql)
    except Exception as e:
        print("Query '{tag_id}' unsuccessfully:".format(tag_id=tag_id), e)
    else:
        print("Query '{tag_id}' successfully!".format(tag_id=tag_id))
        return result


# query table with some table element and its target
def query_table_ele(table_ele, target):
    try:
        sql = """
            select * from baum_test 
            where {table_ele} = '{target}' 
            order by date""" .format(table_ele=table_ele, target=target)
        result = mssql.exec_query(sql)
    except Exception as e:
        print("Query '{table_ele}': '{target}' unsuccessfully:".format(table_ele=table_ele, target=target), e)
    else:
        print("Query '{table_ele}': '{target}' successfully!".format(table_ele=table_ele, target=target))
        return result


# delete information under a tag_id
def delete_table_id(tag_id):
    try:
        sql = """
        delete from baum_test 
        where tag_id ='{tag_id}'
        """ .format(tag_id=tag_id)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Delete '{tag_id}' unsuccessfully:".format(tag_id=tag_id), e)
    else:
        print("Delete '{tag_id}' successful!".format(tag_id=tag_id))


# precondition: create only_read Role: Role_r ; read and write Role: Role_rw
# create SQL Server login name and grant to read right with default database Baum and default table baum_test
def create_login_r(username, password):
    sql = """
        EXEC sp_addlogin '{0}','{1}','Baum'
        create user {0} for login {0} with default_schema=Role_r
        EXEC sp_addrolemember 'Role_r','{0}'
        """.format(username, password)
    mssql.exec_non_query(sql)


# create SQL Server login name and grant to read, write right with default database Baum and default table baum_test
def create_login_rw(username, password):
    sql = """
        EXEC sp_addlogin '{0}','{1}','Baum'
        create user {0} for login {0} with default_schema=Role_rw
        EXEC sp_addrolemember 'Role_rw','{0}'
        """.format(username, password)
    mssql.exec_non_query(sql)

# ------------------------------------------------------------------------------
# ----------------------MAPS----------------------------------------------------


# GPS location mark on map
# Connect points in time order
# baums: list from query
def gps_map_marker(baums):
    import folium
    import webbrowser
    gpss = []
    for baum in baums:
        g = baum['GPS']
        gps = eval('[' + g + ']')
        gpss.append(gps)
        info = baum['tag_id'] + ' ' + baum['date']
        if gpss[0] == gpss[-1]:
            m = folium.Map(location=gpss[0], zoom_start=16)
        folium.Marker(gps, popup=info).add_to(m)
    ls = folium.PolyLine(locations=gpss, color='blue', opacity='0.5')
    ls.add_to(m)
    m.save('temp.html')
    webbrowser.open("temp.html")




# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# create user Role: Role_rw and Role_r
# def creat_user_role():
#     sql="""
#     EXEC sp_addrole 'Role_rw'
#     GRANT SELECT,INSERT ON baum_test TO Role_rw
#     EXEC sp_addrole 'Role_r'
#     GRANT SELECT ON baum_test TO Role_r
#     """
#     mssql.exec_non_query(sql)


# def create_table1(baum):        # according to dict to create table
#     li=['tag_id', 'device_id', 'GPS', 'date']       # column name
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


# def drop_table(baum):
#     #  complete delete
#     sql = "drop table {table_name}" .format(table_name=baum['tag_id'])
#     mssql.exec_non_query(sql)


# def insert_table(baum):     # insert to the table, baum: dict..
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




