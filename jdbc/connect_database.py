#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='db_ylstg')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from bas_hospital_rms")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : ",str(data))

# 关闭数据库连接
db.close()