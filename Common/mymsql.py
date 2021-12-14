# -*- coding: utf-8 -*-
# @Time : 2021/7/20 22:11
# @Author : Liangjiajing
# @FileName: mymsql.py
# @Email : 1369462217@qq.com
import pymysql


class DB:
    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self.con.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.cursor()


databases_conf = dict(
    host="xxx",
    user="xxx",
    password="xxx",
    database="xxx",
    port="xxx",
    charset="xxx"
)
with DB(databases_conf) as cur:
    cur.execute("sql语句")
