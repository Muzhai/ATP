#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# connect to server
def main(host, user, password, database, default_table='baum_test'):
    try:
        import Class
        global table_name
        table_name = default_table
        global mssql
        mssql = Class.MSSQL(host, user, password, database)
    except Exception as e:
        print("Connect to the database unsuccessful:", e)
    else:
        print("Connect to the database successful!")
        return mssql


# create a table tag_id, device_id, GPS, date
def create_table(table):
    try:
        sql = """
        IF OBJECT_ID('{0}', 'U') IS NOT NULL
            DROP TABLE {0}
        CREATE TABLE {0} (
            tag_id VARCHAR(100) NOT NULL,
            device_id VARCHAR(100),
            GPS varchar(100),
            date varchar(100))
        """.format(table)
        mssql.exec_non_query(sql)
    except Exception as e:
        print("Create table unsuccessful:", e)
    else:
        print("Create table successful!")


# delete table
def drop_table(table):
    #  complete delete
    sql = "drop table {table_name}" .format(table_name=table)
    mssql.exec_non_query(sql)


# insert to table baum_test; baum_test is a default table; 'baum' is a dictionary
def insert_table(baum):
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
def insert_table_batch(baum_list):
    for baum in baum_list:
        insert_table(baum)


# read table total
def query_table(table):
    try:
        sql = "select * from {table_name}".format(table_name=table)
        result=mssql.exec_query(sql)
    except Exception as e:
        print("Query '{table_name}' unsuccessfully:".format(table_name=table), e)
    else:
        print("Query '{table_name}' successfully!".format(table_name=table))
        return result


# query table with tag_id and order by data
def query_table_id(tag_id):
    try:
        sql = """
            select * from {table_name} 
            where tag_id = '{tag_id}' 
            order by date""" .format(tag_id=tag_id, table_name=table_name)
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
            select * from {table_name} 
            where {table_ele} = '{target}' 
            order by date""" .format(table_ele=table_ele, target=target, table_name=table_name)
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
        delete from {table_name} 
        where tag_id ='{tag_id}'
        """ .format(tag_id=tag_id, table_name=table_name)
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
    gps_lat_lon = []
    for baum in baums:
        g = baum['GPS']
        gps = eval('[' + g + ']')
        gpss.append(gps)
        info = 'Tag ID: ' + baum['tag_id'] + ' ' + 'Device ID: ' + baum['device_id'] + ' ' + 'Date: ' + baum['date']      # add information
        if gpss[0] == gpss[-1]:
            m = folium.Map(location=gpss[0][0:2], zoom_start=16)
        folium.Marker(gps[0:2], popup=info).add_to(m)
    for lat_lon in gpss:
        gps_lat_lon.append(lat_lon[0:2])
    ls = folium.PolyLine(locations=gps_lat_lon, color='blue', opacity='0.5')
    ls.add_to(m)
    m.save('temp.html')
    webbrowser.open("temp.html")





