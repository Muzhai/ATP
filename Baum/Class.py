#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pymssql


class MSSQL:
    def __init__(self, host, user, pwd, db):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def get_connect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not cur:
            return (NameError, "连接数据库失败")
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

    def exec_non_query(self, sql):
        cur = self.get_connect()
        cur.execute(sql)
        self.conn.commit()
        # self.conn.close()


