#!/usr/bin/env python
# _*_ coding:utf-8 _*_



def main(server, user, password, database):
    import Class
    global mssql
    mssql = Class.MSSQL(server, user, password, database)
    return mssql




def create_table(table_name):

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


def drop_table(table_name):
    #  complete delete
    sql = "drop table {0}" .format(table_name)
    mssql.exec_non_query(sql)


def insert_table(table_name, index, GPS, date):
    sql = "insert into %s values('%s', '%s', '%s')" %(table_name, index, GPS , date )
    mssql.exec_non_query(sql)







# def delete_row(table_name, cursor, row_number='' )
#     if row_number is NULL
#         sql = "delete Nr=max(Nr) from %s where Nr=max(Nr)" % (table_name)




