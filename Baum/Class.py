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
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # get cursor
        if not cur:
            return (NameError, "connect to the database is faul.")
        else:
            return cur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def exec_query(self, sql):  # 执行Sql语句函数，返回结果
        cur = self.get_connect()  # 获得数据库连接信息
        cur.execute(sql)  # 执行Sql语句
        resList = cur.fetchall()  # 获得所有的查询结果
        # 查询完毕后必须关闭连接
        # self.conn.close()  # 返回查询结果
        return resList

    def exec_non_query(self, sql):       # execute non query sentence
        cur = self.get_connect()
        cur.execute(sql)
        self.conn.commit()
        # self.conn.close()



