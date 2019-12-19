#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import pyodbc


class MSSQL:
    def __init__(self, host, user, pwd, db, server='{SQL Server}'):  # creat Class, initialize: address, username, password, database
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.server = server

    def get_connect(self):  # connect to the database, return: conn.cursor()
        conct = {'server': self.host,
                 'user': self.user,
                 'pwd': self.pwd,
                 'database': self.db,
                 'driver': self.server}
        self.conn = pyodbc.connect(
            '''
        DRIVER={info[driver]};
        SERVER={info[server]};
        DATABASE={info[database]};
        UID={info[user]};
        PWD={info[pwd]};
        autocommit = True
        '''.format(info=conct))
        cur = self.conn.cursor()  # get cursor
        if not cur:
            return (NameError, "connect to the database is faul.")
        else:
            return cur

    def exec_query(self, sql):  # execute query sentence
        cur = self.get_connect()  # get database connect information
        cur.execute(sql)
        columns = [column[0] for column in cur.description]
        results = []
        for row in cur.fetchall():
            results.append(dict(zip(columns, row)))
        self.conn.close()   # close the connect
        return results      # return result; list

    def exec_non_query(self, sql):       # execute non query sentence
        cur = self.get_connect()
        cur.execute(sql)
        self.conn.close()







