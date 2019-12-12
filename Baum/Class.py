#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pymssql


class MSSQL:
    def __init__(self, host, user, pwd, db):  # creat Class, initialize: adress, username, password, database
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_connect(self):  # connect to the database, return: conn.cursor()
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8', autocommit = True)
        cur = self.conn.cursor()  # get cursor
        if not cur:
            return (NameError, "connect to the database is faul.")
        else:
            return cur

    def exec_query(self, sql):  # execute query sentence
        cur = self.get_connect()  # get database connect information获得数据库连接信息
        cur.execute(sql)
        resList = cur.fetchall()  # get queried result
        self.conn.close()   # close the connect
        return resList      # return result; list

    def exec_non_query(self, sql):       # execute non query sentence
        cur = self.get_connect()
        cur.execute(sql)
        self.conn.close()



